import os
import platform

def ping(ip_address, count):
    if platform.system().lower() == "windows":
        response = os.system("ping -n " + str(count) + " " + ip_address)
    else:
        response = os.system("ping -c " + str(count) + " " + ip_address)

    if response == 0:
        print(ip_address + " est accessible")
    else:
        print(ip_address + " est inaccessible")

def main():
    ip_address = input("Entrez une adresse IP à pinger : ")
    count = 15  # Nombre de pings à envoyer
    ping(ip_address, count)

if __name__ == '__main__':
    main()
