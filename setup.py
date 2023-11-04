#AP

"""
Authon : Apin (D3)
github Programming based on python

kalo pinter silahkan edit
kalo ga paham ya berarti otak lu ga nyampe
terima kasih sudah menggunakan program saya
"""
re="\033[1;31m"
gr="\033[1;32m"
cy="\033[1;36m"

import os, sys
import time
os.system('')

def banner():
	print(f"""
	{re}╔═╗{cy}┌─┐┌┬┐┬ ┬┌─┐
	{re}╚═╗{cy}├┤  │ │ │├─┘
	{re}╚═╝{cy}└─┘ ┴ └─┘┴
	""")

def requirements():
	def csv_lib():
		banner()
		print(gr+'['+cy+'+'+gr+']'+cy+' this may take some time ...')
		print(gr+"[+] Installing requirements ...")
		os.system("""
			pip3 install telethon numpy pandas colorama
			python3 -m pip install telethon numpy pandas colorama
			""")
	banner()
	print(gr+"[+] requierments Installed.\n")


def update_tool():
	banner()
	#print(gr+'['+cy+'+'+gr+']'+cy+' removing old files ...')
	os.system('del setup.py');time.sleep(3)
	print(gr+'['+cy+'+'+gr+']'+cy+' getting latest files ...')
	os.system("""
		curl -s -O https://raw.githubusercontent.com/Shiro-otto/Tel-Bot/main/setup.py chmod 777 *.py
		""");time.sleep(3)
	print(gr+'\n['+cy+'+'+gr+']'+cy+' update completed.\n')

try:
	if any ([sys.argv[1] == '--update', sys.argv[1] == '-u']):
		update_tool()
	elif any ([sys.argv[1] == '--install', sys.argv[1] == '-i']):
		requirements()
	elif any ([sys.argv[1] == '--help', sys.argv[1] == '-h']):
		banner()
		print("""
			
	( --config  / -c ) setup api configration
	( --merge   / -m ) merge 2 .csv files in one 
	( --update  / -u ) update tool to latest version
	( --install / -i ) install requirements
	( --help    / -h ) show this msg 
			""")
	else:
		print('\n'+gr+'['+re+'!'+gr+']'+cy+' unknown argument : '+ sys.argv[1])
		print(gr+'['+re+'!'+gr+']'+cy+' for help use : ')
		print(gr+'$ python3 setup.py -h'+'\n')
except IndexError:
	print('\n'+gr+'['+re+'!'+gr+']'+cy+' no argument given : '+ sys.argv[1])
	print(gr+'['+re+'!'+gr+']'+cy+' for help use : ')
	print(gr+'['+re+'!'+gr+']'+cy+' https://github.com/th3unkn0n/TeleGram-Scraper#-how-to-install-and-use')
	print(gr+'$ python3 setup.py -h'+'\n')
