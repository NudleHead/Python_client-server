import socket
import pickle
import pathlib
import json
import threading
from _thread import *
import sys
print_lock = threading.Lock()
server = "192.168.8.104"
port = 5555

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    s.bind((server, port))
except socket.error as e:
    str(e)

s.listen(4)
print("Waiting for a connection, Server Started")


def check_if_exist(reply):
    file = pathlib.Path("Users/" + reply[1] + ".json")
    if file.exists():
        print("exist")
        return "True"
    else:
        print("Doesn't exist")
        return "False"


def check_password(reply):
    path = "Users/"+reply[1]+".json"
    with open(path) as json_file:
        data = json.load(json_file)
        password = data["password"]

    if reply[2] == password:
        print("pass correct")
        return "True"
    else:
        print("pass un correct")
        return "False"


def login_to_the_bank(reply):
    login = check_if_exist(reply)
    if login == "True":
        password = check_password(reply)
        if password == "True":
            return "True"
        else:
            return "False"
    else:
        return "False"


def user_account_information(reply):
    path = "Users/" + reply[1] + ".json"
    with open(path) as json_file:
        data = json.load(json_file)
        name = data["login"]
        number = data["number"]
        balance = data["balance"]
    return [name, number, balance]


def operation_on_user_balance(reply):
    info = money_transfer(reply)
    if info is False:
        return False
    else:
        with open("Users/"+info[0]+".json") as json_file:
            data = json.load(json_file)
            sender_balance = data["balance"]
            update_sender_balance = sender_balance - int(info[2])
            data["balance"] = update_sender_balance

        with open("Users/"+info[0]+".json", "w") as json_file:
            json.dump(data, json_file)

        with open("Users/" + info[1] + ".json") as json_file:
            data_receiver = json.load(json_file)
            receiver_balance = data_receiver["balance"]
            update_receiver_balance = receiver_balance + int(info[2])
            data_receiver["balance"] = update_receiver_balance

        with open("Users/" + info[1] + ".json", "w") as json_file:
            json.dump(data_receiver, json_file)

        return [update_sender_balance, update_receiver_balance]


def money_transfer(reply):
    with open("Users/fast_check.json") as json_file:
        data = json.load(json_file)
        receiver_items = next((item for item in data["users"] if str(item["number"]) == reply[3]), False)
        if receiver_items:
            receiver = receiver_items.get("name")
            sender_items = next((item for item in data["users"] if str(item["number"]) == reply[2]), False)
            if sender_items:
                sender = sender_items.get("name")
                return [sender, receiver, reply[4]]
            else:
                return False

        else:
            return False


def refresh(reply):
    with open("Users/" + reply[1] + ".json") as json_file:
        data = json.load(json_file)
        balance = data["balance"]

        return str(balance)


def threaded_client(conn):
    conn.send(pickle.dumps("Connected"))
    reply = ""
    while True:
        try:
            data = pickle.loads(conn.recv(2048))
            reply = data
            send_answer = ""

            if not data:
                print("Disconnected")
                print_lock.release()
                break
            else:
                if reply[0] == 'login':
                    send_answer = login_to_the_bank(reply)
                elif reply[0] == 'account':
                    send_answer = user_account_information(reply)
                elif reply[0] == 'transfer':
                    print(reply)
                    send_answer = operation_on_user_balance(reply)
                elif reply[0] == "refresh":
                    print(reply[1])
                    send_answer = refresh(reply)

            conn.sendall(pickle.dumps(send_answer))

        except:
            break

    print("Lost connection")
    conn.close()


while True:
    conn, addr = s.accept()
    print("Connected to:", addr)

    start_new_thread(threaded_client, (conn,))
