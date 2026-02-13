# save as buy_vs_rent_alpha.py
import numpy as np
import matplotlib.pyplot as plt

# --- Configuration ---
YEARS = 10
NUM_SIMULATIONS = 200_000
SEED = np.random.randint(0, 1000)

# ----- Inputs with uncertainty (modeled with multivariate normal where appropriate) -----
# Home Price Appreciation
MEAN_HOME_APPRECIATION = 0.05
STD_DEV_HOME_APPRECIATION = 0.03

# Investment Returns
MEAN_INVEST_RETURN = 0.07
STD_DEV_INVEST_RETURN = 0.05

# Rent Growth
RENT = 3_000.0  # monthly
MEAN_RENT_GROWTH = 0.03
STD_DEV_RENT_GROWTH = 0.02

# Correlation between appreciation and rent growth (optional)
APP_RENT_CORR = 0.4

# ----- Fixed Inputs -----
HOME_PRICE = 700_000.0
DOWN_PAYMENT_PERCENT = 0.20
MORTGAGE_RATE = 0.06
MORTGAGE_TERM_MONTHS = 360  # 30 years
PROPERTY_TAX_RATE = 0.049  # annual fraction of home value
MAINTENANCE_RATE = 0.01  # annual fraction of home value
CLOSING_COSTS_PERCENT = 0.03
SELLING_COSTS_PERCENT = 0.06
MARGINAL_TAX_RATE = 0.30
HOME_INSURANCE_RATE = 0.005  # annual fraction of home value

# Derived
DOWN_PAYMENT = HOME_PRICE * DOWN_PAYMENT_PERCENT
INITIAL_OUTLAY = DOWN_PAYMENT + HOME_PRICE * CLOSING_COSTS_PERCENT
MORTGAGE_AMOUNT = HOME_PRICE - DOWN_PAYMENT


def vectorized_buy_vs_rent(years=YEARS, n_sims=NUM_SIMULATIONS, seed=SEED):
    rng = np.random.default_rng(seed)

    # Precompute mortgage monthly payment (fixed)
    monthly_rate = MORTGAGE_RATE / 12.0
    num_payments = MORTGAGE_TERM_MONTHS
    mortgage_payment = (
        MORTGAGE_AMOUNT * (monthly_rate * (1 + monthly_rate) ** num_payments) / ((1 + monthly_rate) ** num_payments - 1)
    )

    # --- Sample annual random variables in vectorized form ---
    # We'll draw annual appreciation and rent growth jointly to allow correlation.
    cov_matrix = np.array(
        [
            [STD_DEV_HOME_APPRECIATION**2, APP_RENT_CORR * STD_DEV_HOME_APPRECIATION * STD_DEV_RENT_GROWTH],
            [APP_RENT_CORR * STD_DEV_HOME_APPRECIATION * STD_DEV_RENT_GROWTH, STD_DEV_RENT_GROWTH**2],
        ]
    )
    # shape: (n_sims, years, 2)
    mvnorm_samples = rng.multivariate_normal(
        mean=[MEAN_HOME_APPRECIATION, MEAN_RENT_GROWTH],
        cov=cov_matrix,
        size=(n_sims, years),
    )  # returns shape (n_sims, years, 2)
    annual_home_appreciation = mvnorm_samples[:, :, 0]  # shape (n_sims, years)
    annual_rent_growth = mvnorm_samples[:, :, 1]  # shape (n_sims, years)

    # Investment returns sampled independently (could correlate with equities if desired)
    annual_invest_return = rng.normal(MEAN_INVEST_RETURN, STD_DEV_INVEST_RETURN, size=(n_sims, years))

    # --- Vectorized annual accounting (approximate monthly by annual compounding) ---
    # Start-of-simulation values repeated per-sim
    home_value = np.full(shape=(n_sims,), fill_value=HOME_PRICE, dtype=float)
    mortgage_balance = np.full(shape=(n_sims,), fill_value=MORTGAGE_AMOUNT, dtype=float)
    current_rent = np.full(shape=(n_sims,), fill_value=RENT, dtype=float)

    # Portfolios: buyer has zero initial investable cash (assumes down-payment was used),
    # renter starts with the initial outlay invested.
    portfolio_buy = np.zeros(shape=(n_sims,), dtype=float)
    portfolio_rent = np.full(shape=(n_sims,), fill_value=INITIAL_OUTLAY, dtype=float)

    # For speed: vectorized loop over years (only YEARS iterations; each iteration operates on arrays of size n_sims)
    for y in range(years):
        # annual factors
        a_home_appreciation = annual_home_appreciation[:, y]
        a_rent = annual_rent_growth[:, y]
        a_inv = annual_invest_return[:, y]

        # Grow home value and portfolios annually (approximate monthly compounding)
        home_value = home_value * (1.0 + a_home_appreciation)

        # Investment returns applied to portfolios for the year
        portfolio_buy = portfolio_buy * (1.0 + a_inv)
        portfolio_rent = portfolio_rent * (1.0 + a_inv)

        # --- Amortization and Interest Calculation (Exact Monthly) ---
        # We need to calculate the exact interest paid this year for tax purposes
        # and update the mortgage balance.
        annual_interest_paid = np.zeros(shape=(n_sims,), dtype=float)

        # Only process sims with active mortgage
        active_mortgage = mortgage_balance > 0
        if np.any(active_mortgage):
            bal = mortgage_balance[active_mortgage]
            interest_acc = np.zeros_like(bal)

            # Iterate 12 months
            for _ in range(12):
                interest = bal * monthly_rate
                principal = mortgage_payment - interest
                # If principal payment > balance, we pay off the rest
                # (In a vectorized fixed payment model, we just max(0, bal-princ))
                # But we should be careful not to over-count interest if balance is small.
                # For simplicity with large N, standard formula is fine until payoff.

                interest_acc += interest
                bal = np.maximum(bal - principal, 0.0)

            mortgage_balance[active_mortgage] = bal
            annual_interest_paid[active_mortgage] = interest_acc

        # Annual property tax and maintenance calculated on current home value
        annual_property_tax = home_value * PROPERTY_TAX_RATE
        annual_maintenance = home_value * MAINTENANCE_RATE
        annual_insurance = home_value * HOME_INSURANCE_RATE

        # Annual mortgage payments: convert monthly mortgage payment to annual cash outflow
        annual_mortgage_outflow = mortgage_payment * 12.0

        # Tax deductions: Mortgage interest + Property Tax
        tax_deductions = annual_interest_paid + annual_property_tax
        tax_savings = tax_deductions * MARGINAL_TAX_RATE

        # Annual rent paid by renter (12 months), rent grows annually once per year
        annual_rent_paid = current_rent * 12.0

        # Differential cashflow = buyer annual cost - renter annual cost
        # Buyer pays mortgage + prop tax + maint + insurance - tax_savings
        buyer_annual_cost = (
            annual_mortgage_outflow + annual_property_tax + annual_maintenance + annual_insurance - tax_savings
        )
        diff_annual = buyer_annual_cost - annual_rent_paid

        # Where diff_annual > 0 renter invests the positive difference
        invest_by_renter = np.where(diff_annual > 0, diff_annual, 0.0)
        invest_by_buyer = np.where(diff_annual < 0, -diff_annual, 0.0)

        portfolio_rent += invest_by_renter
        portfolio_buy += invest_by_buyer

        # Update rent for next year
        current_rent = current_rent * (1.0 + a_rent)

    # Final net worths
    equity = home_value - mortgage_balance
    final_buy_net_worth = equity - (home_value * SELLING_COSTS_PERCENT) + portfolio_buy
    final_rent_net_worth = portfolio_rent

    return (
        final_buy_net_worth,
        final_rent_net_worth,
        mortgage_payment,
        annual_home_appreciation,
        annual_rent_growth,
        annual_invest_return,
    )


def main():
    (
        buy_results,
        rent_results,
        mortgage_payment,
        annual_home_appreciation,
        annual_rent_growth,
        annual_invest_return,
    ) = vectorized_buy_vs_rent()

    # statistics
    def summarize(arr):
        return {
            "mean": np.mean(arr),
            "median": np.median(arr),
            "5%": np.percentile(arr, 5),
            "95%": np.percentile(arr, 95),
        }

    buy_stats = summarize(buy_results)
    rent_stats = summarize(rent_results)

    print(f"Simulation: {YEARS} years, {NUM_SIMULATIONS:,} sims")
    print(f"Mortgage term: {MORTGAGE_TERM_MONTHS} months")
    print(f"Monthly mortgage payment (approx): ${mortgage_payment:,.2f}\n")
    print("Buying stats (final net worth):", buy_stats)
    print("Renting stats (final net worth):", rent_stats)

    diff = buy_results - rent_results
    print(f"\nProbability buying results in higher net worth: {np.mean(buy_results > rent_results):.2%}")
    print(f"Median difference: ${np.median(diff):,.0f}")

    # --- Analysis of Drivers ---
    print("\n--- Analysis of Drivers ---")
    # Calculate mean annual inputs per simulation
    mean_home_app = np.mean(annual_home_appreciation, axis=1)
    mean_rent_growth = np.mean(annual_rent_growth, axis=1)
    mean_invest_ret = np.mean(annual_invest_return, axis=1)

    # Correlation with difference (Buy - Rent)
    corr_home = np.corrcoef(mean_home_app, diff)[0, 1]
    corr_rent = np.corrcoef(mean_rent_growth, diff)[0, 1]
    corr_invest = np.corrcoef(mean_invest_ret, diff)[0, 1]

    print("Correlation with Buy-Rent Difference:")
    print(f"  Mean Home Appreciation: {corr_home:.3f}")
    print(f"  Mean Rent Growth:       {corr_rent:.3f}")
    print(f"  Mean Investment Return: {corr_invest:.3f}")

    # Extreme cases
    max_diff_idx = np.argmax(diff)
    min_diff_idx = np.argmin(diff)

    print(f"\nMax Benefit to Buying (Sim #{max_diff_idx}): ${diff[max_diff_idx]:,.0f}")
    print(f"  Avg Home App: {mean_home_app[max_diff_idx]:.2%}")
    print(f"  Avg Rent Growth: {mean_rent_growth[max_diff_idx]:.2%}")
    print(f"  Avg Invest Return: {mean_invest_ret[max_diff_idx]:.2%}")

    print(f"\nMax Benefit to Renting (Sim #{min_diff_idx}): ${-diff[min_diff_idx]:,.0f}")
    print(f"  Avg Home App: {mean_home_app[min_diff_idx]:.2%}")
    print(f"  Avg Rent Growth: {mean_rent_growth[min_diff_idx]:.2%}")
    print(f"  Avg Invest Return: {mean_invest_ret[min_diff_idx]:.2%}")

    # Plot difference distribution
    plt.figure()
    plt.hist(diff, bins=80, alpha=0.7)
    plt.axvline(
        np.median(diff),
        color="k",
        linestyle="--",
        label=f"median diff = ${np.median(diff):,.0f}",
    )
    plt.xlabel("Buy - Rent final net worth ($)")
    plt.ylabel("Frequency")
    plt.title(f"Distribution of Buy vs Rent, Net Worth after {YEARS} years")
    plt.legend()
    plt.grid(True)
    plt.savefig("buy_vs_rent_alpha.png")
    print("\nSaved histogram to buy_vs_rent_alpha.png")


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"Error running main: {e}")
