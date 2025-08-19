import logging

import numpy as np
from rtlsdr import RtlSdr

# --- Configuration ---
SAMPLE_RATE = 2_400_000  # Hz (your RTL-SDR capture rate)
BIT_RATE = 1_000_000  # ADS-B bit rate
SAMPLES_PER_BIT = SAMPLE_RATE // BIT_RATE
THRESHOLD = 40  # preamble detection threshold
MSG_BITS = 112  # decode long frames
CRC_POLY = 0xFFF409

# --- Setup logging ---
logger = logging.getLogger("adsb_live")
logger.setLevel(logging.DEBUG)

# Create console handler
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)

# Improved format:
formatter = logging.Formatter(
    fmt='%(asctime)s [%(levelname)s] %(message)s',
    datefmt='%H:%M:%S'
)
ch.setFormatter(formatter)
logger.addHandler(ch)


# --- Helpers from previous code ---
def magnitude(i, q):
    return np.sqrt(i * i + q * q)


def detect_preambles(mag, threshold=THRESHOLD):
    preambles = []
    for i in range(0, len(mag) - 16 * SAMPLES_PER_BIT, 1):
        w = mag[i:i + 16 * SAMPLES_PER_BIT]
        if (np.mean(w[0:2]) > threshold > np.mean(w[2:4]) and
                np.mean(w[4:6]) > threshold > np.mean(w[6:8]) and
                np.mean(w[14:16]) > threshold):
            preambles.append(i)
    return preambles


def decode_bits(mag, start, bits=MSG_BITS):
    msg_bits = []
    offset = start + 16 * SAMPLES_PER_BIT
    for b in range(bits):
        bit_window = mag[offset + b * 2: offset + (b + 1) * 2]
        if len(bit_window) < 2:
            break
        msg_bits.append(1 if bit_window[0] > bit_window[1] else 0)
    return msg_bits


def bits_to_bytes(bits):
    out = []
    for i in range(0, len(bits), 8):
        byte = 0
        for b in bits[i:i + 8]:
            byte = (byte << 1) | b
        out.append(byte)
    return out


def crc_mode_s(msg_bits):
    data = 0
    for b in msg_bits:
        data = (data << 1) | b
    msglen = len(msg_bits)
    n = msglen - 24
    data >>= 24
    reg = data
    for i in range(n):
        if reg & (1 << (n - 1 - i)):
            reg ^= CRC_POLY << (n - 1 - i - 24)
    return reg & 0xFFFFFF


def parse_adsb(bytestr):
    df = (bytestr[0] >> 3) & 0x1F
    icao = (bytestr[1] << 16) | (bytestr[2] << 8) | bytestr[3]
    info = {"DF": df, "ICAO": f"{icao:06X}"}
    if df == 17:
        tc = bytestr[4] >> 3
        info["TypeCode"] = tc
        if 9 <= tc <= 18:
            alt_raw = ((bytestr[5] & 0x07) << 8) | bytestr[6]
            info["Altitude_ft"] = alt_raw * 25
    return info


def main():
    # --- Live RTL-SDR capture ---
    sdr = RtlSdr()
    sdr.sample_rate = SAMPLE_RATE
    sdr.center_freq = 1090e6  # ADS-B
    sdr.gain = 'auto'

    try:
        logger.info("Starting live capture... Ctrl-C to stop")
        while True:
            # read 256k IQ samples at a time
            iq = sdr.read_samples(256 * 1024)
            i = np.real(iq).astype(np.int16)
            q = np.imag(iq).astype(np.int16)
            mag = magnitude(i, q)

            preambles = detect_preambles(mag)
            if preambles:
                logger.debug(f"Detected {len(preambles)} preambles in current chunk")

            for p in preambles:
                bits = decode_bits(mag, p)
                if len(bits) < MSG_BITS:
                    logger.debug(f"Incomplete frame at sample {p}, skipping")
                    continue
                msg_bytes = bits_to_bytes(bits)
                if crc_mode_s(bits) == 0:
                    parsed = parse_adsb(msg_bytes)
                    logger.info("Valid ADS-B | ICAO=%s | DF=%d | TC=%d | Alt=%s ft",
                                parsed["ICAO"], parsed["DF"],
                                parsed.get("TypeCode", -1),
                                parsed.get("Altitude_ft", "N/A"),
                                )
                else:
                    hexmsg = "".join(f"{b:02X}" for b in msg_bytes)
                    logger.warning(f"Bad CRC at sample {p}: {hexmsg}")

    finally:
        sdr.close()


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        pass
    except Exception as err:
        logger.exception("failure, exception", err)
