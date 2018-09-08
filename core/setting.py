from core.setting_ip import SettingIP


class Setting:

	def __init__(self):
		self.ip = SettingIP()

	def get_setting_ip(self):
		self.ip.find()
		return self.ip

