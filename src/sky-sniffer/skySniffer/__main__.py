import numpy as np
import matplotlib.pyplot as plt
import logging

from .settings import *
from .spectrum import (
    detect_preambles,
    decode_bits,
    bits_to_bytes,
    parse_adsb,
)

# --- Setup logging ---
logger = logging.getLogger("spectrum")
logger.setLevel(logging.INFO)
ch = logging.StreamHandler()
ch.setFormatter(logging.Formatter(fmt='%(asctime)s [%(levelname)s] %(message)s', datefmt='%H:%M:%S'))
logger.addHandler(ch)


def main():
    data = np.fromfile("data/capture.cu8", dtype=np.uint8)
    data = data.astype(np.int16) - 127
    I = data[0::2]
    Q = data[1::2]
    print("Loaded", len(I), "samples")
    complex_signal = I + 1j * Q

    fft = np.fft.fftshift(np.fft.fft(complex_signal))
    plt.plot(20 * np.log10(np.abs(fft)))
    plt.title("Power Spectrum")
    plt.xlabel("Frequency (bins)")
    plt.ylabel("Power (dB)")
    plt.savefig("data/raw.png")

    mag = np.abs(complex_signal)
    plt.plot(mag)
    plt.title("IQ Magnitude")
    plt.xlabel("Sample Index")
    plt.ylabel("Magnitude")
    plt.savefig("data/mag.png")
    plt.clf()

    # Detect preambles
    threshold = np.mean(mag)  # Example: use mean of mag as threshold
    tolerance = 0.1  # 10% tolerance
    preamble_indices = detect_preambles(mag, SAMPLES_PER_BIT, threshold, tolerance)
    print(f"Detected number of preambles: {len(preamble_indices)}")

    # Decode bits for each preamble
    for start in preamble_indices:
        bits = decode_bits(mag, start, SAMPLES_PER_BIT, MSG_BITS, threshold, tolerance)
        if bits:
            logger.debug(f"Bits at preamble {start}: {bits}")
            bytes_out = bits_to_bytes(bits)
            logger.debug(f"Bytes at preamble {start}: {bytes_out.hex()}")
            msg = parse_adsb(bytes_out)
            logger.info(f"ADS-B at index {start}: {msg}")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        pass
    except Exception as err:
        logger.exception("failure, exception", err)
