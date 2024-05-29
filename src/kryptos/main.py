_K4 = "OBKRUOXOGHULBSOLIFBBWFLRVQQPRNGKSSOTWTQSJQSSEKZZWATJKLUDIAWINFBNYPVTTMZFPKWGDKZXTJCDIGKUHUAUEKCAR"
K4_ = "OBKRUOXOGHULBSOLIFBBWEASTNORTHEASTOTWTQSJQSSEKZZWATJKLUDIAWINFBBERLINMZFPKWGDKZXTJCDIGKSHUAUEKCAR"
#   = "THE__________________EASTNORTHEAST___________E______E__________BERLIN________E________E______E___"

"""

OBKRUOXOGHULBSOLIFBBWFLRVQQPRNGKSSOTWTQSJQSSEKZZWATJKLUDIAWINFBNYPVTTMZFPKWGDKZXTJCDIGKUHUAUEKCAR

at positions 22–25, ciphertext "FLRV", in the plaintext is "EAST
at positions 26–34, ciphertext "QQPRNGKSS" in the plaintext is "NORTHEAST"
at positions 64-69, ciphertext "NYPVTT", in the plaintext is "BERLIN" 
at positions 70-74, ciphertext "MZFPK", in the plaintext is "CLOCK"
"""


def vigenere_decrypt(ciphertext, key):
    plaintext = []
    key_length = len(key)
    for i, char in enumerate(ciphertext):
        key_char = key[i % key_length]
        key_offset = ord(key_char) - ord("A")
        plaintext_char = chr((ord(char) - ord("A") - key_offset + 26) % 26 + ord("A"))
        plaintext.append(plaintext_char)
    return "".join(plaintext)


def find_key(ciphertext, known_plaintext_segments):
    key_segments = [""] * len(ciphertext)

    for segment in known_plaintext_segments:
        pos, plaintext = segment
        for i, p_char in enumerate(plaintext):
            c_char = ciphertext[pos + i]
            key_char = chr((ord(c_char) - ord(p_char) + 26) % 26 + ord("A"))
            key_segments[pos + i] = key_char

    # Combine segments to form the key
    full_key = "".join(
        [char if char else "-" for char in key_segments]
    )  # Default to "-" if no key segment found
    return full_key


def caesar_decrypt(ciphertext, shift):
    decrypted_message = ""
    for char in ciphertext:
        if char.isalpha():
            shifted_char = chr(((ord(char) - ord("A") - shift) % 26) + ord("A"))
            decrypted_message += shifted_char
        else:
            decrypted_message += char
    return decrypted_message


def main():
    for shift in range(26):
        decrypted_message = caesar_decrypt(_K4, shift)
        print(f"With shift {shift}: {decrypted_message}")

    known_plaintext_segments = [
        (21, "EAST"),
        (25, "NORTHEAST"),
        (63, "BERLIN"),
        (69, "CLOCK"),
    ]

    key = find_key(_K4, known_plaintext_segments)
    print(f"Key: {key}")

    decrypted_message = vigenere_decrypt(_K4, key)
    print(f"Decrypted message: {decrypted_message}")


if __name__ == "__main__":
    main()
