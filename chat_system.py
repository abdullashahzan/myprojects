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



print("program ran successfully!")

