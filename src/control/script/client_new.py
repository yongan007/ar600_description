import socket
import os
import subprocess
import json
import struct

# this file accepts connection from server and send to udp port gui
s = socket.socket()

# host = '10.91.50.73'
host = '192.168.31.167'
port = 9999

s.connect((host, port))

def receiver():
    while True:        
        # cmd = s.recv(1024)
        # print(cmd)
        json_length = struct.unpack(">I", s.recv(4))[0]

        json_data = b""  # initiate an empty bytes structure

        while len(json_data) < json_len
        gth:
            chunk = s.recv(min(128*1024, json_length - len(json_data)))
            if not chunk:  
                break  
            json_data += chunk
            # print(json_data)
        data = json.loads(json_data.decode())
        print(data)

        #uncomment here
        # return json_data
#comment this line
receiver()

# un comment from here if gui and robot id availab;le
# def udp_server(HOST="127.0.0.1", PORT=34567):
        
#     s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

#     address = (HOST, PORT)

#     message = receiver()

#     while True:
#         print(message)

#         ret=s.sendto(message, address)

# udp_server()