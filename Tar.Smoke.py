#!/usr/bin/python3
#This will configure the Targets file for smokeping
import subprocess
import sys
import os.path
nameservers = []
index = 0
#Get routing table for default gateway and parse it
try:
    route_output = subprocess.check_output(["route", "-n"]).splitlines()
    for line in route_output:
        fields = line.strip().split()
        if fields[0].decode('ascii') == "0.0.0.0":
            gateway = (fields[1].decode('ascii'))
            break
except:
    print ("No route command runnable from path")
    print (sys.exc_info()[0])
    sys.exit()

route_list = gateway.split('.')
subnet = ""
for i in range(0, 3):
    subnet += "{}.".format(route_list[i])

#Print Targets File Data

print ("*** Targets ***\n\nprobe=FPing\n")
print ("menu = Top\ntitle = Network Latency Grapher\nremark =\n")
print ("+ ICMP\nmenu = ICMP\ntitle = ICMP\n")
print ("++ gateway_One\ntitle = Gateway_One\nhost = {}\nalerts = red,amber,green\n".format(gateway))
print ("++ gateway_Two\ntitle = Gateway_Two\nhost = {}2\n".format(subnet))
print ("++ gateway_Three\ntitle = Gateway_Three\nhost = {}3\n".format(subnet))
print ("++ nexus_Two\ntitle = Nexus_Two_Loopback\nhost = 129.82.0.4\n")
print ("++ nexus_Three\ntitle = Nexus_Three_Loopback\nhost = 129.82.0.5\n")
print ("++ colostate\ntitle = colostate\nhost = www.colostate.edu\n")
print ("++ frgp\ntitle = FRGP\nhost = www.frgp.net\n")
print ("++ google\ntitle = Google\nhost = www.google.com\n")

#This is where we get DNS
try:
    resolv=open("/etc/resolv.conf",'r')
except:
    print ("File /etc/resolv.conf be opened")
    print (sys.exc_info()[0])
    sys.exit()
for line in resolv:
    if line.startswith("nameserver"):
        index += 1
        nameservers = line.strip().split()
        #Print the DNS servers
        for i in range(1,len(nameservers)):
            print ("++ DHCP_DNS_{}\ntitle = DHCP_DNS_{}\nhost = {}\n".format(index,nameservers[1],nameservers[1]))

print ("+ DNS\nmenu = DNS\nprobe = DNS\ntitle = DNS request to DNS Servers\n")
index=0
try:
    resolv=open("/etc/resolv.conf",'r')
except:
    print ("File /etc/resolv.conf be opened")
    print (sys.exc_info()[0])
    sys.exit()
for line in resolv:
    if line.startswith("nameserver"):
        index+=1
        nameservers = line.strip().split()
        #Print the DNS servers
        for i in range(1,len(nameservers)):
            print ("++ DNS_{}\ntitle = DNS_{}\nmenu = DNS_{}\nhost = {}\n".format(index,nameservers[1],index,nameservers[1]))

#Print The Http Requests
print ("+ HTTP_Request\nmenu = HTTP_Request\ntitle = HTTP_Request (Ping)\n")
print ("++ HTTP_Colostate\ntitle = Colostate\nmenu = Colostate\nprobe = EchoPingHttp\nhost = www.colostate.edu\nport = 80\nurl = /_support/images/logo-ram.png \n")
print ("++ HTTP_FRGP\ntitle = FRGP_HTTP\nmenu = RFRGP\nprobe = EchoPingHttp\nhost = www.frgp.net\nport = 80\nurl = /index\n")
print ("++ HTTP_Google\ntitle = Google_HTTP\nmenu = Google\nprobe = EchoPingHttp\nhost = www.google.com\nport = 80\nurl = /\n")
