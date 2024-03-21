#!/usr/bin/env python
# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4

import ccsdspy
import io
import struct

from generator.chaos import Lorenz


def read(num_points: int, pkt: io.BytesIO):
    fields = [ccsdspy.PacketField(name=f"lorenz-{i}-{x}", data_type="float", bit_length=32) for i in range(num_points) for x in ["x", "y", "z"]]
    pkt = ccsdspy.FixedLength(fields)
    return pkt.load(pkt, include_primary_header=True)


def write(num_points: int):
    five_bits = ((0x1 << 5) & 0xE0) | ((0 << 4) & 0x10) | (0 & 0x01) # packet_version packet_type secondary_header
    header = struct.pack("!HHH", (five_bits << 10) | 0x1, 0x2A, num_points * 3)
    points = Lorenz(num_points=num_points, init_point=(0.1, 0, -0.1), step=100).get_coordinates()
    body = struct.pack(f"!{num_points * 3}f", *[i for g in points for i in g])
    return io.BytesIO(header + body)


def main():
    pkt = write(10)
    print(pkt)
    result = read(10, pkt)
    

if __name__ == "__main__":
    main()
