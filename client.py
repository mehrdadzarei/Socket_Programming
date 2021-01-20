
import socket

HEADER = 64
PORT = 5015
# SERVER = "192.168.56.10" # private
SERVER = "158.75.54.56"  # public
ADDR = (SERVER, PORT)
FORMAT = "utf-8"
DISCONNECT_MESSAGE = "!DISCONNECT"

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

def send(msg):

    message = msg.encode(FORMAT)
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT)
    send_length += b' ' * (HEADER - len(send_length))
    client.send(send_length)
    client.send(message)
    print(client.recv(2048).decode(FORMAT))

send("Hello World!")
send("Hello Mehrdad")
send("Hello Piotr")
send("Hello Michal")

send(DISCONNECT_MESSAGE)

