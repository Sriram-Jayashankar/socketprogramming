import socket



class Network:
    def __init__(self):
        self.client=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.server="172.26.224.1"
        self.port=5555
        self.addr=(self.server,self.port)
        self.pos=self.connect()
        # print(self.id)

    def getpos(self):
        return self.pos

    def connect(self):
        try:
            self.client.connect(self.addr)
            return self.client.recv(2048).decode('utf-8')
        except:
            pass
    
    def send(self,data):
        try:
            self.client.send(str.encode(data))
            return self.client.recv(2048).decode('utf-8')
        except socket.error as e:
            print(e)


# n=Network()
# print(n.send('yayayayay'))
# print(n.send('yaay'))
