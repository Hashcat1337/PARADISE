from utils.plugin.commun import Title, Fore
import requests

def geoip(target):
    target = target
    try:
        r = requests.get(f"https://api.hackertarget.com/geoip/?q={target}")
        Title().geoip()
        print(Fore.MAGENTA)
        print(r.text+'\n\n\n')
    except:
        print('An error has occurred while sending the request to the API!')