from core.setting import Setting
from core.client import client
from core.server import server


def main():
	isExecute = True
	while isExecute:
		name_cmd = input("cmd:")
		if name_cmd == "exit":
			isExecute = False


if __name__ == "__main__":
	main()
