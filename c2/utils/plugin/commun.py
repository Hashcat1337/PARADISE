from colorama import Fore, Back
from rgbprint import gradient_scroll, gradient_print, Color
import os
import getpass
from os import system, name

username = getpass.getuser()


def clear():
    if name == 'nt':
        system('cls')
    else:
        system('clear')


class Title:
    def home(self):
        clear()

        print(
                    f'\r{Color.deep_sky_blue}Username : {Color.magenta}{username} {Color.gray}| {Color.deep_sky_blue}Broadcast : {Color.magenta}LIVE {Color.gray}| {Color.deep_sky_blue}TELEGRAM : {Color.magenta}@HashCat1337')

        gradient_print(f"""
                      """, start_color=Color.white, end_color=Color.red)
        print(f"""{Color.red}                         
                                  ╔═══════════════════════════╗
                                  ║        Space-Stresser     ║
                         ═╦═══════╩════════════╦═╦════════════╩═══════╦═
                    ╔═════╩════════════════════╩═╩════════════════════╩═════╗
                    ║       {Color.red}Welcome To  {Color.white}Space-Stresser{Color.red}                      ║
                    ║   {Color.white}Powered By {Color.red}Space-Stress API/C2/Stresser{Color.red}             ║
                    ╚═╦═╦═══════════════════════════════════════════════╦═╦═╝
                      ╠═╣  -     →  {Color.white}CONNECTION [ESTABLISHED]{Color.red}  ←      -  ╠═╣
                  ╔═══╩═╩═══════════════════════════════════════════════╩═╩═══╗
                  ║           {Color.reset}Usage{Color.red}:{Color.white} {Color.red}[{Color.white}IP{Color.red}]{Color.white} {Color.red}[{Color.white}PORT{Color.red}]{Color.white} {Color.red}[{Color.white}DURATION{Color.red}]{Color.white} {Color.red}[{Color.white}METHOD{Color.red}]{Color.red}          ║
                  ║        {Color.red}Copyright @ 2023 ShitV2  All Rights Reserved{Color.red}       ║
                  ╚═══════════════════════════════════════════════════════════╝""")
        print('\n')

    def help(self):
        clear()
        gradient_print(
            f"""
                                  ╦ ╦╔═╗╦  ╔═╗             
                                  ╠═╣║╣ ║  ╠═╝             
                                  ╩ ╩╚═╝╩═╝╩
                    ══╦═════════════════════════════════╦══
            ╔═════════╩═════════════════════════════════╩═════════╗
            ║ • .attack   >  Send a attack                        ║
            ║ • .method   >  Shows all the methods                ║                                               
            ║ • .plan     >  Info Plan                            ║
            ║ • .credit   >  Syntaxe Hashcat                      ║
            ║ • .cls      >  Return home                          ║
            ╠═════════════════════════════════════════════════════╣
            ║ Thanks for using Networkshit.                       ║
            ║ Telegram : https://t.me/networkshit                 ║
            ╚═════════════════════════════════════════════════════╝



            """,
            start_color=Color.white,
            end_color=Color.red)

    def credit(self):
        clear()

        gradient_print(
            """
                              ╔═╗╦═╗╔═╗╔╦╗╦╔╦╗
                              ║  ╠╦╝║╣  ║║║ ║ 
                              ╚═╝╩╚═╚═╝═╩╝╩ ╩ 
                   ══╦═════════════════════════════════╦══
            ╔════════╩═════════════════════════════════╩════════╗
            ║ Founders  : HashCAT , Semtex                      ║
            ║ Developer : HashCAT , Smetex                      ║
            ╠═══════════════════════════════════════════════════╣   
            ║               🚀Space-Stress🚀                    ║
            ╚═══════════════════════════════════════════════════╝



            """,
            start_color=Color.white,
            end_color=Color.red)
