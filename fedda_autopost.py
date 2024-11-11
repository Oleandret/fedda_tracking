import requests
from datetime import datetime, timedelta
import schedule
import time

# Facebook API-innstillinger
ACCESS_TOKEN = 'DIN_TILGANGSTOKEN'
PAGE_ID = 'DIN_SIDE_ID'

# Funksjon for å legge ut innlegg med bilde
def post_to_facebook(message, image_url):
    url = f'https://graph.facebook.com/{PAGE_ID}/photos'
    payload = {
        'url': image_url,
        'caption': message,
        'access_token': ACCESS_TOKEN
    }
    response = requests.post(url, data=payload)
    if response.status_code == 200:
        print(f"Innlegget ble publisert: {response.json()}")
    else:
        print(f"Feil ved publisering: {response.status_code} {response.text}")

# Planlegg innlegg
def schedule_post(date_time, message, image_url):
    schedule_time = date_time.strftime("%H:%M:%S")
    print(f"Innlegg planlagt for: {date_time}")
    schedule.every().day.at(schedule_time).do(post_to_facebook, message, image_url)

# Hovedfunksjon for å sette opp planlagte innlegg
def main():
    post_dates = [
        datetime.now() + timedelta(days=i) for i in [1, 7, 14]  # Legg ut poster om 1, 7 og 14 dager
    ]

    for date in post_dates:
        schedule_post(date, "Dette er en automatisk testpost med bilde!", "https://eksempel.no/bilde.jpg")

    # Hold programmet i gang for å kjøre planlagte oppgaver
    while True:
        schedule.run_pending()
        time.sleep(60)

if __name__ == "__main__":
    main()
