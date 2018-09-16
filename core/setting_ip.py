from core.os_wrapper import wrapper


class SettingIP:

	def port(self):
		return 9090

	def scan_local_net(self):
		return wrapper.find_local_ip()


ip_list = SettingIP()
