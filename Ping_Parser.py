#!/usr/bin/env python3
# coding: utf-8
"""
Parses the output of the system ping command.
"""
__version__ = '0.2'

import re
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
    parser.add_argument("count", type=str, help="Ping count.")
    parser.add_argument("host", type=str, help="Ping target.")
    args = parser.parse_args()

    ping_output = None
    ping_error = None

    try:
        p = subprocess.Popen(["ping", "-c", args.count, args.host], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        ping_output, ping_error = p.communicate()
    except OSError as e:
        print("OSError > ", e.errno)
        print("OSError > ", e.strerror)
        print("OSError > ", e.filename)
        ping_output = None
    except:
        print("Error > ", sys.exc_info()[0])
        ping_output = None

    if ping_output == None:
        print(ping_error)
        sys.exit(1)

    try:
        ping_result = parse(str(ping_output))
    except Exception as error:
        sys.exit(1)

    output = " ".join([value for key, value in ping_result.items()])

    #host sent received packet_loss minping avgping maxping jitter

    print(output)
    sys.exit(0)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        pass
