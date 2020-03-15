import socket
import pickle
import pathlib
import json
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


def check_if_exist(reply):
    file = pathlib.Path("Users/" + reply[0] + ".json")
    if file.exists():
        print("exist")
        return "True"
    else:
        print("Doesn't exist")
        return "False"


def check_password(reply):
    path = "Users/"+reply[0]+".json"
    with open(path) as json_file:
        data = json.load(json_file)
        password = data["password"]

    if reply[1] == password:
        print("pass correct")
        return "True"
    else:
        print("pass un correct")
        return "False"


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
                # if reply[0] == answer[0] and reply[1] == answer[1]:
                login = check_if_exist(reply)
                if login == "True":
                    password = check_password(reply)
                    if password == "True":
                        send_answer = "True"
                    else:
                        send_answer = "False"
                else:
                    send_answer = "False"

            conn.sendall(pickle.dumps(send_answer))

        except:
            break

    print("Lost connection")
    conn.close()


while True:
    conn, addr = s.accept()
    print("Connected to:", addr)

    start_new_thread(threaded_client, (conn,))
