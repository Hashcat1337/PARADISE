import json
from utils.plugin.commun import gradient_print, Color, clear

def setstat(server):
    with open('configs.json', 'r') as f:
        subscriptions = json.load(f)
    subscriptions["server"] = server
    with open('configs.json', 'w') as f:
        json.dump(subscriptions, f)


def panelstat():
    with open('configs.json', 'r') as f:
        subscriptions = json.load(f)
        Server_status = "None"
    if subscriptions['server'] == "Working":
        Server_status = "Working"
        clear()
        gradient_print(f"""
                         ╔═╗┌┬┐┌─┐┌┬┐┬ ┬┌─┐
                         ╚═╗ │ ├─┤ │ │ │└─┐
                         ╚═╝ ┴ ┴ ┴ ┴ └─┘└─┘
        ╔═══════════════════════════════════════════════════╗
          • Status Server {Server_status}
          • Methods VIP   {Server_status}
          • Methods Basic {Server_status}
          • Methods GAME  {Server_status}
        ╚═══════════════════════════════════════════════════╝
        
        
        """,
        start_color=0x4BBEE3, 
        end_color=Color.magenta)
    else:
        Server_status = "No Working"
        clear()
        gradient_print(f"""
                         ╔═╗┌┬┐┌─┐┌┬┐┬ ┬┌─┐
                         ╚═╗ │ ├─┤ │ │ │└─┐
                         ╚═╝ ┴ ┴ ┴ ┴ └─┘└─┘
        ╔═══════════════════════════════════════════════════╗
          • Status Server {Server_status}
          • Methods VIP   {Server_status}
          • Methods Basic {Server_status}
          • Methods GAME  {Server_status}
        ╚═══════════════════════════════════════════════════╝
        
        
        """,
        start_color=0x4BBEE3, 
        end_color=Color.magenta)
        



    