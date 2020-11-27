'''
written by: Alex Mulvaney
Class: 471_Computer_Communications

desc: a simple FTP client-server file transfer protocol
'''
import socket

#establish a connection to the server
soc = socket.socket()
host = input(str("Please enter the host address of the sender: "))
port = 8080
soc.connect((host, port))
print("Connected... ")

#create a file for the incoming file
filename = input(str("Please enter a filename for the incoming file: "))
file = open(filename, 'wb')
file_data = soc.recv(1024)
file.write(file_data)
file.close()
print("File has been received successfully.")