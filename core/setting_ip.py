from core.os_wrapper import wrapper

class SettingIP:

	def __init__(self):
		self.port = [0]
		self.ip = ["127.0.0.1"]

	def find(self):
		self.ip = wrapper.find_local_ip()

	def get_ip(self):
		return self.ip

	def get_port(self):
		return self.port

