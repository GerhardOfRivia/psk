#!/usr/bin/env python3
# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4
# coding: utf-8
"""
"""

import hashlib
import json
import logging
import os
import sys
from queue import Queue


class JoinMachinist:
    def __init__(self, input_directory: str):
        meta_file = self._validate_input(input_directory)
        with open(meta_file, "r") as m:
            meta = json.loads(m.read())
        logging.info("number of parts listed: %d", len(meta["parts"]))
        hash_queue = Queue()
        output_file = open("join_{}".format(meta["file"]), "wb")
        parts = sorted(meta["parts"], key=lambda p: p["offset"])
        for part in parts:
            self._make_chunk(part["chunk"], output_file, part["hash"], hash_queue)
        output_file.close()

        file_hash = hashlib.sha256()
        while not hash_queue.empty():
            file_hash.update(hash_queue.get().encode())
        join_file_hash = file_hash.hexdigest()
        assert join_file_hash == meta["hash"], "file hash must match, something is wrong here"

    @staticmethod
    def _validate_input(input_directory: str):
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

    @staticmethod
    def _make_chunk(chunk_path, output_file, split_check_sum, hash_queue):
        with open(chunk_path, "rb") as in_:
            buffer = in_.read()
            logging.info("file read complete buffer size: %d", len(buffer))
            buffer_hash = hashlib.sha256()
            buffer_hash.update(buffer)
            join_check_sum = buffer_hash.hexdigest()
            assert split_check_sum == join_check_sum, "hash is not equal, something is not right here."
            hash_queue.put(join_check_sum)
            logging.info("check sum complete, chunk write to output file")
            output_file.write(buffer)
            logging.info("chunk read complete, %s", chunk_path)
