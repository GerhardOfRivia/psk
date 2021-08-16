#!/usr/bin/env python3
# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4
# coding: utf-8
"""
"""

import argparse
import logging

from miniature_octo_py.split import split
from miniature_octo_py.join import join

logging.basicConfig(format='%(asctime)s %(message)s', level=logging.INFO)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('target', type=str, help='file or directory to split or join')
    parser.add_argument('action', choices=['split', 'join'])
    args = parser.parse_args()

    if args.action == 'split':
        split(args.target)
    else:
        join(args.target)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        pass
    except Exception as err:
        logging.exception(err)
