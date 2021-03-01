import random, string
import webbrowser
import time
import requests
import os
from typing import Iterator
RED   = "\x1b[31m"
GREEN = "\x1b[32m"
RESET = "\x1b[0m"
BOLD  = "\x1b[1m"

if os.name == 'nt':  # Windows
      from colorama import init
      init()


print("""
███╗░░██╗██╗████████╗██████╗░░█████╗░░░░░░░░██████╗░██╗███████╗████████╗
████╗░██║██║╚══██╔══╝██╔══██╗██╔══██╗░░░░░░██╔════╝░██║██╔════╝╚══██╔══╝
██╔██╗██║██║░░░██║░░░██████╔╝██║░░██║█████╗██║░░██╗░██║█████╗░░░░░██║░░░
██║╚████║██║░░░██║░░░██╔══██╗██║░░██║╚════╝██║░░╚██╗██║██╔══╝░░░░░██║░░░
██║░╚███║██║░░░██║░░░██║░░██║╚█████╔╝░░░░░░╚██████╔╝██║██║░░░░░░░░██║░░░
╚═╝░░╚══╝╚═╝░░░╚═╝░░░╚═╝░░╚═╝░╚════╝░░░░░░░░╚═════╝░╚═╝╚═╝░░░░░░░░╚═╝░░░

░██████╗░███████╗███╗░░██╗███████╗██████╗░░█████╗░████████╗░█████╗░██████╗░
██╔════╝░██╔════╝████╗░██║██╔════╝██╔══██╗██╔══██╗╚══██╔══╝██╔══██╗██╔══██╗
██║░░██╗░█████╗░░██╔██╗██║█████╗░░██████╔╝███████║░░░██║░░░██║░░██║██████╔╝
██║░░╚██╗██╔══╝░░██║╚████║██╔══╝░░██╔══██╗██╔══██║░░░██║░░░██║░░██║██╔══██╗
╚██████╔╝███████╗██║░╚███║███████╗██║░░██║██║░░██║░░░██║░░░╚█████╔╝██║░░██║
░╚═════╝░╚══════╝╚═╝░░╚══╝╚══════╝╚═╝░░╚═╝╚═╝░░╚═╝░░░╚═╝░░░░╚════╝░╚═╝░░╚═╝

░░░░░░░░█████╗░██╗░░██╗███████╗░█████╗░██╗░░██╗███████╗██████╗░
░░██╗░░██╔══██╗██║░░██║██╔════╝██╔══██╗██║░██╔╝██╔════╝██╔══██╗
██████╗██║░░╚═╝███████║█████╗░░██║░░╚═╝█████═╝░█████╗░░██████╔╝
╚═██╔═╝██║░░██╗██╔══██║██╔══╝░░██║░░██╗██╔═██╗░██╔══╝░░██╔══██╗
░░╚═╝░░╚█████╔╝██║░░██║███████╗╚█████╔╝██║░╚██╗███████╗██║░░██║
░░░░░░░░╚════╝░╚═╝░░╚═╝╚══════╝░╚════╝░╚═╝░░╚═╝╚══════╝╚═╝░░╚═╝""")
time.sleep(2)
print("Creator  -  Zafros  (Forked by ThatXliner)")
time.sleep(0.3)
print("\n", RED, "Zafros: https://github.com/Zafros56", "\n", GREEN, "ThatXliner: https://github.com/ThatXliner\n", RESET)
time.sleep(0.2)

num = input('Input How Many Codes to Generate and Check: ')

print("Generating...")

def generate_codes(times: int) -> Iterator[str]:
      for code in range(times):
            output = 'https://discord.gift/'
            for length in range(16):
                  output += random.choice(string.ascii_uppercase + string.digits + string.ascii_lowercase)
            yield output

#=============Checker=========================

print("Checking validity!", BOLD)

with open("Nitro Codes.txt") as f:
    for line in generate_codes(int(num)):
        url = "https://discordapp.com/api/v6/entitlements/gift-codes/" + line + "?with_application=false&with_subscription_plan=true"
        if requests.get(url).status_code == 200:
            print(GREEN, " Valid | {} ".format(line))
            break
        else:
        	print(RED, " Invalid | {} ".format(line))
print(RESET)
input("The end! Press Enter 5 times to close the program.")
input("4")
input("3")
input("2")
input("1")
