from scapy.all import *
import time
def packet_callbacke(packet):
    print(packet.show())
#20200220网络监听，监听本机eth0网卡，并生成mycatch_vm.pcap文件
# ip_str = "172.16.144.130"
# filter_str = "host 172.16.144.130"

filter_str = "host 192.168.204.5"

packets = sniff(filter=filter_str,prn=packet_callbacke,iface="eth0",count=6)
# wrpcap("mycatch_baidu.pcap",packets)
wrpcap("mycatch_vm.pcap",packets)