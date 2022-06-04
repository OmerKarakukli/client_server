#!/usr/bin/env python3
import socket
from time import sleep
import serial

arduinoSerialData = serial.Serial('/dev/ttyACM0', 115200)

IP = ''
PORT = 5566

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind((IP, PORT))
print("UDP server listening at port {}".format(PORT))

while True:
    client_msg, client_address = s.recvfrom(1024)
    client_msg = client_msg.decode('utf-8')
    print("{}: {}".format(client_address, client_msg))
    if client_msg == 'exit':
        print('exit message received, closing socket')
        s.close()
        exit()
    elif client_msg == 'None':
        s.sendto(bytes('Server: massage is empty, please resend', 'utf-8'), client_address)
    else:
        arduinoSerialData.write(bytes(client_msg, 'utf-8'))
        arduinoSerialData.write(bytes('\n', 'utf-8'))
        
        while (arduinoSerialData.inWaiting() == 0): # wait for arduino
            pass
        
        arduinoIn = ""
        while (arduinoSerialData.inWaiting() > 0):
            arduinoIn = arduinoSerialData.readline().strip().decode("ascii")
            s.sendto(bytes("Arduino: " + arduinoIn, 'utf-8'), client_address)
