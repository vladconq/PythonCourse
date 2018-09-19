from socket import *

s = socket()
s.connect(('127.0.0.1', 8000))

message = input('->')
while message != 'q':
    s.send(message.encode())
    data = s.recv(1024)
    print("recieved from server: " + str(data.decode()))
    message = input('->')
s.close()
