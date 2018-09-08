import os
import platform


class OSBase:

    def find_local_ip(self):
        raise NotImplementedError("Should have implemented this")


class OSWin(OSBase):

    def find_local_ip(self):
        ip = []
        for line in os.popen("arp -a"):
            rec = line.split()
            if rec:
                if rec[0].count("192"):
                    ip.append(rec[0])
        return ip


class OSLin(OSBase):

    def find_local_ip(self):
        ip = []
        records = os.popen('ip neighbor').read().splitlines()
        for line in records:
            rec = line.split(' ')[0]
            if rec.count('.') == 3:
                ip.append(rec)
        return ip

class OSFabric:

    def __init__(self):
        self.os = platform.system()

    def get_wrapper(self):
        if self.os == 'Linux':
            return OSLin()
        if self.os == 'Windows':
            return OSWin()
        return OSBase()


wrapper = OSFabric().get_wrapper()
