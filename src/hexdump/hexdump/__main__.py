#!/usr/bin/env python
# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4

import string
import struct


class Pane:
    printable = string.digits + string.ascii_letters + string.punctuation + " \v\f"

    def __init__(self, buffer: bytes):
        self._buffer: bytes = buffer
        self._struct_lookup = {}

    def _chunks(self):
        """Yield successive n-sized chunks from lst."""
        for i in range(0, len(self._buffer), 16):
            yield self._buffer[i:i + 16]

    def _bytes(self, hex_row: bytes):
        struct_code = f"{len(hex_row)}c"
        struct_obj = self._struct_lookup.get(struct_code)
        if struct_obj is None:
            struct_obj = struct.Struct(f"{len(hex_row)}c")
            self._struct_lookup[struct_code] = struct_obj
        return struct_obj.unpack(hex_row)

    def __str__(self):
        ret, count = [], 0
        for hex_row in self._chunks():
            hex_values, ascii_values = [], []
            single_bytes = struct.unpack(f"{len(hex_row)}c", hex_row)
            for x, y in zip(hex_row, single_bytes):
                hex_values.append(f"{x:02x}")
                ascii_value = y.decode("ascii")
                ascii_values.append(ascii_value if ascii_value in self.printable else ".")
            hex_values, ascii_values = " ".join(hex_values), "".join(ascii_values)
            ret.append(f"{count:04}\t{ hex_values:40}\t|{ ascii_values:16}|")
            count += 10
        return "\n".join(ret)


def main():
    x = Pane(b"the quick brown fox jumped over the lazy dog")
    print(x, "\n")
    x = Pane(b"Wikipedia, the free encyclopedia that anyone can edit")
    print(x)


if __name__ == "__main__":
    main()
