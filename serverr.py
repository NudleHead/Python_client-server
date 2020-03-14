import socket
import pickle
from _thread import *
import sys

server = "192.168.8.104"
port = 5555

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    s.bind((server, port))
except socket.error as e:
    str(e)

s.listen(2)
print("Waiting for a connection, Server Started")

answer = ["Ola", "spi"]


def threaded_client(conn):
    conn.send(pickle.dumps("Connected"))
    reply = ""
    while True:
        try:
            data = pickle.loads(conn.recv(2048))
            reply = data

            if not data:
                print("Disconnected")
                break
            else:
                if reply[0] == answer[0] and reply[1] == answer[1]:
                    reply = "True"
                else:
                    reply = "False"

            conn.sendall(pickle.dumps(reply))
        except:
            break

    print("Lost connection")
    conn.close()


while True:
    conn, addr = s.accept()
    print("Connected to:", addr)

    start_new_thread(threaded_client, (conn,))