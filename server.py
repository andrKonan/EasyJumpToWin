import socket
from _thread import *
import sys

serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server = 'localhost'
port = 55774

server_ip = socket.gethostbyname(server)

try:
    serverSocket.bind((server, port))
except socket.error as e:
    print(str(e))
		
serverSocket.listen(10)
print("Started on \"{}\" in port {}".format(server, port))

def clientThread(connection):
	connection.send(str.encode("connected"))
	reply = ""
	while True:
		try:
			data = connection.recv(2048)
			reply = data.decode("utf-8")
			if not data:
				print("disconect")
				break
			else:
				print("recive: ", reply)
				print("sending: ", reply)
			connection.sendall(str.encode(reply))
		except Exception as err:
			print("err1: ", str(err))
	connection.close()
			
while True:
	connection, address = serverSocket.accept()
	print("connected: ", address)
	
	start_new_thread(clientThread, (connection,))