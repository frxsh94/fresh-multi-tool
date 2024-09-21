GREEN = '\033[92m'

try:
    import os
    import sys

    print("Telechargement des modules requis pour fresh multi tool : ")
    if sys.platform.startswith("win"):
        os.system("python -m pip install --upgrade pip")
        os.system("python -m pip install requests")
        os.system("python -m pip install colorama")
        os.system("python -m pip install fore")
        os.system("python -m pip install datetime")
        os.system("python MultiToolProject.py")

    elif sys.platform.startswith("linux"):
        os.system("python3 -m pip install --upgrade pip")
        os.system("python3 -m pip install requests")
        os.system("python3 -m pip install colorama")
        os.system("python3 -m pip install fore")
        os.system("python3 -m pip install datetime")
        os.system("python3 MultiToolProject.py")

except Exception as e:
    print(e)
    os.system("pause")

input(f"{GREEN}Telechargement fini. Appuie sur entrer pour quitter...")