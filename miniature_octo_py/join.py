#!/usr/bin/env python3
# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4
# coding: utf-8
"""
"""

from concurrent.futures import ThreadPoolExecutor
from threading import RLock
import os
import sys
import json
import logging


def join(input_directory: str):
    meta_file = validate_input(input_directory)
    with open(meta_file, "r") as m:
        meta = json.loads(m.read())
    logging.info("number of parts listed: %d", len(meta["parts"]))
    output_file = open("join_test", "wb")
    write_lock = RLock()
    with ThreadPoolExecutor(max_workers=5) as executor:
        parts = sorted(meta["parts"], key=lambda p: p["offset"])
        for part in parts:
            chunk_path = os.path.join(input_directory, part["chunk"])
            executor.submit(make_chunk, chunk_path, part["offset"], write_lock, output_file)
    output_file.close()


def validate_input(input_directory: str):
    is_dir = os.path.isdir(input_directory)
    logging.info("input_directory: %s is_dir: %s", input_directory, is_dir)
    if is_dir is False:
        logging.error("target must be directory, exiting.")
        sys.exit(1)
    meta_file = os.path.join(input_directory, ".meta")
    is_meta = os.path.isfile(meta_file)
    if is_meta is False:
        logging.error("target must contain meta file, exiting.")
        sys.exit(1)
    return meta_file


def make_chunk(chunk_path, offset, write_lock, output_file):
    # TODO figure out how to write file in order of offset
    pass
