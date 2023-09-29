from utils.plugin.commun import Title, Fore
import requests

def dns(target):
    target = target
    try:
        r = requests.get(f"https://api.hackertarget.com/reversedns/?q={target}")
        Title().dns()
        print(Fore.MAGENTA)
        print(r.text+'\n\n\n')
    except:
            print('An error has occurred while sending the request to the API!')