import requests
from datetime import datetime
import time

def submit_form():
    current_time = datetime.now().strftime("%H:%M")
    
    form_data = {
        "requestId": current_time
    }
    # changer votre cookie par le votre de ce type PHPSESSID=votrecookie
    headers = {
        "Accept": "*/*",
        "Accept-Language": "fr-FR,fr;q=0.9,en-US;q=0.8,en;q=0.7",
        "Connection": "keep-alive",
        "Cookie": "", # change me
        "Origin": "https://clicker.fuzeiii.fr",
        "Referer": "https://clicker.fuzeiii.fr/",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36",
        "sec-ch-ua": '"Google Chrome";v="125", "Chromium";v="125", "Not.A/Brand";v="24"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": '"Windows"'
    }
    
    url = "https://clicker.fuzeiii.fr/Core/process_form.php"
    
    try:
       
        response = requests.post(url, data=form_data, headers=headers)
        
        
        if response.status_code == 200:
            print("requete sent avec succes", current_time)
            print("nombre de click >> :", response.text)
        else:
            print("braindead error alert >>> :", response.status_code)
    
    except Exception as e:
        print("fix le code retard:", str(e))


while True:
    submit_form()
    time.sleep(0.1)
