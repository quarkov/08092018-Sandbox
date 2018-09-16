from core.os_wrapper import wrapper


class SettingIP:

	def scan_local_net(self):
		return wrapper.find_local_ip()


ip_list = SettingIP()
