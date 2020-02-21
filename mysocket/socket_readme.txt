socket：在两个程序之间建立通道。

服务端socket：创建完后会在本机的一个端口上等待连接。实例化一个socket类，循环监听。建立连接后，接收、发送数据，完了关闭。
客户端socket：客户端socket会访问这个端口。实例化一个socket类，去连接一个远程的地址（hostname：port）。建立连接后，接收、发送数据，完了关闭。
完成连接之后，可以信息交互。

实例化
socket(family,type[,protocal])    
family = socket.AF_INET(默认即可)
type = socket.SOCK_STREAM(TCP,默认) / socket.SOCK_DGRAM（UDP）/socket.SOCK_RAW（基本用不到）
protocal = 可选，通常0

初始化TCP socket：
s = socket.socket()  
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

初始化UDP socket：
s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

服务端专用函数3个：
s.bind(ip,port)。  s.bind('127.0.0.1',2345)  注意，前面字符串，后面整数
s.listen(5) ,开启监听模式。5指定可以挂起的最大连接数量。min = 1，一般设置5
s.accept(),接收TCP连接，返回（conn,address）.conn是新的socket对象，用来接收和发送数据，address是客户端的地址。

客户端专用函数：
connect(hostname,port) example: s.connect("127.0.0.1",2345),去连接127.0.0.1的2345端口

客户端、服务端都可以用的函数：
send(string[,flag]),发送string,返回值是发送字节的数量，可能未全部发送。

sendall(string[,flag]),完整发送string,返回之前尝试发送全部数据，成功返回None，失败抛出异常。
str2 = "hello byte...."
b2 = bytes(str2) 将字符串转为字节
sendall(b2)

sendto()  UDP发送数据，sendto(string[,flag],address) address = (ipaddr,port) 元组

recv()  TCP接收数据，recv(bufsize[,flag])flag一般不用，指定bufsize最多可接收的数量

recvfrom() UDP接收数据，返回远端的IP和端口，返回值是(data,address),data是接收的字符串，address是发送数据的套接字地址。

close()关闭socket


注意：
python3 和 python2 关于 input()函数的使用是不同的！！！

python3:
str1 = input("input str:")

input str:123
str1 =  123

input str:hero
str1 =  hero
type str1 =  <class 'str'>
----------------------------
python2:
str1 = input("input str:")
input str:123
type str1 =  <class 'int'>

input str:hero
会报错：hero name undefined



