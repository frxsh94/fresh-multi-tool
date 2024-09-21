MAGENTA = '\033[95m'
GREEN = '\033[92m'

try:
    import os

    print(f"{MAGENTA}telechargement des modules utiles pour fresh multi tool : ")

    os.system("python -m pip install --upgrade pip")
    os.system("python -m pip install requests")
    os.system("python -m pip install colorama")
    os.system("python -m pip install fore")
    os.system("python -m pip install datetime")

except Exception as e:
    print(e)
    os.system("pause")

input(f"{GREEN}telechargement fini. appuie sur entrer pour quitter puis lance le multi tool...")