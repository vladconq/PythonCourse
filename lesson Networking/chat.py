import socket
import threading
import sys


class Server:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    connections = []
    addresses = []

    def __init__(self):
        self.sock.bind(('0.0.0.0', 10000))
        self.sock.listen(1)

    def handler(self, c, a):
        global connections
        while True:
            data = c.recv(1024)
            if data.decode() == 'ls':
                if len(self.addresses) == 1:
                    prompt = "You are alone".encode()
                    c.send(bytes(prompt))
                else:
                    for address in self.addresses:
                        if a[1] != address[1]:
                            c.send(bytes(str(address).encode()))
            elif data.decode() == 'exit':
                prompt = "Goodbye!".encode()
                c.send(bytes(prompt))
                prompt = (str(a) + " disconnected").encode()
                for connection in self.connections:
                    if c != connection:
                        connection.send(bytes(prompt))
                self.connections.remove(c)
                self.addresses.remove(a)
                c.close()
                break

            elif data.decode()[:data.decode().find(' ')] == 'sendto':
                client = data.decode()[data.decode().find(' ') + 1:]
                client = client[:client.find(')') + 1]

                for connection in self.connections:
                    connection_new = str(connection).split('=')
                    conn = connection_new[-1][:-1]
                    if client == conn:
                        prompt = (str(a) + ":" + (data.decode()[data.decode().find(')') + 1:])).encode()
                        connection.send(bytes(prompt))


            else:
                for connection in self.connections:
                    if data.decode() != 'ls' and c != connection:
                        prompt = (str(a) + ": " + str(data.decode())).encode()
                        connection.send(bytes(prompt))
                if not data:
                    print(str(a[0]) + ':' + str(a[1]), " disconnected")
                    self.connections.remove(c)
                    c.close()
                    break

    def run(self):
        while True:
            c, a = self.sock.accept()
            cThread = threading.Thread(target=self.handler, args=(c, a))
            cThread.daemon = True
            cThread.start()
            self.connections.append(c)
            self.addresses.append(a)
            print(str(a[0]) + ':' + str(a[1]), " connected")


class Client:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def sendMsg(self):
        while True:
            self.sock.send(bytes(input(""), 'utf-8'))

    def __init__(self, address):
        self.sock.connect((address, 10000))
        iThread = threading.Thread(target=self.sendMsg)
        iThread.daemon = True
        iThread.start()
        while True:
            data = self.sock.recv(1024)
            if not data:
                break
            print(str(data, 'utf-8'))


if (len(sys.argv) > 1):
    print("""
TCP chat-client.
1. Enter <ls>, if you want to see participants
2. Enter <exit>, if you want to exit chat
3. Enter <sendto address>, if you want to send msg to a specific user.
   For example: sendto ('127.0.0.1', 1234) hi!
    """)
    client = Client(sys.argv[1])
else:
    print("""
TCP chat-server.
If you want to load client: python3 chat.py <ip>
For example: python3 chat.py 127.0.0.1
Waiting for connections...
    """)
    server = Server()
    server.run()
