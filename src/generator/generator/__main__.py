#!/usr/bin/env python
# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4

import argparse
from dataclasses import dataclass
import io
import struct
from typing import Optional

from generator.chaos import Lorenz


@dataclass
class PacketField:
    name: str
    data_type: str = "float"
    bit_length: int = 32 # 4 bytes
    value: Optional[float] = None


class Packet:
    def __init__(self, num_points: int):
        self.fields = [PacketField(name=f"lorenz-{i}-{x}") for i in range(num_points) for x in ["x", "y", "z"]]
        self.points = Lorenz(num_points=num_points, init_point=(0.1, 0, -0.1), step=100).get_coordinates()
        self._s_header = struct.Struct("!HHH")
        self._s_body = struct.Struct(f"!{num_points * 3}f")

    def __str__(self):
        return str(self.points)

    def read(self, data: bytes):
        version_type_header_apid, sequence_data, length = self._s_header.unpack(data[:6])
        version = (version_type_header_apid >> 8 & 0xE0) >> 5
        #print("version", version, bin(version))
        packet_type = (version_type_header_apid >> 8 & 0x10) >> 4
        #print("packet_type", packet_type, bin(packet_type))
        secondary_header = (version_type_header_apid >> 8 & 0x08) >> 3
        #print("secondary_header", secondary_header, bin(secondary_header))
        apid = version_type_header_apid & 0x07FF
        #print("apid", apid, bin(apid))
        sequence_flag = (sequence_data >> 8 & 0xC0) >> 6
        #print("sequence_flag", sequence_flag, bin(sequence_flag))
        sequence_number = sequence_data & 0x3FFF
        #print("sequence_number", sequence_number, bin(sequence_number))
        if length != len(data[6:]):
            print("warning packet length doesn't match", length, len(data[6:]))
        #print("length", length, bin(length))
        data_points = self._s_body.unpack(data[6:])
        for i, value in enumerate(data_points):
            self.fields[i].value = value
        #print("fields", self.fields)
        

    def write(self):
        five_bits = ((0x1 << 5) & 0xE0) | ((0 << 4) & 0x10) | (0 & 0x01) # (3b) packet_version, (1b) packet_type, (1b) secondary_header
        header = self._s_header.pack((five_bits << 8) | 0x1, 0x2A, len(self.fields) * 4) # (5b), (11b) apid, (2b) sequence_flag, (14b) sequence_number, (16b) packet_size 
        body = self._s_body.pack(*[x for c in self.points for x in c]) # packet_body
        return header + body


def main():
    parser = argparse.ArgumentParser(description="Make a simple ccsds packet out of a Lorenz function.")
    parser.add_argument("count", default=10, type=int, help="number of fields in the packet")
    args = parser.parse_args()

    pkt = Packet(args.count)
    print(pkt)
    result = pkt.write()
    # print(result)
    pkt.read(result)
    # print(pkt.fields)
    

if __name__ == "__main__":
    main()
