# save as buy_vs_rent_vectorized.py
import numpy as np
import matplotlib.pyplot as plt

# --- Configuration ---
YEARS = 10
NUM_SIMULATIONS = 200_000
SEED = 42

# ----- Inputs with uncertainty (modeled with multivariate normal where appropriate) -----
# Home Price Appreciation
MEAN_APPRECIATION = 0.05
STD_DEV_APPRECIATION = 0.02

# Investment Returns
MEAN_INVEST_RETURN = 0.07
STD_DEV_INVEST_RETURN = 0.15

# Rent Growth
MEAN_RENT_GROWTH = 0.05
STD_DEV_RENT_GROWTH = 0.02

# Correlation between appreciation and rent growth (optional)
APP_RENT_CORR = 0.4

# ----- Fixed Inputs -----
HOME_PRICE = 700_000.0
DOWN_PAYMENT_PERCENT = 0.20
MORTGAGE_RATE = 0.06
RENT = 3_000.0  # monthly
PROPERTY_TAX_RATE = 0.012  # annual fraction of home value
MAINTENANCE_RATE = 0.01  # annual fraction of home value
CLOSING_COSTS_PERCENT = 0.03
SELLING_COSTS_PERCENT = 0.06

# Derived
DOWN_PAYMENT = HOME_PRICE * DOWN_PAYMENT_PERCENT
INITIAL_OUTLAY = DOWN_PAYMENT + HOME_PRICE * CLOSING_COSTS_PERCENT
MORTGAGE_AMOUNT = HOME_PRICE - DOWN_PAYMENT


def vectorized_buy_vs_rent(years=YEARS, n_sims=NUM_SIMULATIONS, seed=SEED):
    rng = np.random.default_rng(seed)

    # Precompute mortgage monthly payment (fixed)
    monthly_rate = MORTGAGE_RATE / 12.0
    num_payments = int(years * 12)
    mortgage_payment = (
        MORTGAGE_AMOUNT * (monthly_rate * (1 + monthly_rate) ** num_payments) / ((1 + monthly_rate) ** num_payments - 1)
    )

    # --- Sample annual random variables in vectorized form ---
    # We'll draw annual appreciation and rent growth jointly to allow correlation.
    cov_matrix = np.array(
        [
            [STD_DEV_APPRECIATION**2, APP_RENT_CORR * STD_DEV_APPRECIATION * STD_DEV_RENT_GROWTH],
            [APP_RENT_CORR * STD_DEV_APPRECIATION * STD_DEV_RENT_GROWTH, STD_DEV_RENT_GROWTH**2],
        ]
    )
    # shape: (n_sims, years, 2)
    mvnorm_samples = rng.multivariate_normal(
        mean=[MEAN_APPRECIATION, MEAN_RENT_GROWTH], cov=cov_matrix, size=(n_sims, years)
    )  # returns shape (n_sims, years, 2)
    annual_appreciation = mvnorm_samples[:, :, 0]  # shape (n_sims, years)
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
        a_app = annual_appreciation[:, y]
        a_rent = annual_rent_growth[:, y]
        a_inv = annual_invest_return[:, y]

        # Grow home value and portfolios annually (approximate monthly compounding)
        home_value = home_value * (1.0 + a_app)

        # Investment returns applied to portfolios for the year
        portfolio_buy = portfolio_buy * (1.0 + a_inv)
        portfolio_rent = portfolio_rent * (1.0 + a_inv)

        # Annual property tax and maintenance calculated on current home value
        annual_property_tax = home_value * PROPERTY_TAX_RATE
        annual_maintenance = home_value * MAINTENANCE_RATE

        # Annual mortgage payments: convert monthly mortgage payment to annual cash outflow
        annual_mortgage_outflow = mortgage_payment * 12.0

        # Annual rent paid by renter (12 months), rent grows annually once per year
        annual_rent_paid = current_rent * 12.0

        # Differential cashflow = buyer annual cost - renter annual cost
        # Buyer pays mortgage + prop tax + maint ; renter pays rent
        diff_annual = (annual_mortgage_outflow + annual_property_tax + annual_maintenance) - annual_rent_paid

        # Where diff_annual > 0 renter invests the positive difference
        invest_by_renter = np.where(diff_annual > 0, diff_annual, 0.0)
        invest_by_buyer = np.where(diff_annual < 0, -diff_annual, 0.0)

        portfolio_rent += invest_by_renter
        portfolio_buy += invest_by_buyer

        # Update mortgage balance with amortization across 12 months in a vectorized approximate way:
        # Compute monthly principal reduction for each sim for the 12 months of this year, but vectorized:
        # We'll approximate by applying 12 times the standard amortization step using current mortgage balance.
        # This is an approximation but sufficiently accurate for large-scale Monte Carlo; can be replaced with exact per-month vectorized amortization if needed.
        if np.any(mortgage_balance > 0):
            # For sims where mortgage still outstanding, run amortization for 12 months vectorized
            active = mortgage_balance > 0
            bal = mortgage_balance[active]
            # iterate 12 months on these balances in numpy (no Python loops over sims)
            # We'll do 12 vectorized amort steps:
            for _ in range(12):
                interest = bal * monthly_rate
                principal = mortgage_payment - interest
                bal = np.maximum(bal - principal, 0.0)
            mortgage_balance[active] = bal

        # Update rent for next year
        current_rent = current_rent * (1.0 + a_rent)

    # Final net worths
    equity = home_value - mortgage_balance
    final_buy_net_worth = equity - (home_value * SELLING_COSTS_PERCENT) + portfolio_buy
    final_rent_net_worth = portfolio_rent

    return final_buy_net_worth, final_rent_net_worth, mortgage_payment


if __name__ == "__main__":
    buy_results, rent_results, mortgage_payment = vectorized_buy_vs_rent()

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
    print(f"Monthly mortgage payment (approx): ${mortgage_payment:,.2f}\n")
    print("Buying stats (final net worth):", buy_stats)
    print("Renting stats (final net worth):", rent_stats)

    buying_better_prob = np.mean(buy_results > rent_results)
    print(f"\nProbability buying results in higher net worth: {buying_better_prob:.2%}")

    # Plot difference distribution
    diff = buy_results - rent_results
    plt.hist(diff, bins=80, alpha=0.7)
    plt.axvline(np.median(diff), color="k", linestyle="--", label=f"median diff = ${np.median(diff):,.0f}")
    plt.xlabel("Buy - Rent final net worth ($)")
    plt.ylabel("Frequency")
    plt.title(f"Distribution of Buy - Rent Net Worth after {YEARS} years")
    plt.legend()
    plt.grid(True)
    plt.savefig("buy_vs_rent_alpha.png")
    print("Saved histogram to buy_vs_rent_alpha.png")
