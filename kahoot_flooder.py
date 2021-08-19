from kahoot import client
import threading2, time, os, pyfiglet, requests
from colorama import Fore, init
from termcolor import colored

req = requests.get("https://raw.githubusercontent.com/CxllZ/kahoot_flooder/main/names.txt")
f = req.text.split("\n")
init()
banner = colored(pyfiglet.figlet_format("Kahoot Flooder", font="slant"), color="red")
pin = 0
ite = 0

os.system("cls" or "clear")
print(banner, f"{Fore.RED}\n By https://github.com/ycl310/KahootFloodBot")
print("The kahoot bots will go away once the program is closed!")
pin = int(input(f"{Fore.GREEN}Enter Kahoot lobby PIN code: "))
ite = int(input(f"{Fore.GREEN}Enter how many bots u want connected?: "))

if ite > 2000:
	print(f"{Fore.RED}Cannot exceed 2000 bots!\n{Fore.RED}Automatically setting amount of bots to 2000!\n{Fore.RED}2000 bots might not acutally join!")
	ite = 2000
else:
	pass

def thread_func(name: str):
	def joinHandle():
		pass
	bot = client()
	bot.join(int(pin), str(name))
	bot.on("joined", joinHandle)

def main():
	t = None
	for i in range(int(ite)):
		t = threading2.Thread(target=thread_func, args=(str(f[i]),))
		t.start()
		time.sleep(int(0.1))
	while True:
		try:
			pass
		except KeyboardInterrupt:
			t.stop()
			exit()

if __name__ == "__main__":
	main()
