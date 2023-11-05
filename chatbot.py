#!/bin/env python3
from telethon.sync import TelegramClient
from telethon.errors.rpcerrorlist import PeerFloodError, UserDeactivatedBanError, InputUserDeactivatedError
import pandas as pd
import os, sys
from colorama import Fore
os.system('')
from pathlib import Path
import random
import traceback
import time

re="\033[1;31m"
gr="\033[1;32m"
cy="\033[1;36m"

#Apin (D3)

class main():

    def banner():
        
        print(f"""{gr}
 _________________________________
 |                               |
 |  {cy}█▀▀ █ █ █▀█ ▀█▀ █▀█ █▀█ ▀█▀{gr}  |
 |  {cy}█   █▀█ █▀█  █  █▀█ █ █  █ {gr}  |
 |  {cy}▀▀▀ ▀ ▀ ▀ ▀  ▀  ▀▀▀ ▀▀▀  ▀ {gr}  |
 |   Build by                 |   
 |______________{cy}@Apin(D3){gr}________| 
            """)

    def send_sms():     
        api_id = '7777777'
        api_hash = '10error'

        #Choose the session file
        name = ('')
        me = ('')

        main.banner()

        while True :
            Name = input(Fore.GREEN + "Nama Telegram : ")
            Folder_name = (Name + '.session')
            Session_name = Path("./session",Folder_name)
            if Session_name.is_file():
                name = ('./session/'+Name)
                me = Name
                break
            else : 
                print(Fore.RED + "Telegram tersebut tidak di temukan!\nSilahkan login terlebih dahulu")

        client = TelegramClient(name, api_id, api_hash)
        client.connect()
        

        #member file
        member_file = ('')
        
        while True :
            folder_member = input("Isi nama file member : ")
            Folder_name = (folder_member + '.csv')
            file_name = Path("../../documents/tel-bot/",Folder_name)
            if file_name.is_file():
                member_file = ('../../documents/tel-bot/'+Folder_name)
                break
            else : 
                print(Fore.RED + "File tidak di temukan! Silahkan scrape terlebih dahulu ")

        users = pd.read_csv(member_file)

         
        messages = open("../../documents/tel-bot/pesan.txt","r",encoding="UTF-8")
        message = messages.read()
        
        sent = 0
        n_number = 0

        for x,user in users.iterrows():
            n_number += 1
            if sent == 44:
                print(Fore.CYAN + "message sent to {} users".format(sent))
                client.disconnect()
                sys.exit()
            if n_number % 20 == 0:  
                print (Fore.YELLOW + 'Delay 30 - 60 detik untuk menghindari error server telethon')
                time.sleep(random.randrange(30,60))

            try:
                print(gr+"[+] Sending Message to : {}".format(Fore.CYAN+user['name']))
                receiver = client.get_input_entity(user['user id'])

                client.send_message(receiver, message.format(user['name']))
                sent += 1
                print(gr+"Sukses Mengirim Pesan")
                time.sleep(random.randrange(5,15))
            except PeerFloodError:
                print(re+"[!]Akun anda di batasi\n[!] Please check spam info bot.")
                print(Fore.CYAN)
                print(str(sent) + " pesan di kirim oleh ".format(me))
                client.disconnect()
                sys.exit()
            except UserDeactivatedBanError:
                print(Fore.RED + "akun anda di banned !!!")
                time.sleep(1)
                print(Fore.RED + "akun anda di blokir")
                print(str(sent) + " pesan di kirim oleh ".format(me))
                sys.exit()
            except InputUserDeactivatedError:
                print(re+"Akun Tersebut diban / diblokir\nGagal mengirim pesan ...")
                time.sleep(5)
                continue
            except:
                traceback.print_exc()
                print(Fore.RED + "Gagal Mengirim Pesan!")
                time.sleep(5)
                continue

        print("Done. Message sent to all users.")



main.send_sms()