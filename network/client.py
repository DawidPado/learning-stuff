import socket
import threading

localhost = '127.0.0.1'
port = 5555

nickname = input("choose your nickname")

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((localhost, port))


def recive():
    while True:
        try:
            message = client.recv(1024).decode('ascii')
            if message == "NICK":
                client.send(nickname.encode('ascii'))
            else:
                print(message)
        except:
            print('an error occur')
            client.close()
            break


def write():
    while True:
        message = f"{nickname}: {input('')}"
        client.send(message.encode("ascii"))


recive_thred = threading.Thread(target=recive)
write_thred = threading.Thread(target=write)

recive_thred.start()
write_thred.start()
