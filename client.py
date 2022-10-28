import socket

header = 64
port = 5050
FORMAT = 'utf-8'
server = socket.gethostbyname(socket.gethostname())

"""socket.socket is done to open a new socket"""
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((server, port))

def send(msg):
    message = msg.encode(FORMAT)
    msg_len = len(message)
    send_len = str(msg_len).encode(FORMAT)
    send_len += b" " * (header - len(send_len))
    client.send(send_len)
    client.send(message)
    print(client.recv(2048).decode(FORMAT))

send("hello world")
input()
send("Yo world")
input()
send("bye")
    
