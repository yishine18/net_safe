import socket

str_msg = input("请输入要发送的信息:")
s2 = socket.socket()
s2.connect(("127.0.0.1",2345))
s2.sendall(bytes(str_msg,encoding="utf-8"))
str_recv = s2.recv(1024).decode()
print(str_recv)
# s2.send(str_msg.encode(encoding="gb2312"))
s2.close()


#ls /root/gitskills/net_safe/mysbprocess