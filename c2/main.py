from utils.plugin.commun import Title, Fore, Back
from utils.attack import SilenceAttack, getplan,time
from utils.stats import setstat, panelstat
from utils.keys import setkeys
from utils.subscriber import add_user, remove_user, viewuser
from utils.method import Method
from utils.credit import Credit
import sys
import os
from os import system
from sys import stdout
import getpass
from rgbprint import *

username = getpass.getuser()


class Commands:
    def commands(self):
        user = getpass.getuser()
        stdout.write(
            Fore.LIGHTWHITE_EX + f'{Fore.LIGHTWHITE_EX}{username}{Fore.LIGHTMAGENTA_EX}@{Fore.WHITE}RosaStress:~$')
        command = input()
        # Commandes All user
        if command == "help":
            gradient_print(
                f"""
                      ╦ ╦╔═╗╦  ╔═╗  ╔╦╗╔═╗╔╗╔╦ ╦
                      ╠═╣║╣ ║  ╠═╝  ║║║║╣ ║║║║ ║
                      ╩ ╩╚═╝╩═╝╩    ╩ ╩╚═╝╝╚╝╚═╝
           ╔══════════════════════════════════════════╗
           ║  methods : Shows The All Methods         ║
           ║══════════════════════════════════════════║
           ║  attack  : Commands Attack               ║
           ║══════════════════════════════════════════║
           ║  api     : Get API                       ║
           ║ ═════════════════════════════════════════║
           ║  viewuser: Commands Admin                ║ 
           ║══════════════════════════════════════════║
           ║  status  : For Status All The Server     ║
           ║══════════════════════════════════════════║
           ║  credit  : View Credit Rosia C2          ║
           ╚══════════════════════════════════════════╝  
          ╚╦══════════════════════════════════════════╦╝
           ║  helpadmin   :  Commands For Admin       ║
           ╚══════════════════════════════════════════╝
            """,
                start_color=Color.purple,
                end_color=Color.dark_red)
        elif command == "methods":
            Method().method()
        elif command == "tools":
            print()
        elif command.startswith('attack'):
            args = command.split()
            if len(args) < 5:
                gradient_print(
                f"""
                [>] attack [host] [port] [time] [methods]
                            """,
                start_color=Color.purple,
                end_color=Color.dark_red)
            else:
                SilenceAttack().attack(args[1], args[2], args[3], args[4])

        elif command == "plan":
            getplan()
        elif command == "status":
            panelstat()
        elif command == "credit":
            Credit().credit()
        elif command == "cls":
            Title().home()
        # Commanndes Owners
        if command == "helpadmin":
            gradient_print(
                f"""
                             ╦ ╦╔═╗╦  ╔═╗  ╔╦╗╔═╗╔╗╔╦ ╦
                             ╠═╣║╣ ║  ╠═╝  ║║║║╣ ║║║║ ║
                             ╩ ╩╚═╝╩═╝╩    ╩ ╩╚═╝╝╚╝╚═╝
                  ╔══════════════════════════════════════════╗
                  ║  adduser  : Add user                     ║
                  ║══════════════════════════════════════════║
                  ║  deluser  : delete user                  ║
                  ║══════════════════════════════════════════║
                  ║  setstatus: shows status                 ║
                  ║ ═════════════════════════════════════════║
                  ║  setkeys  : set keys api                 ║ 
                  ╚══════════════════════════════════════════╝   
                   """,
                start_color=Color.purple,
                end_color=Color.dark_red)
        elif command.startswith("adduser"):
            if user == "debian":
                args = command.split()
                add_user(args[1], args[2], args[3])
            else:
                return print('No Permission')
        elif command.startswith("deluser"):
            if user == "debian":
                args = command.split()
                remove_user(args[1])
            else:
                return print('No Permission')

        elif command.startswith("setstatus"):
            if user == "debian":
                args = command.split()
                setstat(args[1])
            else:
                return print('No Permission')
        elif command.startswith("setkeys"):
            if user == "root" or "debian":
                args = command.split()
                setkeys(args[1])
            else:
                return print('No Permission')
        elif command == "viewuser":
            viewuser()
    def set_putty_window_title(title):
            username = getpass.getuser()
            sys.stdout.write(f"\033]0;{title}\007")
            sys.stdout.flush()
    CONC = 7
    Attack = 1
    duration = "09/2023"
   

    Attack + 1
        

# Utilisation
new_title = f"SpaceStress [C2] & [{username}]| Running [1/7] | Expiry [10/2023] FOLLOW OUR SOCIALS! \\007"
set_putty_window_title(new_title)

if __name__ == '__main__':
    Title().home()
    while True:
        Commands().commands()