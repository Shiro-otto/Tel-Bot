import os
import getpass
from turtle import clear
os.system('')
from colorama import Fore
from telethon.sync import TelegramClient
from telethon.errors.rpcerrorlist import SessionPasswordNeededError



print('\n'+Fore.LIGHTMAGENTA_EX)
print("___________________________\n")
print ("| ~ █   █▀█ █▀▀ █ █▀█ ~   |")
print ("| ~ █   █ █ █ █ █ █ █ ~   |")
print ("| ~ ▀▀▀ ▀▀▀ ▀▀▀ ▀ ▀ ▀ ~   |")
print (Fore.LIGHTMAGENTA_EX,"________Build by_________")
print (Fore.LIGHTWHITE_EX,"             @Apin(D3)")


async def main():
        await client.send_message('me', 'hello there !')

def login_api():
    Fore.GREEN
    Name = input(Fore.LIGHTMAGENTA_EX + "[-]Nama Telegram : ")
    name = ('./session/' + Name)
    api_id = input(Fore.LIGHTMAGENTA_EX + "[-]Telegram API ID : ")
    api_hash = input(Fore.LIGHTMAGENTA_EX + "[-]Telegram API Hash : ")
    phone = input(Fore.LIGHTMAGENTA_EX + "[-]Nomor Telepon dengan kode negara (+) : ")

    client = TelegramClient(name, api_id, api_hash)

    
    try :
        client.connect()
        if not client.is_user_authorized():
            client.send_code_request(phone)
            client.sign_in(phone, input('Enter The Code : '))
    except SessionPasswordNeededError:
        password = getpass.getpass('password : ')
        client.sign_in(password = password)

    print(Fore.GREEN + "Login Berhasil !")
    print(Fore.GREEN + "Telegram tersebut sudah siap digunakan!")


print(Fore.LIGHTMAGENTA_EX + "Silahkan login telegram anda di bawah")
check_point = input(Fore.GREEN + "apakah telegram tersebut memiliki api id ?\nyes [y] / no [n]  : ")


if check_point == 'yes' or check_point == 'y' or check_point == 'Y' :
    login_api()
else:
    Fore.GREEN
    Name = input(Fore.LIGHTMAGENTA_EX + "[-]Nama Telegram : ")
    name = ('./session/' + Name)
    api_id = '28242955'
    api_hash = '9484aa7210c1ec5433d1b4461ebc465a'
    phone = ''
    client = TelegramClient(name, api_id, api_hash)

    with client:
        client.loop.run_until_complete(main())
    client.connect()
    if not client.is_user_authorized():
         client.send_code_request(phone)
         client.sign_in(phone, input('40779'))
    
    print(Fore.GREEN + "Login Berhasil !")
    print(Fore.GREEN + "Telegram tersebut sudah siap digunakan!")

print(Fore.WHITE)
#tanjungbalai asahan