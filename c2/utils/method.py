import time
from colorama import *
import sys
from sys import *


class Method():
    def method(self):
        print(f'''
{Fore.LIGHTRED_EX}Methods : {Fore.LIGHTWHITE_EX} AMPLIFICATION
{Fore.LIGHTRED_EX}DNS-AMP : {Fore.LIGHTWHITE_EX}[DNS Amp]
{Fore.LIGHTRED_EX}NTP-AMP : {Fore.LIGHTWHITE_EX}[NTP Amp]
{Fore.LIGHTRED_EX}Methods : {Fore.LIGHTWHITE_EX} UDM
{Fore.LIGHTRED_EX}UDP-PPS : {Fore.LIGHTWHITE_EX}[SPOOF + BOTNET]
{Fore.LIGHTRED_EX}UDP-BYPASS : {Fore.LIGHTWHITE_EX}[UDP PAYLOAD]
{Fore.LIGHTRED_EX}RAKNET : {Fore.LIGHTWHITE_EX}[RACKNET PACKET]
{Fore.LIGHTRED_EX}VALVE : {Fore.LIGHTWHITE_EX}[VSE] 
{Fore.LIGHTRED_EX}DISCORD : {Fore.LIGHTWHITE_EX}[CALL BYPASS]
{Fore.LIGHTRED_EX}Methods : {Fore.LIGHTWHITE_EX}LAYER 3
{Fore.LIGHTRED_EX}GRE : {Fore.LIGHTWHITE_EX}[ETH]
{Fore.LIGHTRED_EX}ESP : {Fore.LIGHTWHITE_EX}[RANDOM PROTOCOL]
{Fore.LIGHTRED_EX}ICMP : {Fore.LIGHTWHITE_EX}[ICMP FLOOD]
{Fore.LIGHTRED_EX}Methods : {Fore.LIGHTWHITE_EX}OF GAMES
{Fore.LIGHTRED_EX}GAME : {Fore.LIGHTWHITE_EX}[UDP PAYLOAD CUSTOM]
{Fore.LIGHTRED_EX}R6-RANK : {Fore.LIGHTWHITE_EX}[UDP-BYPASS]
{Fore.LIGHTRED_EX}MCPE : {Fore.LIGHTWHITE_EX}[MINECRAFT EDTION] 
{Fore.LIGHTRED_EX}FIVEM : {Fore.LIGHTWHITE_EX}[FIVEM CONFORMATION TOKEN]
{Fore.LIGHTRED_EX}ROBLOX : {Fore.LIGHTWHITE_EX}[UDP-BYPASS]
{Fore.LIGHTRED_EX}SCP : {Fore.LIGHTWHITE_EX}[APPLICATION BYPASS]
{Fore.LIGHTRED_EX}FORTNITE : {Fore.LIGHTWHITE_EX} [UDP-SADP]
{Fore.LIGHTRED_EX}Methods : {Fore.LIGHTWHITE_EX} Transmission Control Protocol
{Fore.LIGHTRED_EX}SYN : {Fore.LIGHTWHITE_EX}[Methods SYN with Server spoof] 
{Fore.LIGHTRED_EX}ACK : {Fore.LIGHTWHITE_EX}[Methods ACK with Server spoof] 
{Fore.LIGHTRED_EX}TFO : {Fore.LIGHTWHITE_EX}[TFO Cookie] 
{Fore.LIGHTRED_EX}HANDSHAKE : {Fore.LIGHTWHITE_EX}[TCP-BYPASS Hanshake For OVH] 
{Fore.LIGHTRED_EX}TCP-SW : {Fore.LIGHTWHITE_EX}[TCP SYN-ACK]
{Fore.LIGHTRED_EX}TCP : {Fore.LIGHTWHITE_EX}[TCP-BYPASS]
{Fore.LIGHTRED_EX}SOCKET : {Fore.LIGHTWHITE_EX}[Mass Socket] 
{Fore.LIGHTRED_EX}BBHOST : {Fore.LIGHTWHITE_EX}[TCP-BYPASS For Hosting BB-HOST]
{Fore.LIGHTRED_EX}HETZNER : {Fore.LIGHTWHITE_EX}[TCP-BYPASS For Hosting Hetzner]
{Fore.LIGHTRED_EX}OVH : {Fore.LIGHTWHITE_EX}[Methods Specific OVH]
{Fore.LIGHTRED_EX}CUBIX-BYPASS : {Fore.LIGHTWHITE_EX}[CUBIX-BYPASS]
{Fore.LIGHTRED_EX}Methods : {Fore.LIGHTWHITE_EX} BOTNET
{Fore.LIGHTRED_EX}TCP-NUKE : {Fore.LIGHTWHITE_EX}[BOTNET]
{Fore.LIGHTRED_EX}UDP-NUKE : {Fore.LIGHTWHITE_EX}[BOTNET]
{Fore.LIGHTRED_EX}GAME-NUKE : {Fore.LIGHTWHITE_EX}[BOTNET]
{Fore.LIGHTRED_EX}OVH-NUKE : {Fore.LIGHTWHITE_EX}[BOTNET]
{Fore.LIGHTRED_EX}SYN-NUKE : {Fore.LIGHTWHITE_EX}[BOTNET]
{Fore.LIGHTRED_EX}Methods : {Fore.LIGHTWHITE_EX} LAYER 7
{Fore.LIGHTRED_EX}CF-PRO : {Fore.LIGHTWHITE_EX}[Bypass CloundFlare]
{Fore.LIGHTRED_EX}HTTPGET : {Fore.LIGHTWHITE_EX}[Requete GET Flood]
{Fore.LIGHTRED_EX}TLS : {Fore.LIGHTWHITE_EX}[TLS Version 3]
{Fore.LIGHTRED_EX}OVHBYPASS : {Fore.LIGHTWHITE_EX}OVH-UDP 
{Fore.LIGHTRED_EX}TCP-BYPASS : {Fore.LIGHTWHITE_EX}TCP-BYPASS
{Fore.LIGHTRED_EX}UDPBYPASS : {Fore.LIGHTWHITE_EX}UDPBYPASS
{Fore.LIGHTRED_EX}OVHTCP : {Fore.LIGHTWHITE_EX}OVHTCP
{Fore.LIGHTRED_EX}CS16 : {Fore.LIGHTWHITE_EX}CS16
{Fore.LIGHTRED_EX}TCPL : {Fore.LIGHTWHITE_EX}TCPL
{Fore.LIGHTRED_EX}IPRAND: {Fore.LIGHTWHITE_EX}IPRAND
{Fore.LIGHTRED_EX}WRA : {Fore.LIGHTWHITE_EX}WRA
{Fore.LIGHTRED_EX}HTTPS-NUKE : {Fore.LIGHTWHITE_EX}[BOTNET]''''')