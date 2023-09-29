import getpass, pymysql, requests, socket
from utils.plugin.commun import gradient_print, Color, clear


def ongoing(host, port, time, method):
    username = getpass.getuser()

    if host.startswith("http://") or host.startswith("https://"):
        try:
            response = requests.get(host)
            if response.status_code == 200:
                message = f"{Color.green}Ready"
            else:
                message = f"{Color.red}Down"
        except requests.ConnectionError:
            message = f"{Color.red}Down"
    else:

        # Vérification de l'adresse IP
        try:
            socket.create_connection((host, port), timeout=2)
            message = f"{Color.green}Ready"
        except socket.error:
            message = f"{Color.red}Down"
    clear()
    gradient_print(f"""
                              ╔═╗╦╦  ╔═╗╔╗╔╔═╗╔═╗
                              ╚═╗║║  ║╣ ║║║║  ║╣ 
                              ╚═╝╩╩═╝╚═╝╝╚╝╚═╝╚═╝""", start_color=0x4BBEE3, end_color=Color.magenta)
    print(f"""                             {Color.magenta}SERVER STATUS [{message}{Color.magenta}] 🚀
                    {Color.deep_sky_blue}══╦═════════════════════════════════╦══
            ╔═════════╩═════════════════════════════════╩═════════╗
            ║  {Color.magenta}Target {Color.red}> {Color.white_smoke}[{Color.cyan}{host}{Color.white_smoke}]{Color.deep_sky_blue}
            ║  {Color.magenta}Port {Color.red}> {Color.white_smoke}[{Color.cyan}{port}{Color.white_smoke}]{Color.deep_sky_blue}
            ║  {Color.magenta}Time {Color.red}> {Color.white_smoke}[{Color.cyan}{time}{Color.white_smoke}]{Color.deep_sky_blue}
            ║  {Color.magenta}Method {Color.red}> {Color.white_smoke}[{Color.cyan}{method}{Color.white_smoke}]{Color.deep_sky_blue}
            ║  {Color.magenta}END {Color.red}> {Color.white_smoke}[{Color.cyan}{end}{Color.white_smoke}]{Color.deep_sky_blue}
            ╚═════════════════════════════════════════════════════╝



            """)

