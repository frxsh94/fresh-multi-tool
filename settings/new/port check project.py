import socket
from datetime import datetime
import threading
import random

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
             
              PORT CHECK
'''

print(f"{MAGENTA}{ascii_art}{RESET}")

def get_target():
    try:
        hostname = input(f"{MAGENTA}entre l'ip : {RESET}")
        target = socket.gethostbyname(hostname)
        return target
    except socket.gaierror:
        print(f"{MAGENTA}impossible{RESET}")
        exit()

def get_port_list():
    return range(1, 10000)

def scan_port(target, port):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.settimeout(1)
        result = s.connect_ex((target, port))
        if result == 0:
            print(f"{MAGENTA}Le port {port} est ouvert{RESET}")

def port_scanner():
    try:
        target = get_target()
        port_list = get_port_list()
        threads = []
        start_time = datetime.now()

        for port in port_list:
            thread = threading.Thread(target=scan_port, args=(target, port))
            threads.append(thread)
            thread.start()

        for thread in threads:
            thread.join()
    except Exception as e:
        print(f"{MAGENTA}erreur : {e}{RESET}")
    else:
        end_time = datetime.now()
        duration = end_time - start_time
        print(f"{MAGENTA}scan terminer en {duration} seconde{RESET}")

if __name__ == '__main__':
    port_scanner()
    input(f"{MAGENTA}voila les ports ouverts. appuie sur entrer pour quitter...{RESET}")
