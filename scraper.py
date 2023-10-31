from telethon.sync import TelegramClient
import os, sys
os.system('')
from colorama import Fore
import csv
from pathlib import Path
import time

re="\033[1;31m"
gr="\033[1;32m"
ab="\033[1;33m"
bc="\033[1;34m"
cd="\033[1;35m"
cy="\033[1;36m"

def banner():
    print(f"""
{re}╔╦╗{cy}┌─┐┬  ┌─┐{re}  ╔═╗{cy}┌─┐┬─┐┌─┐┌─┐┌─┐
{re} ║ {cy}├┤ │  ├┤ {re}  ╚═╗{cy}│  ├┬┘├─┤├─┘├┤ 
{re} ╩ {cy}└─┘┴─┘└─┘{re}  ╚═╝{cy}└─┘┴└─┴ ┴┴  └─┘

    Modified by {ab}@Apin
        """)

api_id = '7777777'
api_hash = '10error'
phone = '+60000'
name = ('')

while True :
    Name = input(Fore.GREEN + "Isi Nama Telegram : ")
    Folder_name = (Name + '.session')
    Session_name = Path("./session",Folder_name)
    if Session_name.is_file():
        name = ('./session/'+Name)
        break
    else : 
        print(Fore.RED + "Telegram Tersebut tidak di temukan!\nanda harus login dulu (python login.py)!")

client = TelegramClient(name, api_id, api_hash)

client.connect()
print("berhasil login\n")

banner()


Group = input('Isi Username grup yang ingin di scrape (grup harus publik dan member tidak di hide) : ')
group = client.get_entity(Group)

file_name = input("Isi Nama File Yang anda inginkan : ")
folder = ('../../documents/tel-bot/'+file_name)
File_name = (folder + '.csv')

print(gr+'[+] Scraping Member...')
time.sleep(1)

all_participants = []

all_participants = client.get_participants(group)

print(gr+'[+] Menyimpan File...')
time.sleep(1)
with open(File_name,"w",encoding='UTF-8') as f:
    writer = csv.writer(f,delimiter=",",lineterminator="\n")
    writer.writerow(['name','username','user id', 'access hash','group'])
    for user in all_participants:
        if user.username:
            username= user.username
        else:
            username= ""
        if user.first_name:
            first_name= user.first_name
        else:
            first_name= ""
        if user.last_name:
            last_name= user.last_name
        else:
            last_name= ""
        name= (first_name + ' ' + last_name).strip()
        writer.writerow([name,username,user.id,user.access_hash,group.title])      
print(gr+'[+] Berhasil Scrape Member.')
