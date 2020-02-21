# -*- coding:utf-8 -*-
import socket
import subprocess

def run_command(command):
    command = command.rstrip()
    print(command)
    try:
        child = subprocess.check_output(command,shell=True)
        # print("type child = ",type(child))
        # str = str(child,encoding="utf-8")
        # print(str)
        print(child)
    except:
        child = "can not execute the command.\r\n"
        return child

s1 = socket.socket()
s1.bind(("127.0.0.1",2345))#一个服务没有被连接多久会被回收?
s1.listen(5)
while True:
    conn,address = s1.accept()#这里是元组返回形式，accept()返回（conn,address），新套接字对象和发送数据
    print("a new connect from",address)
    # conn.send("hello word".encode(encoding="gb2312"))
    conn.sendall(bytes("hello word", encoding = "utf8"))

    data = conn.recv(1024)
    command = data.decode()
    print("the command is :"+command)

    output = run_command(command)
    conn.sendall(bytes(str(output),encoding="utf-8"))
    # conn.send(output)
    break

conn.close()


