from telethon.sync import TelegramClient
import os,sys
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

print(f""" 
 _______________________
 |                     |
 |  {cy}█▀█▀█ █ █   █  █ {gr}  |
 |  {cy}█ █ █ █ █   █▀█  {gr}  |
 |  {cy}▀ ▀ ▀ ▀ ▀▀▀ ▀  ▀ {gr}  |
 |   Build by          |   
 |________{cy}@Apin(D3){gr}____| 
            """)

api_id = '7777777'
api_hash = '10error'
phone = '+60000'
name = ('')

print(Fore.LIGHTYELLOW_EX + "program ini di buat khusus untuk global check")

while True :
    Name = input(Fore.GREEN + "Nama Telegram : ")
    Folder_name = (Name + '.session')
    Session_name = Path("./session",Folder_name)
    if Session_name.is_file():
        name = ('./session/'+Name)
        break
    else : 
        print(Fore.RED + "Telegram Tersebut tidak di temukan!\nanda harus login dulu (python login.py)!")

client = TelegramClient(name, api_id, api_hash)
client.connect()

X_X = []
group = input('target username grup telegram : ')
with client:
    entity = client.get_participants(group)
    print("Greeting Member ...")
    time.sleep(2)
    for user in entity:
        X_X.append(user)
    
    print("Done Bosque ^_^ !")
