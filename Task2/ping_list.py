import os
from termcolor import colored

#print colored('hello', 'red'), colored('world', 'green')
#Or in Python 3:

#print(colored('hello', 'red'), colored('world', 'green'))
hostnames=["telecomprofi.xyz", "cisco.com", "google.com"]
for hostname in hostnames:
  response = os.system("ping -c 1 " + hostname)
  if response == 0:
    print(colored(hostname, 'green'), colored(' is up!', 'green'))
  else:
    print(colored(hostname, 'red'), colored(' is down!','red'))

for hostname in hostnames:
  ip_resolved = os.system("dig +short A" + hostname)
  print("A record for " +hostname+" is ")

import socket
import dns.resolver

# Basic query
for rdata in dns.resolver.resolve('www.yahoo.com') :
    print("www.yahoo.com has IP in A record: ",rdata)
