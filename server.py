import socket, threading   #threading allows two functions to run simultaneously

header = 64
FORMAT = 'utf-8'
port = 5050

"""My ip address comes here and i will call it a my ip"""
myIP = socket.gethostbyname(socket.gethostname())

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

"""Now we are going to bind our ip address and port to the server
NOTE: It should be a tuple"""
server.bind((myIP, port))

"""Creating functions to make our server work"""
def handle_client(conn, addr):  # conn stands for connection and addr stands for address
    print(f"[CONNECTED] {addr} has connected to the server")
    connected = True
    while connected:
        msg_len = conn.recv(header).decode(FORMAT)
        if msg_len:
            msg_len = int(msg_len)
            msg = conn.recv(msg_len).decode(FORMAT)
            if msg == "bye":
                connected = False
            print(f"[User] {msg}")
            conn.send("Hi there!".encode(FORMAT))
    conn.close()

def start():  # This is going to start our server
    server.listen()
    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args= (conn, addr))
        thread.start()

print("[STARTING] Server listening....")
start()
