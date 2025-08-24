import numpy as np
import logging

from settings import *

# --- Setup logging ---
logger = logging.getLogger("spectrum")
logger.setLevel(logging.INFO)
ch = logging.StreamHandler()
ch.setFormatter(logging.Formatter(fmt='%(asctime)s [%(levelname)s] %(message)s', datefmt='%H:%M:%S'))
logger.addHandler(ch)


def detect_preambles(mag, samples_per_bit, threshold, tolerance=0.1):
    """
    Detect preambles in the magnitude array based on a specific pattern.

    Args:
        mag: Array of signal magnitudes (e.g., np.abs(I + 1j*Q)).
        samples_per_bit: Number of samples per bit in the signal.
        threshold: Threshold value for comparisons.
        tolerance: Fractional tolerance for "close enough" comparisons (e.g., 0.1 for ±10%).

    Returns:
        List of starting indices where preambles are detected.
    """
    preambles = []
    window_size = 16 * samples_per_bit

    # Check if mag is long enough
    if len(mag) < window_size:
        logger.warning(f"Input array too short: {len(mag)} < {window_size}")
        return preambles

    for i in range(0, len(mag) - window_size + 1, samples_per_bit):  # Step by bit
        w = mag[i:i + window_size]

        # Compute means for each bit (assuming 2 samples per bit for simplicity)
        bit_means = [np.mean(w[j * samples_per_bit:(j + 1) * samples_per_bit]) for j in range(16)]

        # Check conditions with tolerance
        thresh_min = threshold * (1 - tolerance)
        thresh_max = threshold * (1 + tolerance)

        if (bit_means[0] > thresh_min and bit_means[1] > thresh_min and
                bit_means[2] < thresh_max and bit_means[3] < thresh_max):
            if (bit_means[4] > thresh_min and bit_means[5] > thresh_min and
                    bit_means[6] < thresh_max and bit_means[7] < thresh_max):
                if bit_means[14] > thresh_min and bit_means[15] > thresh_min:
                    logger.debug(f"condition passed {i}: {bit_means[14]:.2f},{bit_means[15]:.2f} > {threshold:.2f}")
                    preambles.append(i)

    return preambles


def decode_bits(mag, start, samples_per_bit, bits=32, threshold=0.0, tolerance=0.1):
    """
    Decode binary bits from the magnitude array starting after a preamble.

    Args:
        mag: Array of signal magnitudes (e.g., np.abs(I + 1j*Q)).
        start: Starting index of the preamble.
        samples_per_bit: Number of samples per bit in the signal.
        bits: Number of bits to decode (default: 32).
        threshold: Threshold for bit comparison (default: 0, uses mean of window).
        tolerance: Fractional tolerance for "close enough" comparisons (default: 0.1).

    Returns:
        List of decoded bits (0 or 1).
    """
    msg_bits = []
    offset = start + 16 * samples_per_bit  # Skip preamble
    if offset + bits * samples_per_bit > len(mag):
        logger.warning(f"Insufficient samples to decode {bits} bits at offset {offset}")
        return msg_bits

    for b in range(bits):
        # Extract window for one bit
        bit_window = mag[offset + b * samples_per_bit: offset + (b + 1) * samples_per_bit]
        if len(bit_window) < samples_per_bit:
            logger.warning(f"Incomplete bit window at index {offset + b * samples_per_bit}")
            break

        # Compute mean of the bit window
        bit_mean = np.mean(bit_window)
        # Use provided threshold or default to window mean
        thresh = threshold if threshold != 0.0 else np.mean(mag[offset:offset + bits * samples_per_bit])
        thresh_min = thresh * (1 - tolerance)

        # Decode bit: 1 if mean is above threshold (within tolerance), else 0
        bit = 1 if bit_mean > thresh_min else 0
        msg_bits.append(bit)
        logger.debug(f"Bit {b} at index {offset + b * samples_per_bit}: {bit_mean=:.2f}, {thresh=:.2f}, bit={bit}")

    return msg_bits


def bits_to_bytes(bits):
    """
    Convert a list of bits to bytes.

    Args:
        bits: List of binary values (0 or 1).

    Returns:
        bytes: Converted bytes object.
    """
    if not bits:
        return bytes()

    # Validate bits
    if not all(b in (0, 1) for b in bits):
        logger.error("Bits must be 0 or 1")
        raise ValueError("Bits must be 0 or 1")

    # Pad with zeros if needed to complete the last byte
    padded_bits = bits + [0] * (8 - len(bits) % 8) if len(bits) % 8 != 0 else bits
    logger.debug(f"Padded bits to length {len(padded_bits)} for complete bytes")

    out = []
    for i in range(0, len(padded_bits), 8):
        byte = 0
        for b in padded_bits[i:i + 8]:
            byte = (byte << 1) | b
        out.append(byte)

    return bytes(out)


def check_crc(bytes_out):
    """
    Verify the CRC of an ADS-B extended squitter message.

    Computes the CRC-24 over the first 11 bytes (88 bits) using the polynomial
    0xFFF409 and compares it with the parity field in bytes 12–14 (24 bits).

    Args:
        bytestr (bytes or bytearray): A 14-byte ADS-B message.

    Returns:
        bool: True if the CRC check passes (message is valid), False otherwise.

    Raises:
        ValueError: If `bytestr` is not bytes/bytearray or has fewer than 14 bytes.
    """
    if not isinstance(bytes_out, (bytes, bytearray)):
        logger.error("Input must be bytes or bytearray")
        raise ValueError("Input must be bytes or bytearray")
    if len(bytes_out) < ADSB_SHORT_MSG_LEN:
        logger.error(f"Input too short: {len(bytes_out)} bytes, expected {ADSB_SHORT_MSG_LEN}")
        raise ValueError(f"ADS-B message must be {ADSB_SHORT_MSG_LEN} bytes")

    # Convert first 11 bytes to a 88-bit integer
    msg = 0
    for i in range(11):
        msg = (msg << 8) | bytes_out[i]

    # Extract received CRC (bytes 12–14, 24 bits)
    received_crc = (bytes_out[11] << 16) | (bytes_out[12] << 8) | bytes_out[13]

    # Compute CRC-24
    poly = ADSB_CRC_POLY
    remainder = msg
    for _ in range(88):  # Process 88 bits
        if remainder & (1 << 87):  # Check MSB
            remainder ^= (poly << (87 - 24))  # Align polynomial with MSB
        remainder <<= 1
    remainder >>= (87 - 24)  # Extract 24-bit remainder

    # Check if computed CRC matches received CRC
    return (remainder ^ received_crc) == 0


def test_check_crc():
    """
    # Message (DF=17, TypeCode=4, callsign=UAL123)
    """
    msg_hex = "8da49fd29985a90348383ff96fdf"
    msg_bytes = bytes.fromhex(msg_hex)

    valid_crc = check_crc(msg_bytes)
    logger.info("valid crc:", valid_crc)
    assert valid_crc is True, f"Expected valid crc but got {valid_crc=}"


def decode_callsign(bytes_out):
    """
    Decode the callsign from an ADS-B ES (DF17/DF18) message.

    Uses the 56-bit ME field (bytes 4..10, 0-based). Valid only for Type Code 1..4.
    Returns the 8-char callsign stripped of trailing spaces.
    """
    if len(bytes_out) < 14:
        raise IndexError("ADS-B ES message must be 14 bytes")

    # Type Code is the top 5 bits of ME (byte 4 >> 3).
    type_code = bytes_out[4] >> 3
    if not (1 <= type_code <= 4):
        # Not an Aircraft Identification message; either return empty or raise.
        # Raise helps catch using the wrong hex in tests.
        raise ValueError(f"Not an identification message (type code={type_code}).")

    # Build the 56-bit ME value (bytes 4..10 inclusive).
    ident_bits = 0
    for i in range(4, 11):
        ident_bits = (ident_bits << 8) | bytes_out[i]

    # ident_bits layout (MSB→LSB):
    # [ TC:5 | EC:3 | Char1:6 | Char2:6 | ... | Char8:6 ]
    callsign = []
    # Start with the first character at bits 47..42; peel left to right.
    tmp = ident_bits
    for _ in range(8):
        char_code = (tmp >> 42) & 0x3F
        callsign.append(ADSB_CHAR_SET[char_code])
        tmp <<= 6  # move next 6-bit code into position

    return "".join(callsign).rstrip()


def test_callsign():
    """
    # Encoded callsign: "UAL123"
    # From a real ADS-B message with ICAO 0xA12345
    # Message (DF=17, TypeCode=4, callsign=UAL123)
    """
    msg_hex = "8da49fd2223b3e77d41820853907"
    msg_bytes = bytes.fromhex(msg_hex)

    callsign = decode_callsign(msg_bytes)
    logger.info("decoded callsign:", callsign)
    assert callsign == "UAL123", f"Expected UAL123 but got {callsign=}"


def decode_velocity(bytes_out):
    """
    Decode the Velocity field from an ADS-B extended squitter message (Type Code 19, subtypes 1–2).

    Extracts airborne velocity data from bytes 8–14, computing ground speed and heading
    from East-West and North-South velocity components. Requires NumPy for calculations.

    Args:
        bytes_out (bytes or bytearray): A 14-byte ADS-B message containing velocity data in bytes 8–14.

    Returns:
        dict: (ground_speed_kts, heading_deg)
            - (float or None): Ground speed in knots, or None if invalid.
            - (float or None): Heading in degrees (0–359), or None if invalid.

    Raises:
        IndexError: If `bytes_out` has fewer than 14 bytes.
    """
    result = {
        "ground_speed_kts": None,
        "heading_deg": None,
        "airspeed_kts": None,
        "airspeed_type": None,
        "vertical_rate_fpm": None,
        "vr_source": None,
    }
    subtype = (bytes_out[7] >> 5) & 0x07
    if subtype in (1, 2):
        ew_dir = (bytes_out[8] >> 7) & 0x01
        ew_vel = (((bytes_out[8] & 0x7F) << 3) | (bytes_out[9] >> 5)) - 1
        ns_dir = (bytes_out[9] >> 4) & 0x01
        ns_vel = (((bytes_out[9] & 0x0F) << 6) | (bytes_out[10] >> 2)) - 1

        if ew_vel >= 0 and ns_vel >= 0:
            result["ground_speed_kts"] = np.sqrt(ew_vel**2 + ns_vel**2)
            x = np.arctan2(ew_vel * (-1 if ew_dir else 1), ns_vel * (-1 if ns_dir else 1))
            result["heading_deg"] = np.degrees(x) % 360

        elif subtype in (3, 4):  # Airspeed + heading
            airspeed_type = (bytes_out[8] >> 6) & 0x01  # 0 = IAS, 1 = TAS
            airspeed_raw = (((bytes_out[8] & 0x3F) << 4) | (bytes_out[9] >> 4)) - 1
            if airspeed_raw >= 0:
                result["airspeed_kts"] = airspeed_raw
                result["airspeed_type"] = "TAS" if airspeed_type else "IAS"

            hdg_status = (bytes_out[9] >> 3) & 0x01  # 0 = not valid
            hdg_raw = ((bytes_out[9] & 0x07) << 7) | (bytes_out[10] >> 1)
            if hdg_status and hdg_raw > 0:
                result["heading_deg"] = (hdg_raw * 360.0) / 1024.0

        elif subtype == 5:  # Vertical rate only
            vr_sign = (bytes_out[9] >> 3) & 0x01
            vr_raw = (((bytes_out[9] & 0x07) << 6) | (bytes_out[10] >> 2)) - 1
            if vr_raw >= 0:
                vr = vr_raw * 64  # ft/min
                result["vertical_rate_fpm"] = -vr if vr_sign else vr

            vr_source_bit = bytes_out[10] & 0x01
            result["vr_source"] = "GNSS" if vr_source_bit else "Baro"

    return result


def test_groundspeed_subtype_1():
    """
    # Example: Type Code 19, Subtype 1 (groundspeed)
    """
    msg_hex = "8D40621D58C382D690C8AC2863A7"
    msg_bytes = bytes.fromhex(msg_hex)

    result = decode_velocity(msg_bytes)

    assert result["ground_speed_kts"] is not None
    assert result["heading_deg"] is not None
    assert 0 <= result["heading_deg"] <= 360


def test_airspeed_supersonic_subtype_3():
    """
    # Synthetic example, supersonic TAS ~1100 kt, heading ~90 deg
    """
    msg_hex = "8D4840D699107FB5C00408000000"
    msg_bytes = bytes.fromhex(msg_hex)

    result = decode_velocity(msg_bytes)

    assert result["airspeed_kts"] > 1000
    assert result["airspeed_type"] in ("IAS", "TAS")
    assert 80 <= result["heading_deg"] <= 100


def test_airspeed_subsonic_subtype_4():
    """
    # Subtype 4: Airspeed (subsonic)
    # Real-world style message, IAS ~240 kt, heading ~180 deg
    """
    msg_hex = "8D40621D58C382D690C8AC2863A7"
    msg_bytes = bytes.fromhex(msg_hex)

    result = decode_velocity(msg_bytes)

    assert result["airspeed_kts"] is not None
    assert result["airspeed_kts"] < 600
    assert result["airspeed_type"] == "IAS"
    assert 150 <= result["heading_deg"] <= 210


def test_vertical_rate_subtype_5_climb():
    """
    # Subtype 5: Vertical Rate
    # Synthetic example, climb ~1280 fpm, GNSS source
    """
    msg_hex = "8D40621D58C382D690C8AC2863B5"
    msg_bytes = bytes.fromhex(msg_hex)

    result = decode_velocity(msg_bytes)

    assert result["vertical_rate_fpm"] > 0
    assert result["vr_source"] in ("GNSS", "Baro")


def test_vertical_rate_subtype_5_descent():
    """
    # Synthetic example, descent ~640 fpm, Baro source
    """
    msg_hex = "8D40621D58C382D690C8AC2863C4"
    msg_bytes = bytes.fromhex(msg_hex)

    result = decode_velocity(msg_bytes)

    assert result["vertical_rate_fpm"] < 0
    assert result["vr_source"] == "Baro"


def parse_adsb(bytes_out):
    """
    Parse an ADS-B message from a byte string.

    Args:
        bytes_out: bytes or bytearray containing the ADS-B message (at least 7 bytes).

    Returns:
        dict: Parsed fields (DF, ICAO, TypeCode, Altitude_ft if applicable).

    Raises:
        ValueError: If bytestr is too short or invalid.
    """
    if not isinstance(bytes_out, (bytes, bytearray)):
        logger.error("Input must be bytes or bytearray")
        raise ValueError("Input must be bytes or bytearray")
    if len(bytes_out) < ADSB_SHORT_MSG_LEN:
        logger.error(f"Input too short: {len(bytes_out)} bytes, expected {ADSB_SHORT_MSG_LEN}")
        raise ValueError(f"ADS-B message must be at least {ADSB_SHORT_MSG_LEN} bytes")

    # Extract Downlink Format (DF): bits 1–5 of first byte, Extract ICAO address: bytes 2–4 (24 bits)
    info = {
        "RawHex": f"{bytes_out.hex()}",
        "CRCValid": check_crc(bytestr),
    }
    if not info["CRCValid"]:
        logger.warning(f"CRC check failed for message: {info['RawHex']}")
        return info

    info["DF"] = (bytes_out[0] >> 3) & 0x1F,
    info["ICAO"] = (bytes_out[1] << 16) | (bytes_out[2] << 8) | bytes_out[3],
    info["ICAO_hex"] = f"{info['ICAO']:06X}"  # Hex string for display

    if info["DF"] in ADSB_DF_EXTENDED:
        # Extract Type Code: bits 1–5 of fifth byte
        info["TypeCode"] = bytes_out[4] >> 3
        if info["TypeCode"] in ADSB_TC_IDENTITY_RANGE:
            info["Identification"] = decode_callsign(bytes_out)
        elif info["TypeCode"] in ADSB_TC_ALTITUDE_RANGE:
            # Extract altitude: last 3 bits of byte 6 + all of byte 7
            ext_raw = ((bytes_out[5] & 0x07) << 8) | bytes_out[6]
            info["Altitude_ft"] = ext_raw * ADSB_ALTITUDE_SCALE
        elif info["TypeCode"] in ADSB_TC_VELOCITY_RANGE:
            velocity_results = decode_velocity(bytes_out)
            info.update(velocity_results)
        else:
            logger.debug(f"TypeCode {info['TypeCode']} does not contain altitude")
    else:
        logger.debug(f"DF {info['DF']} is not an extended ADS-B message")

    return info


if __name__ == "__main__":
    test_check_crc()
    test_callsign()
    test_groundspeed_subtype_1()
    test_airspeed_supersonic_subtype_3()
    test_airspeed_subsonic_subtype_4()
    test_vertical_rate_subtype_5_climb()
    test_vertical_rate_subtype_5_descent()
