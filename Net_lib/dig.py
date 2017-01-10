#!/usr/bin/env python3
# coding: utf-8
"""
Generate and parses the output of the dig command.
"""
__version__ = '0.2'

import re
import json
import sys
import argparse
import subprocess

def _get_match_groups(dig_output, regex):
    match = regex.search(dig_output)
    if not match:
        raise Exception('Invalid DIG output: ' + dig_output.rstrip())
    return match.groups()

def parse(dig_output):
    matcher = re.compile(r'((w{3}?\.?)?[\w?-]+\.(com))')
    host = _get_match_groups(dig_output, matcher)[0]

    matcher = re.compile(r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})')
    host_ip = _get_match_groups(dig_output, matcher)[0]

    matcher = re.compile(r'(\d+) msec')
    query_time= _get_match_groups(dig_output, matcher)[0]

    matcher = re.compile(r'SERVER:(\s\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})')
    server = _get_match_groups(dig_output, matcher)[0]

    return {'host': host, 'ip': host_ip, 'time': query_time, 'server': server}


def main():
    
    parser = argparse.ArgumentParser()
    parser.add_argument('host', type=str, help='host to get DNS information')
    args = parser.parse_args()

    dig_output = None
    dig_error = None
    try:
        p = subprocess.Popen(['dig', args.host], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        dig_output, dig_error = p.communicate()
    except OSError as e:
        print("OSError > ", e.errno)
        print("OSError > ", e.strerror)
        print("OSError > ", e.filename)
        dig_output = None
    except:
        dig_output = None

    if dig_output == None:
        print("Error > dig: unknown host", args.host)
        sys.exit(1)

    try:
        dig_result = parse(str(dig_output))
    except Exception as error:
        print(error)
        sys.exit(1)

    print(json.dumps(dig_result))
    sys.exit(0)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        pass
