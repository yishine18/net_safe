# # -*- coding:utf8 -*-
# import socket
# import sys

# s1 = socket.socket()
# s1.bind(("127.0.0.1",2345))

# s1.listen(5)
# goon = True
# str1 = "hello socket!!!"
# #string to byte
# str1_tobyte = str1.encode(encoding="utf8")
# while goon:
#     try:
#         conn,address = s1.accept()
#         print("a new connect from ,", address)
#     except KeyboardInterrupt:
#         print("KeyboardInterrupt ")
#         sys.exit()
#     conn.sendall(str1_tobyte)
#     conn.close()
#     print ("I have a dream")
#     goon = False

import socket

#in python3.7
#if in python2.X ,input() will can't work!

sk=socket.socket()
ip_port=('127.0.0.1',2466)
sk.bind(ip_port)
sk.listen(5)
b_data = b'quit'
print("type b_data:",type(b_data)) #type b_data: <class 'bytes'>
print("waiting...")
conn, address = sk.accept()
msg = "this is server !!!"
conn.send(msg.encode())
data = conn.recv(1024)
while True:

    print("type data",type(data)) #type data <class 'bytes'>
    print("type data.decode", type(data.decode())) #type data.decode <class 'str'>
    print("this is from client: ",data.decode())
    if data == b'quit':
        print("ready to quit!!!")
        break
    else:
        msg_input = input("input :")
        conn.send(bytes(msg_input, encoding="gb2312"))
        if msg_input == "quit":
            print("server ready to quit!")
            break
    print("waiting to receive from client:")
    data = conn.recv(1024)

conn.close()