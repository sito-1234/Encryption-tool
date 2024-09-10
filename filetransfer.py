#!/bin/usr/env python3
import socket
# define server ip addres and port
server_ip = '0.0.0.0' # it Listens on all network interfaces
server_port = 5001

#Buffer size for receiving data
BUFFER_SIZE =4096

#Create a socket object (TCP)
server_socket= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#Bind the socket to the ip port
server_socket.bind((server_ip, server_port))

#start the listening for incoming connections
server_socket.listen(5)
print(f"Server is listening on {server_ip}:{server_port}...")

# NOW TIME TO ACCEPT THE CONNECTION
cliebt_socket, addr = server_socket.accept()
print(f"Connection established with {addr}")
#Recive the file to write name from the client
file_name = client_socket.recv(BUFFER_SIZE).decode()
print(f"Receiving file: {file_name}")

#open a file to write the incoming data
with open(f"recieved_{file_name}", "wb") as file:
	while True:
		#recive data from client
		data = client_socket.recv(BUFFER_SIZE)
		if not data:
			break
		#writw the data to the file
		file.write(data)
print(f"File recived and saved as 'received_{file_name}'")
# close the client and server sockets
client_socket()
server_socket()
