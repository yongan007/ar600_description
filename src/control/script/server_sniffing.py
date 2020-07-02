# this script works with control state joint. It snifs information from gui and send
#  to remote laptop for publishing into joint state in rviz

import socket
import sys
import json
import struct
def create_socket():
    try:
        global host
        global port
        global s
        host = ""
        port = 9999
        s = socket.socket()

    except socket.error as msg:
        print("Socket creation error: " + str(msg))


# Binding the socket and listening for connections
def bind_socket():
    try:
        global host
        global port
        global s
        print("Binding the Port: " + str(port))

        s.bind((host, port))
        s.listen(10)

    except socket.error as msg:
        print("Socket Binding error" + str(msg) + "\n" + "Retrying...")
        bind_socket()


# Establish connection with a client (socket must be listening)

def socket_accept():
    conn, address = s.accept()
    print("Connection has been established! |" + " IP " + address[0] + " | Port" + str(address[1]))
    send_commands(conn)
    # conn.shutdown()
    conn.close()

# Send commands to client/victim or a friend
def send_commands(conn):
    while True:
        # cmd = "Hello world"
        # data={"id": 2405301, "dtg": 3465258, "slaves":
        # [{"state": "SAFE_OP", "class": "TEtherCatSlaveFTSensOnRobot", "name": "R.FTS", "fx": 17.36, "fy": -35.9, "fz": -177.01, "tx": 0.472, "ty": -0.753, "tz": -0.964}, 
        # {"state": "SAFE_OP", "class": "TDrive", "name": "R.HipR", "mode": "stop", "position": 0, "velocity": 0, "current": 0, "voltage": 23.512, "AI": -108, "DI": 8},
        # {"state": "SAFE_OP", "class": "TDrive", "name": "R.HipS", "mode": "stop", "position": -3.5595703125, "velocity": 0, "current": 0, "voltage": 23.652, "AI": -130, "DI": 8},
        # {"state": "SAFE_OP", "class": "TDrive", "name": "R.HipF", "mode": "stop", "position": 7.734375, "velocity": 0, "current": 0, "voltage": 23.552, "AI": -157, "DI": 8},
        # {"state": "SAFE_OP", "class": "TDrive", "name": "R.Knee", "mode": "stop", "position": 3.37554931640625, "velocity": -0.05767822265625, "current": 0, "voltage": 23.692, "AI": -130, "DI": 8}, 
        # {"state": "SAFE_OP", "class": "TDrive", "name": "R.FootF", "mode": "current", "position": 7.92320251464844, "velocity": 0.279464721679688, "current": 0, "voltage": 23.672, "AI": -130, "DI": 8},
        # {"state": "SAFE_OP", "class": "TDrive", "name": "R.FootS", "mode": "position", "position": 3.5595703125, "velocity": 0, "current": 0, "voltage": 23.632, "AI": -92, "DI": 8},
        # {"state": "SAFE_OP", "class": "TEtherCatSlaveFTSensOnRobot", "name": "L.FTS", "fx": 3.71, "fy": -70.89, "fz": -253.86, "tx": 0.175, "ty": 0.642, "tz": 0.918},
        # {"state": "SAFE_OP", "class": "TDrive", "name": "L.HipR", "mode": "stop", "position": 15.029296875, "velocity": 0, "current": 0, "voltage": 23.572, "AI": -103, "DI": 8},
        # {"state": "SAFE_OP", "class": "TDrive", "name": "L.HipS", "mode": "stop", "position": 6.064453125, "velocity": 0, "current": 0, "voltage": 23.632, "AI": -97, "DI": 8},
        # {"state": "SAFE_OP", "class": "TDrive", "name": "L.HipF", "mode": "stop", "position": 3.4716796875, "velocity": 0, "current": 0, "voltage": 23.592, "AI": -130, "DI": 8}, 
        # {"state": "SAFE_OP", "class": "TDrive", "name": "L.Knee", "mode": "stop", "position": 9.91996765136719, "velocity": 0, "current": 0, "voltage": 23.692, "AI": -135, "DI": 8}, 
        # {"state": "SAFE_OP", "class": "TDrive", "name": "L.FootF", "mode": "current", "position": 5.8392333984375, "velocity": -0.356369018554688, "current": 0, "voltage": 23.552, "AI": -146, "DI": 8}, 
        # {"state": "SAFE_OP", "class": "TDrive", "name": "L.FootS", "mode": "stop", "position": -3.076171875, "velocity": 0, "current": 0, "voltage": 23.552, "AI": -103, "DI": 8}]}

        # data= json.dumps(data).encode()
        
        # when gui is active, i comment out the next line to receive from udp port
        data =  udp_server()
        # data = 

        conn.sendall(struct.pack(">I", len(data)))  # pack as BE 32-bit unsigned int
        # now send the JSON payload itself
        conn.sendall(data)

def udp_server(host='127.0.0.1', port=34568):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    s.bind((host, port))
    print("binded sniifer port to robot")
    while True:



        (data, addr) = s.recvfrom(128*1024)
        data_msg = data.decode()

        print(json.loads(data_msg)["slaves"][3]["position"])

        return data

def main():
    # global data
    create_socket()
    bind_socket()
    socket_accept()


main()