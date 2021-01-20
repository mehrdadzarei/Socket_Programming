
import socket
import threading

HEADER = 64
PORT = 5015
# SERVER = "192.168.56.10"
SERVER = "158.75.54.56"      # for public server.   158.75.54.56 for wifi   192.168.56.10   158.75.87.169 for ethernet cable
# SERVER = socket.gethostbyname(socket.gethostname())   # for private server
ADDR = (SERVER, PORT)
FORMAT = "utf-8"
DISCONNECT_MESSAGE = "!DISCONNECT"

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

def handle_client(conn, addr):
    
    print(f"[NEW CONNECTION] {addr} connected.")

    connected = True
    while connected:

        msg_length = conn.recv(HEADER).decode(FORMAT)
        # print(f"\n {msg_length} \n")
        if msg_length:

            msg_length = int (msg_length)
            msg = conn.recv(msg_length).decode(FORMAT)
            if msg == DISCONNECT_MESSAGE:
    
                connected = False
            else:
                
                led_state = input("Enter the LED State Value (On 2/ Off 3): ")
                if led_state == '':

                    led_state = 0
                    
                conn.send(bytes(f"{led_state}".encode(FORMAT)))
                # conn.send(bytes(f"message received: {msg}\n".encode(FORMAT)))

            print(f"[{addr}] {msg}")

    conn.close()

def start():

    server.listen()
    print(f"[LISTENING] Server is listening on {SERVER}:{PORT}")
    cheking = True
    while cheking:

        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        # cheking = False
        print(f"[ACTIVE CONNECTIONS] {threading.activeCount() - 1}")

print("[STARTING] server is starting...")
start()

