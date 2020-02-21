# import socket

# s2 = socket.socket()
# s2.connect(("127.0.0.1",2345))

# data = s2.recv(1024)
# s2.close()
# print ("receive data",repr(data))

# import socket

# #in python3.7
# #if in python2.X ,input() will can't work!
# def conn_socket():
#     client = socket.socket()
#     ip_port=('127.0.0.1',2466)
#     client.connect(ip_port)
#     data = client.recv(1024)
#     while True:

#         if data == b"quit":
#             print("client ready to quit!")
#             break
#         else:
#             print("this is from server:",data.decode())
#             msg_input = input("input :")
#             client.send(bytes(msg_input, encoding="gb2312"))
#             print("send data:",msg_input)
#             if msg_input == "quit":
#                 print("client ready to quit!")
#                 break
#         print("waiting to receive from server:")
#         data = client.recv(1024)
#     client.close()


# def test_001():
#     str1 = input("input str:")
#     str2 = str(str1)
#     print("str1 = ",str2)
#     print ("type str1 = ",type(str1))
#     print ("type str2 = ", type(str2))

# # test_001()
# conn_socket()
import socket

#in python3.7
#if in python2.X ,input() will can't work!
def conn_socket():
    client = socket.socket()
    ip_port=('127.0.0.1',2346)
    client.connect(ip_port)
    data = client.recv(1024)
    while True:

        if data == b"quit":
            print("client ready to quit!")
            break
        else:
            print("this is from server:",data.decode())
            msg_input = input("input :")
            client.send(bytes(msg_input, encoding="gb2312"))
            print("send data:",msg_input)
            if msg_input == "quit":
                print("client ready to quit!")
                break
        print("waiting to receive from server:")
        data = client.recv(1024)
    client.close()


def test_001():
    str1 = input("input str:")
    str2 = str(str1)
    print("str1 = ",str2)
    print ("type str1 = ",type(str1))
    print ("type str2 = ", type(str2))

# test_001()
# conn_socket()

def main():
    conn_socket()

if __name__ == '__main__':
    main()