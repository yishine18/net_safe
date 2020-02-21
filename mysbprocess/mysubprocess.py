import subprocess

#这是一个包含程序参数的列表
# child = subprocess.Popen(["ping","-c","5","www.baidu.com"])
# child.wait(),有这个，就会先输出ping
print("this is test...")#程序执行会先输出这个



#这是一个字符串
# child = subprocess.Popen("ping -c 5 www.baidu.com",shell=True)
# print(child)
# print(type(child))
# child  ------- <class 'subprocess.Popen'>
# PING www.baidu.com (14.215.177.38) 56(84) bytes of data.
# 64 bytes from 14.215.177.38 (14.215.177.38): icmp_seq=1 ttl=54 time=26.6 ms
# 64 bytes from 14.215.177.38 (14.215.177.38): icmp_seq=2 ttl=54 time=27.0 ms
# 64 bytes from 14.215.177.38 (14.215.177.38): icmp_seq=3 ttl=54 time=26.9 ms
# 64 bytes from 14.215.177.38 (14.215.177.38): icmp_seq=4 ttl=54 time=26.9 ms
# 64 bytes from 14.215.177.38 (14.215.177.38): icmp_seq=5 ttl=54 time=91.9 ms

# --- www.baidu.com ping statistics ---
# 5 packets transmitted, 5 received, 0% packet loss, time 4005ms
# rtt min/avg/max/mdev = 26.564/39.859/91.928/26.034 ms
# [Finished in 4.2s]


# child = subprocess.check_output(["ping","-c","5","www.baidu.com"])
child = subprocess.check_output("ping -c 5 www.baidu.com",shell=True)
print("child = %s,child type = %s"%(child,type(child)))
# child = b'PING www.baidu.com (14.215.177.38) 56(84) bytes of data.\n
# 64 bytes from 14.215.177.38 (14.215.177.38): icmp_seq=1 ttl=54 time=29.0 ms\n
# 64 bytes from 14.215.177.38 (14.215.177.38): icmp_seq=2 ttl=54 time=32.0 ms\n
# 64 bytes from 14.215.177.38 (14.215.177.38): icmp_seq=3 ttl=54 time=27.5 ms\n
# 64 bytes from 14.215.177.38 (14.215.177.38): icmp_seq=4 ttl=54 time=26.7 ms\n
# 64 bytes from 14.215.177.38 (14.215.177.38): icmp_seq=5 ttl=54 time=29.9 ms\n
# \n--- www.baidu.com ping statistics ---\n
# 5 packets transmitted, 5 received, 0% packet loss, time 4007ms\n
# rtt min/avg/max/mdev = 26.737/29.036/32.013/1.856 ms\n
# ',child type = <class 'bytes'>
# [Finished in 4.1s]