#!/usr/bin/env python3
# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4
# coding: utf-8
"""
"""

from concurrent.futures import ThreadPoolExecutor
from queue import Queue
import hashlib
import os
import json
import logging
import uuid

from miniature_octo_py.environment import CHUNK_SIZE


def split(input_file: str):
    file_stat_info = os.stat(input_file)
    logging.info("input_file: %s size: %d", input_file, file_stat_info.st_size)
    file_size = file_stat_info.st_size
    number_of_chunks = file_size % CHUNK_SIZE
    logging.info("chuck_size: %d number_of_chunks: %d", CHUNK_SIZE, number_of_chunks)
    parts_dir = make_part_dir()
    hash_queue = Queue()
    with ThreadPoolExecutor(max_workers=5) as executor:
        for seek in range(0, file_size, CHUNK_SIZE):
            executor.submit(make_chunk, input_file, parts_dir, seek, hash_queue)
        executor.shutdown(wait=True)

    parts = []
    file_hash = hashlib.sha256()
    while not hash_queue.empty():
        data = hash_queue.get()
        file_hash.update(data["hash"].encode())
        parts.append(data)
    meta_file = os.path.join(parts_dir, ".meta")
    with open(meta_file, "w") as f:
        f.write(json.dumps({"file": input_file, "hash": file_hash.hexdigest(), "parts": parts}))


def make_part_dir():
    ret = str(uuid.uuid4())
    logging.info("making parts directory: %s", ret)
    try:
        os.mkdir(ret, mode=0o700)
    except FileExistsError:
        logging.info("parts directory: %s already on file system", ret)
    return ret


def make_chunk(input_file, parts_dir, seek, hash_queue):
    logging.info("input: %s parts_dir: %s seek: %s", input_file, parts_dir, seek)
    chunk_path = os.path.join(parts_dir, "{}.part".format(uuid.uuid4()))
    logging.info("chunk_path: %s", chunk_path)
    with open(input_file, "rb") as in_, open(chunk_path, "wb") as out:
        offset = in_.seek(seek)
        logging.info("file seek to %d complete", offset)
        buffer = in_.read(CHUNK_SIZE)
        logging.info("file read complete buffer size: %d", len(buffer))
        buffer_hash = hashlib.sha256()
        buffer_hash.update(buffer)
        hash_queue.put({"chunk": chunk_path, "hash": buffer_hash.hexdigest(), "offset": seek})
        logging.info("chunk write to %s", chunk_path)
        out.write(buffer)
        logging.info("chunk write complete %s", chunk_path)
