import subprocess
import os
import time

COLOR_STEPS = [
    '\033[38;5;55m',   
    '\033[38;5;91m',   
    '\033[38;5;129m',  
    '\033[38;5;135m',  
    '\033[38;5;141m',  
    '\033[38;5;147m', 
]

RESET = '\033[0m'
BOLD = '\033[1m'

ascii_art = r'''
  ______  _____   ______   _____  _    _ 
 |  ____||  __ \ |  ____| / ____|| |  | | 
 | |__   | |__) || |__   | (___  | |__| | 
 |  __|  |  _  / |  __|   \___ \ |  __  | 
 | |     | | \ \ | |____  ____) || |  | | 
 |_|     |_|  \_\|______||_____/ |_|  |_| 

 ________ ________ ________ ________ ________
"""""""" """""""" """""""" """""""" """""""" 
             
               MULTI-TOOL

'''

def effacer_ecran():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_menu_header():
    effacer_ecran()
    for i, line in enumerate(ascii_art.splitlines()):
        print(f"{COLOR_STEPS[i % len(COLOR_STEPS)]}{line}{RESET}")

current_dir = os.path.dirname(os.path.abspath(__file__))
scripts_dir = os.path.join(current_dir, "settings", "new")

def option1():
    effacer_ecran()
    script_path = os.path.join(scripts_dir, "ddos_attack.py")
    try:
        subprocess.run(['python', script_path], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Erreur lors de l'execution du script : {e}")
    time.sleep(2)

def option2():
    effacer_ecran()
    script_path = os.path.join(scripts_dir, "dm all project.py")
    try:
        subprocess.run(['python', script_path], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Erreur lors de l'execution du script : {e}")
    time.sleep(2)

def option3():
    effacer_ecran()
    script_path = os.path.join(scripts_dir, "ip localisation project.py")
    try:
        subprocess.run(['python', script_path], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Erreur lors de l'execution du script : {e}")
    time.sleep(2)

def option4():
    effacer_ecran()
    script_path = os.path.join(scripts_dir, "numero location project.py")
    try:
        subprocess.run(['python', script_path], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Erreur lors de l'execution du script : {e}")
    time.sleep(2)

def option5():
    effacer_ecran()
    script_path = os.path.join(current_dir, "port check project.py")
    try:
        subprocess.run(['python', script_path], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Erreur lors de l'execution du script : {e}")
    time.sleep(2)

def option6():
    effacer_ecran()
    script_path = os.path.join(current_dir, "ddos_attack2.py")
    try:
        subprocess.run(['python', script_path], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Erreur lors de l'execution du script : {e}")
    time.sleep(2)

def menu():
    while True:
        print_menu_header()
        print(f"  {COLOR_STEPS[0]}{{1}}{RESET}       {COLOR_STEPS[1]}{{2}}{RESET}        {COLOR_STEPS[2]}{{3}}{RESET}        {COLOR_STEPS[3]}{{4}}{RESET}          {COLOR_STEPS[4]}{{5}}{RESET}         {COLOR_STEPS[5]}{{6}}{RESET}")
        print(f"{COLOR_STEPS[0]}panel ddos{RESET}   {COLOR_STEPS[1]}DM All{RESET}     {COLOR_STEPS[2]}IP Loc{RESET}   {COLOR_STEPS[3]}Numero info{RESET}   {COLOR_STEPS[4]}soon...{RESET}   {COLOR_STEPS[5]}soon...{RESET}")
        
        choix = input(f"{COLOR_STEPS[1]}\n__user@fresh\n|$  {RESET}")

        if choix == '1':
            option1()
        elif choix == '2':
            option2()
        elif choix == '3':
            option3()
        elif choix == '4':
            option4()
        elif choix == '5':
            option5()
        elif choix == '6':
            option6()
        else:
            print(f"{COLOR_STEPS[1]}Choix invalide, essayez a nouveau.{RESET}")
            time.sleep(2)

if __name__ == "__main__":
    menu()