subprocess的理解

subprocess.call(args,*,stdin=None,stdout=None,stderr=None,shell=True)
args 是一个字符串或者是一个包含程序参数的列表，用来指明需要执行的命令，这个参数就可以在Python中执行的对应命令。
如果是序列类型，第一个元素通常是可执行文件的路径。
也可以用executeable参数指定可执行文件的路径。-------这个需要再推敲
shell = True 参数让接受字符串类型的变量作为命令，并调用shell去执行这个字符串。
shell = False 参数只接受数组变量作为命令，并将数组的第一个元素作为命令，剩下的全部作为该命令的参数。

win7 启动记事本
>>> import subprocess
>>> child = subprocess.call("notepad.exe")
>>> print child
0
0表成功，非0表失败。

以下两个一样
>>> import subprocess
>>> child = subprocess.call_all("ping -c 5 www.baidu.com")
>>> child = subprocess.call_all("ping -c 5 www.baidu.com",shell=True)
>>> print child
0

>>> import subprocess
>>> child = subprocess.check_output("ping -c 5 www.baidu.com",shell=True)
>>> print child
PING www.baidu.com (14.215.177.38) 56(84) bytes of data.
64 bytes from 14.215.177.38 (14.215.177.38): icmp_seq=1 ttl=54 time=27.7 ms
64 bytes from 14.215.177.38 (14.215.177.38): icmp_seq=2 ttl=54 time=29.8 ms
64 bytes from 14.215.177.38 (14.215.177.38): icmp_seq=3 ttl=54 time=29.5 ms
64 bytes from 14.215.177.38 (14.215.177.38): icmp_seq=4 ttl=54 time=31.1 ms
64 bytes from 14.215.177.38 (14.215.177.38): icmp_seq=5 ttl=54 time=36.8 ms

--- www.baidu.com ping statistics ---
5 packets transmitted, 5 received, 0% packet loss, time 4007ms
rtt min/avg/max/mdev = 27.673/30.980/36.810/3.117 ms

>>> 

以上3个函数基于Popen()函数的安装classPopen()

classPopen(args,bufsize=0,executable=None,stdin=None,stdout=None,stderr=None,preexec_fn=None,close_fds=False,shell=False,cwd=None,env=None,universal_newlines=False,startupinfo=None,creationflags=0)

classPopen("notepad","test.txt")

import subprocess

#这是一个包含程序参数的列表
#child = subprocess.Popen(["ping","-c","5","www.baidu.com"])
#print(child)
#print("this is test...")
#print(type(child))

#这是一个字符串
child = subprocess.Popen("ping -c 5 www.baidu.com",shell=True)
print(child)
print("this is test...")
print(type(child))

上述两段程序都能得到底下的结果
<subprocess.Popen object at 0x7fd13ef65fd0>
<class 'subprocess.Popen'>
this is test...
PING www.baidu.com (14.215.177.38) 56(84) bytes of data.
PING www.baidu.com (14.215.177.39) 56(84) bytes of data.
64 bytes from 14.215.177.39 (14.215.177.39): icmp_seq=1 ttl=54 time=18.4 ms
64 bytes from 14.215.177.39 (14.215.177.39): icmp_seq=2 ttl=54 time=105 ms
64 bytes from 14.215.177.39 (14.215.177.39): icmp_seq=3 ttl=54 time=25.5 ms
64 bytes from 14.215.177.39 (14.215.177.39): icmp_seq=4 ttl=54 time=18.1 ms
64 bytes from 14.215.177.39 (14.215.177.39): icmp_seq=5 ttl=54 time=22.0 ms




import subprocess
def run_command(command):
	command = command.rstrip()
	try:
		child = subprocess.check_output(command,shell=True)
	except Exception as e:
		child = "can't execute the command.."
	return child
execute = "ls /root/gitskills/net_safe/mysbprocess"
output = run_command(execute)
print(output)

b'mysubprocess.py\nreadme_subprocess.txt\nsub001.py\n'
[Finished in 0.1s]

--- www.baidu.com ping statistics ---
5 packets transmitted, 5 received, 0% packet loss, time 4005ms
rtt min/avg/max/mdev = 18.133/37.850/105.181/33.774 ms
[Finished in 9.1s]

