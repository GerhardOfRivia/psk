#!/usr/bin/env python3
# coding: utf-8
"""
Generate and parses the output of the system ping command.
"""
__version__ = '0.2'

import re
import json
import sys
import argparse
import subprocess

def _get_match_groups(ping_output, regex):
    match = regex.search(ping_output)
    if not match:
        raise Exception('Invalid PING output: ' + ping_output.rstrip())
    return match.groups()

def parse(ping_output):
    matcher = re.compile(r'PING ([a-zA-Z0-9.\-]+) *\(')
    host = _get_match_groups(ping_output, matcher)[0]

    matcher = re.compile(r'(\d+) packets transmitted, (\d+) received, (\d+)% packet loss')
    sent, received, packet_loss = _get_match_groups(ping_output, matcher)

    matcher = re.compile(r'(\d+.\d+)/(\d+.\d+)/(\d+.\d+)/(\d+.\d+)')
    minping, avgping, maxping, jitter = _get_match_groups(ping_output, matcher)

    return {'host': host, 'sent': sent, 'received': received, 'packet_loss': packet_loss,
            'minping': minping, 'avgping': avgping, 'maxping': maxping,
            'jitter': jitter}


def main():
    
    parser = argparse.ArgumentParser()
    parser.add_argument("count", type=int, help="Stop after sending number ECHO_REQUEST packets.")
    parser.add_argument("host", type=str, help="Send ICMP ECHO_REQUEST to network destination.")
    args = parser.parse_args()

    ping_count = str(args.count)
    ping_output = None
    ping_error = None

    try:
        p = subprocess.Popen(["ping", "-c", ping_count, args.host], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        ping_output, ping_error = p.communicate()
    except OSError as e:
        print("OSError > ", e.errno)
        print("OSError > ", e.strerror)
        print("OSError > ", e.filename)
        ping_output = None
    except:
        ping_output = None

    if ping_output == None:
        print("Error > ping: unknown host", args.host)
        sys.exit(1)

    try:
        ping_result = parse(str(ping_output))
    except Exception as error:
        sys.exit(1)

    print(json.dumps(ping_result))
    sys.exit(0)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        pass
