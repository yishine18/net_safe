from scapy.all import *
import time
def packet_callbacke(packet):
    print(packet.show())
#20200220网络监听，监听本机eth0网卡，并生成mycatch_vm.pcap文件
# ip_str = "172.16.144.130"
# filter_str = "host 172.16.144.130"

'''
使用sniff之前要先安装scapy库，如下，采用豆瓣源模式安装
安装前确认是否已安装pip或者pip3
pip install -i https://pypi.douban.com/simple --trusted-host=pypi.doubanio.com scapy
关于sniff命令
Sniff方法定义：
sniff(filter="",iface="any", prn=function, count=N)
iface参数设置嗅探器所要嗅探的网卡，留空则对所有网卡进行嗅探。
　　例如：wlan0
prn参数指定嗅探到符合过滤器条件的数据包时所调用的回调函数,这个回调函数以接受到的数据包对象作为唯一的参数。
　　例如：
def pack_callback(packet):
    print packet.show()
sniff(prn=pack_callback,iface="wlan0",count=1)
count参数指定你需要嗅探的数据包的个数,留空则默认为嗅探无限个
'''

filter_str = "host 192.168.204.5"

packets = sniff(filter=filter_str,prn=packet_callbacke,iface="eth0",count=6)
# wrpcap("mycatch_baidu.pcap",packets)
wrpcap("mycatch_vm.pcap",packets)