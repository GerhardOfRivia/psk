#!/usr/bin/env python3
#This will configure the Targets file for smokeping
import subprocess
import sys
import os.path
nameservers = []
index = 0
#Get routing table
 for default gateway and parse it
try:
    route_output=subprocess.check_output(["route", "-n"]).splitlines()
    for line in route_output:
        fields = line.strip().split()
        if fields[0].decode('ascii')=="0.0.0.0":
            gateway=(fields[1].decode('ascii'))
            break
except:
    print ("No route command runnable from path")
    print (sys.exc_info()[0])
    sys.exit()

#Print Targets File Data
print ("*** Targets ***\n\nprobe = FPing\n")
print ("menu = Top\ntitle = Network Latency Grapher\nremark =\n")
print ("+ Local_Network\nmenu = Local Area Network\ntitle = LAN\n")
print ("++ Public_Wireless\nmenu = Public Wireless\nhost = %s\nalerts = red,amber,green\n" % gateway)
print ("+ DNS\nmenu = DNS\ntitle = ICMP echo to DNS Servers\n")
print ("++ GETDNS\ntitle = Google public DNS\nmenu = Google public DNS\nprobe = EchoPingDNS\ndns_request = www.google.com\nhost = 8.8.8.8\n")
print ("++ Google_DNS\nmenu = DNS\nhost = 8.8.8.8\n")
#This is where we get DNS
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
            print ("++ Local_DNS_{}\ntitle = Local_DNS_{}\nhost = {}\n".format(index,nameservers[1],nameservers[1]))
#Go back to printing rest of file
print ("+ Internet\nmenu = Internet\ntitle = Internet Access (Ping)\n")
print ("++ Google\ntitle = Google\nhost = www.google.com\n")
print ("++ HTTP_Google\ntitle = Google_Pic\nmenu = Google\nprobe = EchoPingHttp\nhost = www.google.com\nport = 80\nurl = /images/srpr/logo11w.png\n")
print ("++ Colostate\ntitle = Colostate\nhost = www.colostate.edu\n")
