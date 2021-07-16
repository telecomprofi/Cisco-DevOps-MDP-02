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

