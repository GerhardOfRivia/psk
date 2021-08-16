#!/usr/bin/env python3
# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4
# coding: utf-8
"""
"""

import os

_chunk_size = "GFS_CHUNK_SIZE"

try:
    CHUNK_SIZE = int(os.getenv(_chunk_size, "10000"))
except ValueError:
    CHUNK_SIZE = 10000
