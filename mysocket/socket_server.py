# -*- coding:utf8 -*-
import socket
import sys

s1 = socket.socket()
s1.bind(("127.0.0.1",2345))

s1.listen(5)
goon = True
str1 = "hello socket!!!"
#string to byte
str1_tobyte = str1.encode(encoding="utf8")
while goon:
    try:
        conn,address = s1.accept()
        print("a new connect from ,", address)
    except KeyboardInterrupt:
        print("KeyboardInterrupt ")
        sys.exit()
    conn.sendall(str1_tobyte)
    conn.close()
    print ("I have a dream")
    goon = False

