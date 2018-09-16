import socket
from core.setting_ip import ip_list


class Client:

    def __init__(self):
        self.socket = None

    def try_to_connect(self):

        for ip in ip_list.scan_local_net():
            sock = socket.socket()
            try:
                sock.settimeout(2)
                sock.connect((ip, 9090))
                self.socket = sock
                print("connected to: ", ip)
            except Exception:
                print("can't connect to: ", ip)
                sock.close()


cl = Client()
cl.try_to_connect()
