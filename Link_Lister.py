#!/usr/bin/env python3

import requests
import re

# urlName = "http://www.cs.colostate.edu/~ganvana"
urlName = "http://www.cs.colostate.edu"
website = requests.get(urlName)
html = website.text

Names = re.findall('<a\s+.*?href=["](.*?)["].*?(?:</a)>', html)
linkNames = []

for name in Names:
    print(name)
    tempList = re.findall('>(.*?)</a>', name)
    print(tempList)
    if len(tempList) > 0:
        print(tempList[0])
        linkNames.append(tempList[0])

links = re.findall('"((http|ftp)s?://.*?)"', html)

fmt = '{:<4}{:<25}{}'
print(fmt.format('', 'Link Name', 'Link'))
for i, (name, link) in enumerate(zip(linkNames, links)):
    print(fmt.format(i, name, link))
