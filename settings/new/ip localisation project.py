import requests
import random
import time

MAGENTA = '\033[95m'
RESET = '\033[0m'

ascii_art = r'''


   ▄████████    ▄████████    ▄████████    ▄████████    ▄█    █▄   
  ███    ███   ███    ███   ███    ███   ███    ███   ███    ███  
  ███    █▀    ███    ███   ███    █▀    ███    █▀    ███    ███  
 ▄███▄▄▄      ▄███▄▄▄▄██▀  ▄███▄▄▄       ███         ▄███▄▄▄▄███▄▄
▀▀███▀▀▀     ▀▀███▀▀▀▀▀   ▀▀███▀▀▀     ▀███████████ ▀▀███▀▀▀▀███▀ 
  ███        ▀███████████   ███    █▄           ███   ███    ███  
  ███          ███    ███   ███    ███    ▄█    ███   ███    ███  
  ███          ███    ███   ██████████  ▄████████▀    ███    █▀   
               ███    ███                                         

 

         ________ ________ ________ ________ ________
        """""""" """""""" """""""" """""""" """"""""
             
                        IP LOCATION
 '''

print(f"{MAGENTA}{ascii_art}{RESET}")

def get_location(ip_address):
    url = f"https://ipinfo.io/{ip_address}/json"
    
    try:
        response = requests.get(url)
        data = response.json()
        if 'loc' in data:
            location = data['loc'].split(',')
            latitude = location[0]
            longitude = location[1]
            print(f"{MAGENTA}{latitude} {longitude}{MAGENTA}")
        else:
            print("La localisation n'a pas pu être déterminée.")
    except Exception as e:
        print(f"Erreur lors de la récupération de la localisation : {e}")

ip = input((f"{MAGENTA}entre l'ip : "))

get_location(ip)

input(f"{MAGENTA}(voila la localisation de l'ip que ta entrer. appuie sur entrer pour quitter...")

time.sleep(0.5)