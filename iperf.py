#!/usr/bin/env python3
# coding: utf-8
"""
Generate and parses the output of the iperf3 command.
"""
__version__ = '0.2'

import re
import json
import sys
import argparse
import subprocess

def _get_match_groups(iperf_output, regex):
    match = regex.search(iperf_output)
    if not match:
        raise Exception('Invalid PING output: ' + iperf_output.rstrip())
    return match.groups()

def parse(iperf_output):
    matcher = re.compile(r'PING ([a-zA-Z0-9.\-]+) *\(')
    host = _get_match_groups(iperf_output, matcher)[0]

    matcher = re.compile(r'(\d+) packets transmitted, (\d+) received, (\d+)% packet loss')
    sent, received, packet_loss = _get_match_groups(iperf_output, matcher)

    matcher = re.compile(r'(\d+.\d+)/(\d+.\d+)/(\d+.\d+)/(\d+.\d+)')
    = _get_match_groups(iperf_output, matcher)

    return {'host': host, 'sent': sent, 'received': received, 'packet_loss': packet_loss, 'jitter': jitter}


def main():
    
    parser = argparse.ArgumentParser()
    parser.add_argument('host', type=str, help='')
    parser.add_argument('port', type=int, help='')
    parser.add_argument('time', type=int, help='')
    args = parser.parse_args()

    port = str(args.port)
    time = str(args.time)
    iperf_output = None
    iperf_error = None
    command = ['iperf3', '-J', '-02', '-c', args.host, '-p', port, '-fm', '-ub', '2M', '-t', time]
    try:
        p = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        iperf_output, iperf_error = p.communicate()
    except OSError as e:
        print("OSError > ", e.errno)
        print("OSError > ", e.strerror)
        print("OSError > ", e.filename)
        iperf_output = None
    except:
        iperf_output = None

    if iperf_output == None:
        print("Error > iperf: unknown host", args.host)
        sys.exit(1)

    try:
        iperf_result = parse(str(iperf_output))
    except Exception as error:
        print(error)
        sys.exit(1)

    print(json.dumps(iperf_result))
    sys.exit(0)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        pass
