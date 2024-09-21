import requests
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

              NUMBER LOOKUP
 '''

print(f"{MAGENTA}{ascii_art}{RESET}")

def find_phone_info_api(phone_number):
    url = "https://neutrinoapi.net/phone-validate"

    params = {
        "user-id": "fresh94",
        "api-key": "b60gThfQnj2UeTKLboyXQnH04UFyskrjcvDOMBdzWuJDlXVv",
        "number": phone_number
    }

    response = requests.post(url, params=params)

    if response.status_code == 200:
        data = response.json()
        
        location = data.get("location", "Unknown")
        carrier = data.get("prefix-network", "Unknown")
        timezone = data.get("timezone", "Unknown")
        is_valid = data.get("valid", False)
        country = data.get("country", "Unknown")
        country_code = data.get("country-code", "Unknown")
        local_number = data.get("local-number", "Unknown")
        international_number = data.get("international-number", "Unknown")
        phone_type = data.get("type", "Unknown")
        currency_code = data.get("currency-code", "Unknown")

        return {
            "Location": location,
            "Carrier": carrier,
            "Timezone": timezone,
            "Valid": is_valid,
            "Country": country,
            "Country Code": country_code,
            "Local Number": local_number,
            "International Number": international_number,
            "Type": phone_type,
            "Currency Code": currency_code,
        }
    else:
        print(f"probleme avec l'api : {response.status_code}")
        return None

phone_number = input(f"{MAGENTA}entre le numero que tu veux lookup (exemple : +33123456789) :{RESET}")

phone_info = find_phone_info_api(phone_number)

if phone_info:
    for key, value in phone_info.items():
        colored_key = (key + ': ')
        colored_value = (str(value))
        print(f"{colored_key}{colored_value}")
else:
    print("un probleme est survenu")

input(f"{MAGENTA}\nappuie sur entrer pour quitter ... ")