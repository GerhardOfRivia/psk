#!/usr/bin/env python

import argparse
import json
import subprocess as sub
import sys

from iwconfig import IwConfig
from ifconfig import IfConfig

def get_network_info(interface):
    for line in open('/proc/net/dev', 'r'):
        if interface in line.split(':')[0]:
            return True
    return False

parser = argparse.ArgumentParser()
parser.add_argument("interface", type=str, help="wireless interface to get information of.")
parser.add_argument("-c", "--check", action="store_true", help="Check if interface exists.")
args = parser.parse_args()

if args.check:
    if not get_network_info(args.interface):
        print("Interface not found.\n")
        sys.exit(1)

output = "["

ifconfig_output = ""
ifconfig_errors = ""
ifconfig_result = True

try:
    p = sub.Popen(["ifconfig", args.interface], stdout=sub.PIPE, stderr=sub.PIPE)
    ifconfig_output, ifconfig_errors = p.communicate()
except OSError as e:
    print("OSError > ",e.errno)
    print("OSError > ",e.strerror)
    print("OSError > ",e.filename)
    ifconfig_result = False
except:
    print("Error > ",sys.exc_info()[0])
    ifconfig_result = False

# if got error print message and exit
if not ifconfig_output and ifconfig_errors:
    print(ifconfig_errors)
    sys.exit(1)

if ifconfig_result:
    ifconfig_output = ifconfig_output.decode()
    IfObj = IfConfig(ifconfig_output.strip())
    output += IfObj.to_json(indent=4) + ", "

iwconfig_output = ""
iwconfig_errors = ""
iwconfig_result = True

try:
    p = sub.Popen(["iwconfig", args.interface], stdout=sub.PIPE, stderr=sub.PIPE)
    iwconfig_output, iwconfig_errors = p.communicate()
except OSError as e:
    print("OSError > ",e.errno)
    print("OSError > ",e.strerror)
    print("OSError > ",e.filename)
    iwconfig_result = False
except:
    print("Error > ",sys.exc_info()[0])
    iwconfig_result = False

# if got error print message and exit
if not iwconfig_output and iwconfig_errors:
    print(iwconfig_errors)
    sys.exit(1)

if iwconfig_result:
    iwconfig_output = iwconfig_output.decode()
    IwObj = IwConfig(iwconfig_output.strip())
    output += IwObj.to_json(indent=4) + " ]"
