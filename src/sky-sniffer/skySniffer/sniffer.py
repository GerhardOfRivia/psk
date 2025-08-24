import numpy as np
from rtlsdr import RtlSdr
import logging
from settings import *

# --- Logging setup ---
logger = logging.getLogger("sniffer")
logger.setLevel(logging.INFO)
ch = logging.StreamHandler()
ch.setFormatter(logging.Formatter("%(asctime)s [%(levelname)s] %(message)s", "%H:%M:%S"))
logger.addHandler(ch)


def main():
    sdr = RtlSdr()

    sdr.sample_rate = SAMPLE_RATE
    sdr.center_freq = FREQUENCY
    sdr.gain = 'auto'            # Automatic gain

    logger.info("SDR configured: %.1f MHz center, %.1f MHz sample rate",
                sdr.center_freq/1e6, sdr.sample_rate/1e6)

    # --- Read samples ---
    logger.info("Reading 1M samples...")
    samples = sdr.read_samples(1024*1024)

    logger.info("Got %d samples", len(samples))

    # --- Convet to .cu8 format ---
    # Scale float32 complex samples (-1.0 to +1.0) into uint8 (0-255)
    iq = np.empty((samples.size * 2,), dtype=np.uint8)
    iq[0::2] = np.clip((samples.real * 127.5 + 127.5), 0, 255).astype(np.uint8)
    iq[1::2] = np.clip((samples.imag * 127.5 + 127.5), 0, 255).astype(np.uint8)

    # --- Write file ---
    filename = "data/capture.cu8"
    with open(filename, "wb") as f:
        iq.tofile(f)

    logger.info("Wrote %d IQ pairs (%.2f MB) to %s",
                len(samples), iq.nbytes / (1024*1024), filename)

    # --- Cleanup ---
    sdr.close()


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        pass
    except Exception as err:
        logger.exception("failure, exception", err)
