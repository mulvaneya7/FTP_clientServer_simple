import socket

#opening port and listening for connections
soc = socket.socket()
host = socket.gethostname()
port = 8080
soc.bind((host, port))
soc.listen(1)
print(host)
print("Waiting for any incoming connections... ")
conn, addr = soc.accept()
print(addr, "Has connected to the server")

#select file to upload to client
filename = input(str("Please enter the filename of the file: "))
file = open(filename, 'rb')
file_data = file.read(1024)
conn.send(file_data)
print("Data has been transmitted successfully")