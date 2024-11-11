# Program for automatisk publisering av Facebook-innlegg

Dette programmet er designet for å legge ut innlegg med bilder automatisk på en Facebook-side ved forhåndsbestemte tidspunkter.

## Forutsetninger
- Python 3.x
- Biblioteker: `requests`, `schedule`
- En Facebook-app med de nødvendige tillatelsene (`publish_pages`, `pages_manage_posts`)
- En langvarig tilgangstoken fra Meta for API-tilgang

## Installasjon
1. Klon dette repositoriet eller kopier koden til din lokale maskin.
2. Installer nødvendige Python-biblioteker ved å kjøre:
   ```bash
   pip install requests schedule
   ```

## Konfigurasjon
1. Erstatt `DIN_TILGANGSTOKEN` med din faktiske tilgangstoken.
2. Erstatt `DIN_SIDE_ID` med ID-en til Facebook-siden du ønsker å publisere på.

## Bruk
Kjør programmet ved å bruke følgende kommando:
```bash
python script_navn.py
```
Programmet vil automatisk planlegge og legge ut innlegg med bilder på de spesifikke datoene som er definert i koden.

## Hvordan programmet fungerer
- Programmet planlegger innlegg basert på en liste over datoer, som i dette tilfellet er satt til 1, 7 og 14 dager fremover.
- Hvert innlegg legges ut ved hjelp av Facebook Graph API, og programmet bruker `schedule`-biblioteket til å holde oversikt over når innleggene skal publiseres.
- Programmet kjører kontinuerlig for å sikre at planlagte oppgaver utføres.

## Eksempel på kode
```python
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
```

## Feilsøking
- Hvis du mottar en feilmelding, sjekk at tilgangstokenet er gyldig og at API-en har de riktige tillatelsene.
- Sørg for at side-ID-en og bilde-URL-en er korrekte.

## Lisens
Dette prosjektet er lisensiert under MIT-lisensen.