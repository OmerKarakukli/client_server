#!/usr/bin/env python3
import socket
from time import sleep

IP = ''
PORT = 5566

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
print("Client ready")

while True:
    toSend = input('Data to send: ')
    if toSend == '':
        toSend = 'None'
    s.sendto(bytes(toSend, 'utf-8'), (IP, PORT))
    if toSend == 'exit':
        print('closing socket')
        s.close()
        break
    msg, server_address = s.recvfrom(1024)
    msg = msg.decode('utf-8')
    print(msg)
