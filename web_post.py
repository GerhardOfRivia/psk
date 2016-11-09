#!/usr/bin/env python3

import argparse
import urllib.request
import urllib.parse
import json


parser = argparse.ArgumentParser()
parser.add_argument("name", type=str, help="name of current device.")
parser.add_argument("target", type=str, help="name of away device.")
parser.add_argument("filename", type=str, help="name of json iperf ouput.")
args = parser.parse_args()


with open(args.filename) as data_file:    
    data = json.load(data_file)

text = json.dumps(data, indexnt=4)

data = urllib.parse.urlencode({'name': args.name, 'from': args.target , 'info': text})
data = data.encode('utf-8')
request = urllib.request.Request("http://antdash.colostate.edu/lib/make_data.php")

# adding charset parameter to the Content-Type header.
request.add_header("Content-Type","application/x-www-form-urlencoded;charset=utf-8")

f = urllib.request.urlopen(request, data)
print(f.read().decode('utf-8'))
