
SAMPLE_RATE = 2_400_000  # Hz (2.4 MHz)
FREQUENCY = 10_900_000  # ADS-B frequency (1090 MHz)
BIT_RATE = 1_000_000  # ADS-B bit rate
SAMPLES_PER_BIT = SAMPLE_RATE // BIT_RATE
MSG_BITS = 112  # decode long frames
CRC_POLY = 0xFFF409

# Constants for ADS-B parsing
ADSB_SHORT_MSG_LEN = 7  # Short Messages (56 bits, 7 bytes)
ADSB_EXTENDED_MSG_LEN = 14  # Extended Messages (112 bits, 14 bytes)
ADSB_DF_EXTENDED = (17, 18)   # Downlink Format for extended messages
ADSB_TC_IDENTITY_RANGE = range(1, 5)  # Type Codes 1-4 for identification
ADSB_TC_ALTITUDE_RANGE = range(9, 19)  # Type Codes 9–18 for altitude
ADSB_TC_VELOCITY_RANGE = range(19, 20)  # Type Codes for 19-20 for velocity
ADSB_ALTITUDE_SCALE = 25  # Altitude scaling factor (feet per raw unit)
ADSB_CRC_POLY = 0xFFF409  # CRC-24 polynomial
ADSB_CHAR_SET = (
    " "                      # 0
    "ABCDEFGHIJKLMNOPQRSTUVWXYZ"  # 1–26
    "     "                  # 27–31 (spaces)
    "0123456789"             # 32–41
    "                      "  # 42–63 (22 spaces)
)  # Total length: 64
