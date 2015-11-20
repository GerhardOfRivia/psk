#!/usr/bin/env python3


## Take Arguments from CLI ##
## End of Take Arguments from CLI ##


## Start of Imports ##
import sys
import os
import time
import getopt
import re
import ipaddress
## End of Imports ##


## Define Variables ##
endr = "129.82.0.4"
sub_dir="/home/local/rancid/var/rancid/core/configs"
dren = "129.82.0.5"
## End of Define Variables ##


## Start of Classes ##
class ACL:
    def __init__(self,name,type):
        self.name = name
        self.ACL = []
        self.type = type

    def addACLTerm(self, x):
        self.ACL.append(x)

    def printACL(self):
        print("ip access-list {}".format(self.name))
        for line in self.ACL:
            print(line)

    def aclEqual(self, acl):
        return self.ACL == acl.ACL

    def typeEqual(self, acl):
        return self.type == acl.type

    def printMismatch(self, acl, router1, router2):
         i = 0
         aclSize = len(acl.ACL)
         selfSize = len(self.ACL)
         print("ACL Sizes - {}:{} - {}:{}".format(router1, router2, str(selfSize), str(aclSize)))

         while selfSize > i and aclSize > i:
             if self.ACL[i] != acl.ACL[i]:
                 sys.stdout.write(router1 + " " + self.ACL[i])
                 sys.stdout.write(router2 + " " + acl.ACL[i])
                 print("-----")
             i = i+1

class SVI:
    def __init__(self,name):
        self.name = name
        self.SVI = []
        self.shutdown = None
        self.description = None
        self.dhcpRelay = []
        self.hsrpPriority = None
        self.hsrpInstance = None
        self.pim = None
        self.OSPF = None
        self.IP = None
        self.RouteMap = None
        self.Gateway = None
        self.proxy = None

    def addSVIList(self, x):
        self.SVI.append(x)

    def printAll(self):
        for x in self.SVI:
            print(x)


#    def getName(self):
#        return self.name
#
    def setName(self, x):
        self.name = x
#
#    def getGateway(self):
#        return self.Gateway
#
    def setGateway(self, x):
        self.Gateway = x
#
#    def getRouteMap(self):
#        return self.RouteMap
#
    def setRouteMap(self, x):
        self.RouteMap = x
#
#    def getIP(self):
#        return self.IP
#
    def setIP(self, x):
        self.IP = x
#
#    def getOSPF(self):
#        return self.OSPF
#
    def setOSPF(self, x):
        self.OSPF = x
#
#    def getPim(self):
#        return self.pim
#
    def setPim(self, x):
        self.pim = x
#
#    def getHSRPInstance(self):
#        return self.hsrpInstance
#
    def setHSRPInstance(self, x):
        self.hsrpInstance = x
#
#    def getHSRPPriority(self):
#        return self.hsrpPriority
#
    def setHSRPPriority(self, x):
        self.hsrpPriority = x
#
#    def getShutdown(self):
#        return self.shutdown
#
    def setShutdown(self, x):
        self.shutdown = x
#
#    def getDescription(self):
#        return self.description
#
    def setDescription(self, x):
        self.description = x
#
    def addRelay(self, x):
        self.dhcpRelay.append(x)
#
#    def getRelay(self):
#        return self.dhcpRelay

    def printMismatch(self, svi):
        return self.sviEqual(svi, "1")

    def sviEqual(self, svi, show="0"):
        returnValue = 1
        if self.name != svi.name:
            returnValue = 0
            if show == "1":
                print("Name Mismatch for : " + self.name)

        if self.shutdown != svi.shutdown:
            returnValue = 0
            if show == "1":
                print("Shutdown Mismatch for: " + self.name)


        if self.proxy != svi.proxy:
            returnValue = 0
            if show == "1":
                print("IP Proxy-Arp mismatch for "+ self.name)

        if self.description != svi.description:
            returnValue = 0
            if show == "1":
                print("Description Mismatch for: " + self.name)

        if self.dhcpRelay != svi.dhcpRelay:
            returnValue = 0
            if show == "1":
                print("DHCP Relay Mismatch for: " + self.name)

#        self.hsrpPriority = None
#        if self.hsrpPriority != svi.hsrpPriority:
#            returnValue = 0
#            if show == "1":
#                print("hsrpPriority Mismatch for: " + self.name)

        if self.hsrpInstance != svi.hsrpInstance:
            returnValue = 0
            if show == "1":
                print("HSRP Instance Mismatch for: " + self.name)

        if self.pim != svi.pim:
            returnValue = 0
            if show == "1":
                print("Pim Mismatch for: " + self.name)

        if self.OSPF != svi.OSPF:
            returnValue = 0
            if show == "1":
                print("OSPF Mismatch for: " + self.name)

#        self.IP = None
#        if self.IP != svi.IP:
#            returnValue = 0
#            if show == "1":
#                print("IP Mismatch for: " + self.name)

        if self.RouteMap != svi.RouteMap:
            returnValue = 0
            if show == "1":
                print("RouteMap Mismatch for: " + self.name)

        if self.Gateway != svi.Gateway:
            returnValue = 0
            if show == "1":
                print("Gateway Mismatch for: " + self.name)


        return returnValue
## End of Classes ##


## Start of Fucntions ##
def ping(hostname):
   response = os.system("ping -c 3 " + hostname)
   if response == 0:
      print (hostname, 'is up!')
   else:
     print (hostname, 'is down!')


def buildListOfACLs(list, router):
    with open(os.path.join(sub_dir, router), "r") as f:
        for line in f:
            if "ip access-list" in line or "object-group ip" in line or re.search(regexp, line) is not None:
                if "ip access-list" in line:
                    wordsInLine = line.split()
                    thisACL = ACL(wordsInLine[2], "ip access-list")
                    list.append(thisACL)

                elif "object-group ip" in line:
                    wordsInLine = line.split()
                    thisACL = ACL(wordsInLine[3], "object-group ip")
                    list.append(thisACL)

                else:
                    list[len(list)-1].addACLTerm(line)


def findPosByName(ACLList, x):
    returnValue = None
    i = -1
    for acl in ACLList:
        i = i+1
        if acl.name == x:
            return i
        else:
            returnValue = None
    return returnValue

def nullTestCase():
    #Do nothing; null case
    #Also re-used if needed for a line that has no effect
    return ""

def endrOnlyACL(endrList, drenList):
    for endrACL in endrList:
        if findPosByName(drenList, endrACL.name) is None:
            print(endrACL.name + " - is endr exclusive ACL")

def drenOnlyACL(drenList, endrList):
    for drenACL in drenList:
        if findPosByName(endrList, drenACL.name) is None:
            print(drenACL.name + " - is dren exclusive ACL")

def aclMismatch(endrList, drenList):
    for ACL in endrList:
        i = -1
        i = findPosByName(drenList, ACL.name)
        if i is not None:
            if ACL.aclEqual(drenList[i]) and i > -1:
                 nullTestCase()
            else:
                print("")
                print("ACL: " + ACL.name + " has a content mismatch with its counterpart")
                ACL.printMismatch(drenList[i],"ENDR","DREN")

    for ACL in drenList:
        i = -1
        i = findPosByName(endrList, ACL.name)
        if i is not None:
            if ACL.aclEqual(endrList[i]) and i > -1:
                 nullTestCase()
            else:
                print("")
                print("ACL: " + ACL.name + " has a content mismatch with its counterpart")
                ACL.printMismatch(endrList[i],"DREN","ENDR")

def typeMismatch(endrList, drenList):
    for ACL in endrList:
        i = -1
        i = findPosByName(drenList, ACL.name)
        if i is not None:
            if ACL.typeEqual(drenList[i]) and i > -1:
                 nullTestCase()
            else:
                print("")
                print("ACL: " + ACL.name + " has a type mismatch with it's counterpart")

    for ACL in drenList:
        i = -1
        i = findPosByName(endrList, ACL.name)
        if i is not None:
            if ACL.typeEqual(endrList[i]) and i > -1:
                 nullTestCase()
            else:
                print("")
                print("ACL: " + ACL.name + " has a type mismatch with it's counterpart")

def buildACLApplied(list, router):
    with open(os.path.join(sub_dir, router), "r") as f:
        for line in f:
            if "portgroup" in line or "addrgroup" in line or "access-group" in line or "match ip address" in line:
                list.append(line)

def appCompare(list1, list2, list1name, list2name):
    for x in list1:
        count = 0
        for y in list2:
            if x == y:
                count = count + 1
        if count == 0:
            print (list1name + " only acl application: " + x)

    for x in list2:
        count = 0
        for y in list1:
            if x == y:
                count = count + 1
        if count == 0:
            print (list2name + " only acl application: " + x)

def aclDefinedNotApplied(listACL, listApp, router):
    for x in listACL:
        if "route-map" in x.name:
            print(x)
        count = 0
        for y in listApp:
            if x.name in y:
                count = count + 1
        if count == 0:
            print (router + ": does not apply acl: " + x.name)

def aclAppliedNotDefined(listACL, listApp, router):
    searchFor = []
    for y in listApp:
        if "addrgroup" in y or "portgroup" in y:
            aclname = y.split()
            cnt = 0
            for z in aclname:
                if "addrgroup" in z or "portgroup" in z:
                    searchFor.append(aclname[cnt+1])
                cnt = cnt + 1
        elif "access-group" in y:
            aclname = y.split()
            searchFor.append(aclname[2])
        elif "ip policy route-map" in y:
            aclname = y.split()
            searchFor.append(aclname[2])


    #list(set()) elminates duplicate enteries
    searchFor = list(set(searchFor))
    for aclname in searchFor:
        count = 0
        for x in listACL:
            if x.name == aclname:
                count = count + 1
        if count == 0:
            print (router + ": has applied but not defined acl " + aclname)

def buildSVIArray(listSVI, router):
    with open(os.path.join(sub_dir, router), "r") as f:
        data = f.read()
    fileContents = data.splitlines()
    i = 0
    while i < len(fileContents):
        if re.search(regexpVlan, fileContents[i]) is not None:
            words = fileContents[i].split()
            newSVI = SVI(words[1])

            while fileContents[i] is not "":
                newSVI.addSVIList(fileContents[i])
                i = i + 1
            listSVI.append(newSVI)
        i = i + 1

    for thisSVI in listSVI:
        for line in thisSVI.SVI:
            if "ip address" in line and not "secondary" in line:
                splitLine = line.split()
                thisSVI.setIP(splitLine[2])
#                print(thisSVI.getIP())

            elif "pim sparse" in line:
                splitLine = line.split()
                thisSVI.setPim(splitLine[2])
#                print(thisSVI.getPim())

            elif "route-map" in line:
                splitLine = line.split()
                thisSVI.setRouteMap(splitLine[3])
#                print(thisSVI.getRouteMap())

            elif "hsrp" in line and not "hsrp version 2" in line:
                splitLine = line.split()
                thisSVI.setHSRPInstance(splitLine[1])
#                print(thisSVI.getHSRPInstance())

            elif "priority" in line:
                splitLine = line.split()
                thisSVI.setHSRPPriority(splitLine[1])
#                print(thisSVI.getHSRPPriority())

            elif re.search(regexpGateway, line) is not None and not "secondary" in line:
                splitLine = line.split()
                thisSVI.setGateway(splitLine[1])
#                print(thisSVI.getGateway())

            elif "ip dhcp relay" in line:
                splitLine = line.split()
                thisSVI.addRelay(splitLine[4])
#                print(thisSVI.getRelay())

            elif "description" in line:
                splitline = line.split()
                thisSVI.setDescription(splitLine[1])
#                print(thisSVI.getDescription())

            elif "shutdown" in line:
                thisSVI.setShutdown(line)
#                print(thisSVI.getShutdown())

            elif "ip router ospf" in line:
                thisSVI.setOSPF(line)
#                print(thisSVI.getOSPF())

            elif "ip proxy-arp" in line:
                thisSVI.proxy = line
#                print(thisSVI.proxy)

def routerOnlySVI(routerOneSVI,routerTwoSVI, router):
    for SVIone in routerOneSVI:
        if findPosByName(routerTwoSVI, SVIone.name) is None:
            print(SVIone.name + " is " + router + " exclusive")

def sviMismatch(endrList, drenList):
    for SVI in endrList:
        i = -1
        i = findPosByName(drenList, SVI.name)
        if i is not None:
            if SVI.sviEqual(drenList[i]) and i > -1:
                 nullTestCase()
            else:
                print("")
                SVI.printMismatch(drenList[i])

    for SVI in drenList:
        i = -1
        i = findPosByName(endrList, SVI.name)
        if i is not None:
            if SVI.sviEqual(endrList[i]) and i > -1:
                 nullTestCase()
            else:
                print("")
                SVI.printMismatch(endrList[i])


def sviMissing(List,router):
    for svi in List:
        if svi.shutdown == None:
            print(router + ": shutdown not defined for: " + svi.name)
        if svi.description == None:
            print(router + ": description not defined for: " + svi.name)
        if svi.dhcpRelay == None:
            print(router + ": dhcpRelay not defined for: " + svi.name)
        if svi.hsrpPriority == None:
            print(router + ": hsrpPriority not defined for: " + svi.name)
        if svi.hsrpInstance == None:
            print(router + ": hsrpInstance not defined for: " + svi.name)
        if svi.pim == None:
            print(router + ": pim not defined for: " + svi.name)
        if svi.OSPF == None:
            print(router + ": OSPF not defined for: " + svi.name)
        if svi.IP == None:
            print(router + ": IP not defined for: " + svi.name)
        if svi.proxy == None:
            print(router + ": IP Proxy Arp not defined for: " + svi.name)
#        if svi.RouteMap == None:
#            print(router + ": routeMap not defined for: " + svi.name)
        if svi.Gateway == None:
            print(router + ": Gateway not defined for: " + svi.name)


def endrSpecificChecks(endrSVI):
    for svi in endrSVI:
        if svi.IP != None and svi.Gateway != None:
            splitLine = svi.IP.split('/')
            a = ipaddress.IPv4Address(splitLine[0]) - 1
            if a != ipaddress.IPv4Address(svi.Gateway):
                print("ENDR IP is not one after gateway for: " + svi.name)
        if svi.hsrpPriority != "250":
            print("HSRP Priority is " + str(svi.hsrpPriority) + " and not 250 for: " + svi.name)


def drenSpecificChecks(drenSVI):
    for svi in drenSVI:
        if svi.IP != None and svi.Gateway != None:
            splitLine = svi.IP.split('/')
            a = ipaddress.IPv4Address(splitLine[0]) - 2
            if a != ipaddress.IPv4Address(svi.Gateway):
                print("DREN IP is not two after gateway for: " + svi.name)
                svi.printAll()
        if svi.hsrpPriority != "110":
            print("HSRP Priority is " + str(svi.hsrpPriority) + " and not 110 for: " + svi.name)

def gatewayValidate(routerSVI, offset):
    for svi in routerSVI:
        if svi.IP != None and svi.Gateway != None:
            splitLine = (svi.IP).split('/')
            a = ipaddress.IPv4Address(splitLine[0])
            b = ipaddress.ip_network(svi.IP,0)
            if (a - offset) != list(b.hosts())[0]:
                print("Gateway is not correct for: " + svi.name)

def verifyRouteMap(listSVI):
    for svi in listSVI:
        if svi.description is not None:
            if svi.RouteMap is None and "Private" in svi.description:
                print("RouteMap not defined for " + svi.name)

def replaceSVI(listSVI, newSVI):
    #Verify SVI exists
    i = findPosByName(listSVI, newSVI.name)
    if i is not None:
        if int(i) > -1:
            listSVI[i] = newSVI



## End of Functions ##


## Start of Main ##
print("Python Version:")
print(sys.version)


## Verify Systems are Online
#ping(endr)
#ping(dren)

## Open RANCID Files and grab approriate lines
regexp = re.compile(r'  \d[\d]* permit|  \b\d[\d]* remark|  \b\d[\d]* deny')
regexpVlan = re.compile(r'interface Vlan[\d]*')
regexpGateway = re.compile(r'    ip \d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$')
endrList = []
drenList = []
buildListOfACLs(endrList, endr)
buildListOfACLs(drenList, dren)

endrApp = []
drenApp = []
buildACLApplied(endrApp, endr)
buildACLApplied(drenApp, dren)

#for x in endrApp:
#    print (x)

endrSVI = []
drenSVI = []
buildSVIArray(endrSVI,endr)
buildSVIArray(drenSVI,dren)

## This is a bogus SVI so can ignore Vlan1 ##
## Does not scale nicely ##
bogusSVIe = SVI("Vlan1")
bogusSVIe.IP = "192.168.0.2/24"
bogusSVIe.setPim("pim sparse")
bogusSVIe.hsrpInstance = "1"
bogusSVIe.hsrpPriority = "250"
bogusSVIe.setGateway("192.168.0.1")
bogusSVIe.OSPF = "0.0.0.0"
bogusSVIe.dhcpRelay = "129.82.100.81"
bogusSVIe.description = "Vlan 1"
bogusSVIe.shutdown = "no shutdown"
bogusSVIe.proxy = "ip proxy-arp"

bogusSVId = SVI("Vlan1")
bogusSVId.IP = "192.168.0.3/24"
bogusSVId.setPim("pim sparse")
bogusSVId.hsrpInstance = "1"
bogusSVId.hsrpPriority = "110"
bogusSVId.setGateway("192.168.0.1")
bogusSVId.OSPF = "0.0.0.0"
bogusSVId.dhcpRelay = "129.82.100.81"
bogusSVId.description = "Vlan 1"
bogusSVId.shutdown = "no shutdown"
bogusSVId.proxy = "ip proxy-arp"

replaceSVI(endrSVI,bogusSVIe)
replaceSVI(drenSVI,bogusSVId)

## End of Does not scale nicely ##

        ###For each ACL listing check for the below cases
#* No ACL for ENDR and DREN(Acceptable) - null case
nullTestCase()
print("")
print("")


#* ACL for ENDR and no ACL for DREN(Flag)
print("Searching for ENDR only ACLs...")
endrOnlyACL(endrList, drenList)
print("")
print("")


#* No ACL for ENDR and ACL for DREN(Flag)
print("Searching for DREN only ACLs...")
drenOnlyACL(drenList, endrList)
print("")
print("")


#* ACL on ENDR does not match dren(Flag)
print("Searching for ACL content mis-match...")
aclMismatch(endrList,drenList)
print("")
print("")


#* ACL on ENDR Matches DREN(Acceptable) - normal case
#print("")
#print("")


#* ACL Name mismatch(spelling) between ENDR/DREN(Flag)
#Note: This is not needed because router-specific ACLs will catch this


#* ACL Number mismatch between ENDR/DREN(Flag)
#Note - This is not possible because ACLs are not listed by number but by name.


#* ACL Type mismatch between ENDR/DREN(Flag)
print("Searching for ACL type mismatch(ip access list / object-group)...")
typeMismatch(endrList,drenList)
print("")
print("")


#* ACL applied mismatch between ENDR/DREN(FLAG)
print("Searching for ACL application mismatch...")
appCompare(endrApp,drenApp,"ENDR","DREN")
print("")
print("")


#* ACL Defined but not applied(Flag)
print("Searching for ACL defined but not applied...")
#aclDefinedNotApplied(endrList, endrApp, "ENDR")  #Restore after 12/31/2015
#aclDefinedNotApplied(drenList, drenApp, "DREN")  #Restore after 12/31/2015
print("")
print("")


#* ACL Applied but not defined(Flag)
print("Searching for ACL applied but not defined...")
aclAppliedNotDefined(endrList, endrApp, "ENDR")
aclAppliedNotDefined(drenList, drenApp, "DREN")
print("")
print("")


#Build an array of SVI Objects
#Verify Parity between ENDR and DREN SVI Objects for each object
print("Searching for ENDR only SVIs...")
routerOnlySVI(endrSVI,drenSVI, "ENDR")
print("")
print("")

print("Searching for DREN only SVIs...")
routerOnlySVI(drenSVI,endrSVI, "DREN")
print("")
print("")


print("Searching for SVI Content Mismatch...")
sviMismatch(endrSVI,drenSVI)
print("")
print("")

print("Searching for SVI Content Missing...")
sviMissing(endrSVI,"ENDR")
sviMissing(drenSVI,"DREN")
print("")
print("")


#Verify ENDR specific values are correct
print("Verifying ENDR specific values are set...")
endrSpecificChecks(endrSVI)
print("")
print("")

#Verify DREN Specific Values are correct
print("Verifying DREN specific values are set...")
drenSpecificChecks(drenSVI)
print("")
print("")

#Verify Gateway value matches expected value
print("Verifying Gateway is the first address in the network...")
gatewayValidate(endrSVI,1)
gatewayValidate(drenSVI,2)
print("")
print("")


#Verify Policy Route-map for Private(but not utility)
print("Verifying Private Networks have a RouteMap...")
verifyRouteMap(endrSVI)
print("")
print("")


## End of Main ##
