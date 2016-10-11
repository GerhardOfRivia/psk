#!/usr/bin/env python3

import requests
import re

urlName = "http://www.cs.colostate.edu/~ganvana"
website = requests.get(urlName)
html = website.text
links = re.findall('"((http|ftp)s?://.*?)"', html)
for link in links:
    print(link[0])
