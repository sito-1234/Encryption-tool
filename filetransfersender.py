#!/bin/usr/env python3
import socket
import os

# Define server ip and port
server_ip = '192.168.174.158'
server_port = 5001

#create a socket object (TCP)
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#Conect to the server
client_socket.connect((server_ip, server_port))
print(f"Connected to the server at {server_ip}:{server_port}")

#Send the file name to the server
file_name = os.path.basename(file_path)
client_socket.senf(file_name.encode())

#Open the file and send its content
with open(file_path, 'rb')as file:
	while True:
		data = file.read(4096)
		if not data:
			break
		client_socket.send(data)
print(f"File sent sucessfully!")

#always remember to close the conection
client_socket.close()

