#!/bin/env python3
from operator import inv
import sys
import os
import time
import random
import traceback
import pandas as pd
os.system('')
from colorama import Fore
from pathlib import Path

print ("\033[1;95m")
print ("░█▀█░█▀▄░█▀▄░█░█▄ █ █▀▀▀  ")
print ("░█▀█░█░█░█░█░█░█ ▀█ █ ▀█  ")
print ("░▀░▀░▀▀░░▀▀░░▀░▀░ ▀ ▀▀▀▀  ")
print ("Build")
print ("      by \033[1;92m @Apin(D3)")
print ("\033[1;92m")
from telethon.sync import TelegramClient
from telethon.errors.rpcerrorlist import PeerFloodError, UserPrivacyRestrictedError, FloodWaitError, UserChannelsTooMuchError, ChatWriteForbiddenError, UserIdInvalidError, UsernameNotOccupiedError
from telethon.tl.functions.channels import InviteToChannelRequest
from telethon.tl.functions.contacts import ResolvePhoneRequest, ResolveUsernameRequest



api_id = '7777777'
api_hash = '10error'
phone = '+60000'

name = ('')
me = ('')

while True :
    Name = input(Fore.GREEN + "Nama Telegram : ")
    Folder_name = (Name + '.session')
    Session_name = Path("./session",Folder_name)
    if Session_name.is_file():
        name = ('./session/'+Name)
        me = Name
        break
    else : 
        print(Fore.RED + "Telegram tersebut tidak ditemukan!\nsilahkan login terlebih dahulu dengan command (python login.py)")

client = TelegramClient(name, api_id, api_hash)
client.connect()
print('\n')

member_file = ''

while True :
    folder_member = input("Isi nama file member : ")
    Folder_name = (folder_member + '.csv')
    file_name = Path("../../documents/tel-bot/",Folder_name)
    if file_name.is_file():
        member_file = ('../../documents/tel-bot/'+Folder_name)
        break
    else : 
        print(Fore.RED + "File tidak di temukan! Silahkan scrape terlebih dahulu ")


grup = input("username grup yang ingin di add (pastikan anda sudah bergabung) : ")
group = client.get_entity(grup)

group_entity = client.get_input_entity(group)


users = pd.read_csv(member_file)

print('\n')
mode = int(input("1. add dengan Username\n2. add dengan User Id\nPilih mode : "))

#Calculating the time to wait for FloodWaitError
def Hitung_waktu (e):
    number = e.seconds
    hour = 0
    min = 0
    sec = 0
    if number >= 3600:
        hour = number // 3600
        number -= (hour * 3600)
    if number >= 60:
        min = number // 60
        number -= (min * 60)
    sec = number

    print(Fore.RED+f"""Mencapai Limit Server Telethon.
anda harus menunggu {hour} jam {min} menit {sec} detik untuk add selanjutnya""")
#The End 

#username
def add_username():
  invited_member = 0
  for x,user in users.iterrows():
    n = 0
    n += 1
    Fore.WHITE
    if n % 20 == 0:  
        print ('Tunggu selama 60 detik untuk menghindarin banjiran error')
        time.sleep(120)
    try:
        print(Fore.GREEN + "Menginvite {}".format(Fore.CYAN + user['username']))
        user_to_add = client(ResolveUsernameRequest(user['username']))

        client(InviteToChannelRequest(group_entity, [user_to_add]))
        invited_member += 1
        print(Fore.GREEN + "jumlah member di invite : ", invited_member)
        time.sleep(random.randrange(3, 10))
    except PeerFloodError:
        print(Fore.RED + "Akun anda di batasi\nSilahkan Cek Spam Info Bot!")
        print(Fore.GREEN + "Invited by " + me)
        client.disconnect()
        sys.exit()
    except UserPrivacyRestrictedError:
        print(Fore.RED + "Pengguna tersebut tidak mengizinkan siapa pun untuk di invite ke grup.\nSkip ...")
        time.sleep(random.randrange(10, 20))
        continue
    except FloodWaitError as e:
        Hitung_waktu(e)
        print(Fore.GREEN + "jumlah member di invite : ", invited_member)
        print(Fore.GREEN + "Invited by " + me)
        client.disconnect()
        sys.exit()
    except UserChannelsTooMuchError:
        print(Fore.RED + "Pengguna tersebut telah mencapai limit grup/channel untuk bergabung\nSkip ...")
        time.sleep(random.randrange(10, 20))
        continue
    except ChatWriteForbiddenError:
        print(Fore.RED + "anda belum bergabung ke grup tersebut!\nPlease join the group first !")
        client.disconnect()
        sys.exit()
    except UsernameNotOccupiedError:
        print(Fore.RED + "Username tidak ditemukan / telah di banned \nSkip ...")
        time.sleep(random.randrange(10,20))
        continue
    except:
        print(Fore.RED + "unexpected error")
        traceback.print_exc()
        time.sleep(5)
        continue

  print(Fore.LIGHTMAGENTA_EX + 'Well Done !!!\nyou did it till the end !')


#userid
def adding():
  invited_member = 0
  for x,user in users.iterrows():
    n = 0
    n += 1
    Fore.WHITE
    if n % 20 == 0:  
        print ('Tunggu selama 60 detik untuk menghindarin banjiran error')
        time.sleep(120)
    try:
        print(Fore.GREEN + "Menginvite {}".format(Fore.CYAN + user['name']))
        user_to_add = client.get_input_entity(user['user id'])

        client(InviteToChannelRequest(group_entity, [user_to_add]))
        invited_member += 1
        print(Fore.GREEN + "jumlah member di invite : ", invited_member)
        time.sleep(random.randrange(3, 10))
    except PeerFloodError:
        print(Fore.RED + "Akun anda di batasi\nSilahkan Cek Spam Info Bot!")
        print(Fore.GREEN + "Invited by " + me)
        client.disconnect()
        sys.exit()
    except UserPrivacyRestrictedError:
        print(Fore.RED + "Pengguna tersebut tidak mengizinkan siapa pun untuk di invite ke grup.\nSkip ...")
        time.sleep(random.randrange(10, 20))
        continue
    except FloodWaitError as e:
        Hitung_waktu(e)
        waiting = input("wait ?\n[y] / [n]\n")
        if waiting == 'y' or waiting == "Y":
            print(Fore.WHITE + "WAITING . . .")
            time.sleep(e.seconds + 1)
        else :
            print("Stopping now...")
            print(Fore.GREEN + "jumlah member di invite : ", invited_member)
            print(Fore.GREEN + "Invited by " + me)
            client.disconnect()
            sys.exit()
    except UserChannelsTooMuchError:
        print(Fore.RED + "Pengguna tersebut telah mencapai limit grup/channel untuk bergabung\nSkip ...")
        time.sleep(random.randrange(10, 20))
        continue
    except ChatWriteForbiddenError:
        print(Fore.RED + "anda belum bergabung ke grup tersebut!\nPlease join the group first !")
        client.disconnect()
        sys.exit()
    except UserIdInvalidError:
        print(Fore.RED + "Pengguna tersebut dibanned/diblokir\nSkip ...")
        time.sleep(random.randrange(10,20))
        continue
    except:
        print(Fore.RED + "Pengguna tersebut tidak dikenal\nSkipping ..")
        time.sleep(5)
        continue

  print(Fore.LIGHTMAGENTA_EX + 'Well Done !!!\nyou did it till the end !')

    

if mode == 1:
    adding()
elif mode == 2:
    add_username()
