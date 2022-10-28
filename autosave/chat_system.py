import socket
import threading 

#Making server

host = '192.168.8.108'
port = 9090

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, port))

server.listen()

clients = []
nicknames = []

#broadcasting
def broadcast(message):
    for client in clients:
        client.send(message)
    return

#Handle
def handle(client):
    try:
        message = client.recv(1024)
        print(f"{nicknames[clients.index(client)]} says {message}")
        broadcast(message)
    except:
        index = clients.index(client)
        clients.remove(client)
        client.close()
        nickname = nicknames[index]
        nicknames.remove(nickname)
        break

#recieving
def recieve():
    while True:
        client, address = server.accept()
        print(f"Connected with {str(address)}!")
        
        client.send("NICK".encode('utf-8'))
        nickname = client.recv(1024)
        nicknames.append(nickname)
        clients.append(client)
        
        print(f"The nickname of the client is {nickname}")
        broadcast(f"{nickname} has entered the chat!\n".encode('utf-8'))
        client.send("Connected to the server".encode('utf-8'))
        
        thread = threading.Thread(target = handle, args = (clients,))
        thread.start()

recieve()

print("program ran successfully!")

