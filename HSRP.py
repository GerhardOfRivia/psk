#!bin/python3

#Hot Standby Router Protocol
#http://tools.ietf.org/html/rfc2281

class Interface:
  def __init__(self, vlan, ip):
    self.vlan = vlan
    self.ip = ip

  def __str__(self):
    return self.vlan+" "+self.ip

  def read(file_name):
    with open(file_name, "r") as f:
      interfaces = []
      while True:
        line = f.readline()
        if not line:
          break

        if line.startswith("interface"):
          interface = line.strip().split()
          while True:
            last_pos = f.tell()
            temp_line = f.readline()
            if not temp_line:
              break

            if temp_line.startswith("  ip address"):
              address = temp_line.strip().split()
              interfaces.append(Interface(interface[1], address[2]))
            elif temp_line.startswith("  "):
              continue
            else:
              f.seek(last_pos)
              break
      return interfaces
      
class RouteMap:
  def __init__(self, vlan, ip):
    self.vlan = vlan
    self.ip = ip

  def __str__(self):
    return self.vlan+" "+self.ip

  def read(file_name):
    with open(file_name, "r") as f:
      routes = []
      while True:
        line = f.readline()
        if not line:
          break

        if line.startswith("route-map"):
          interface = line.strip().split()
          while True:
            last_pos = f.tell()
            temp_line = f.readline()
            if not temp_line:
              break

            if temp_line.startswith("  match ip address"):
              route_map = temp_line.strip().split()
              routes.append(RouteMap(interface[1], route_map[3]))
            else:
              f.seek(last_pos)
              break
      return routes
  
class AccessList:
  def __init__(self, ip, block):
    self.ip = ip
    self.block = block

  def __str__(self):
    return self.ip+" "+self.block

  def read(file_name):
    with open(file_name, "r") as f:
      accesses = []
      while True:
        line = f.readline()
        if not line:
          break

        if line.startswith("ip access-list"):
          interface = line.strip().split()
          while True:
            last_pos = f.tell()
            temp_line = f.readline()
            if not temp_line:
              break

            if temp_line.startswith("  "):
              access_list = temp_line.strip().split()
              accesses.append(AccessList(interface[2], access_list[3]))
            else:
              f.seek(last_pos)
              break
      return accesses
  
class AnomalyDetector:

  def __init__(self, ip, block):
    self.ip = ip
    self.block = block

  def __str__(self):
    return self.ip+" "+self.block

  def detect(interface, route_map, access_list):
    print("No anomalies")
    # check for anomalies

if __name__ == "__main__":

  I_fileName = "test"
  interfaces = Interface.read(I_fileName)
  print("Interfaces:")
  for interface in interfaces:
    print("\t"+str(interface))

  R_fileName = "test2"
  route_maps = RouteMap.read(R_fileName)
  print("Route-Maps:")
  for route_map in route_maps:
    print("\t"+str(route_map))

  A_fileName = "test3"
  access_lists = AccessList.read(A_fileName)
  print("Access-Lists:")
  for access_list in access_lists:
    print("\t"+str(access_list))

  AnomalyDetector.detect(interfaces, route_maps, access_lists)
