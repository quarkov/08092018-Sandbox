import socket
from core.setting_ip import ip_list

class Server:

    def __init__(self):
        self.sock = socket.socket()
        self.sock.bind(("", ip_list.port()))
        self.sock.listen(1)
        self.conn, self.addr = self.sock.accept()

    def thread(self):
        pass
        
    # def clients_connected(self):


server = Server()

"""
import socket


sock = socket.socket()
sock.bind(('', 9090))
sock.listen(1)
conn, addr = sock.accept()

print(conn)
print("connected:", addr)

while True:
    data = conn.recv(1024)
    if data:
        print(data)
        break
    conn.send(data.upper())
"""

