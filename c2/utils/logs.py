import requests
import json

url = "https://discord.com/api/webhooks/1141744703109349386/AxwHt1DK_73t5zlLQoHomAYbiaTOW5OraSKgz5K4Nx2YimuzqJfJEUJVUUnpTirIR-mS" # Remplacez WEBHOOK_ID et WEBHOOK_TOKEN par les identifiants de votre webhook Discord
class Logs():
    def webhook(self, user, host, port, time, method, messsage):
        image = "" # initialisation de la variable image
        if messsage == "max concurrents of 2 are in use":
            image = "https://cdn.discordapp.com/attachments/1075900515378008117/1089606612358021210/istockphoto-1254186911-612x612-removebg-preview.png"
        else:
            image = "https://cdn.discordapp.com/attachments/1075900515378008117/1089606688467853342/83_generated-removebg-preview.png"

        data = {}
        data["embeds"] = []

        embed = {}
        embed["description"] = f"**IP** \n ```fix\n {host}``` \n **PORT** \n ```fix\n {port}``` \n **TIME** \n ```fix\n {time}``` \n  **METHOD** \n ```fix\n {method}``` \n\n **MESSAGE** \n ```fix\n %{messsage}%```"
        embed["color"] = 0x7851A9  # Couleur de l'embed (rouge)
        embed["author"] = {"name": f"{user}", "icon_url": "https://cdn.discordapp.com/attachments/1075900515378008117/1089603308127260782/standard_3.gif"} # Facultatif : Auteur de l'embed avec icône
        embed["thumbnail"] = {"url": f"{image}"} # Facultatif : Miniature de l'embed
        embed["image"] = {"url": "https://cdn.discordapp.com/attachments/1075900515378008117/1087169950726246591/standard_4.gif"} # Facultatif : Image de l'embed

        data["embeds"].append(embed)

        headers = {"Content-Type": "application/json"}

        response = requests.post(url, data=json.dumps(data), headers=headers)

        print(response.status_code)
