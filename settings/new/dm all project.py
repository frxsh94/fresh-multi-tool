import requests
from colorama import Fore
import time

MAGENTA = '\033[95m'
RESET = '\033[0m'

ascii_art = r'''
  ______  _____   ______   _____  _    _ 
 |  ____||  __ \ |  ____| / ____|| |  | | 
 | |__   | |__) || |__   | (___  | |__| | 
 |  __|  |  _  / |  __|   \___ \ |  __  | 
 | |     | | \ \ | |____  ____) || |  | | 
 |_|     |_|  \_\|______||_____/ |_|  |_| 

 ________ ________ ________ ________ ________
"""""""" """""""" """""""" """""""" """""""" 
             
                  DM ALL
 '''

print(f"{MAGENTA}{ascii_art}{RESET}")
                     
token = input(MAGENTA + 'token : ')  
message = input(MAGENTA +'message : ')

headers = {
        'Authorization': token
    }
channelIds = requests.get("https://discord.com/api/v9/users/@me/channels", headers=headers).json()
    
for channel in channelIds:
        try:
            requests.post(f'https://discord.com/api/v9/channels/{channel["id"]}/messages',headers=headers,json={"content": message})  
            print(f"{MAGENTA} id : {channel['id']}")
            time.sleep(0.7)
        except Exception as e:
            print(f"erreur :  {e}")

input(MAGENTA + 'appuie sur entrer pour sortir')