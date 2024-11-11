import requests
from bs4 import BeautifulSoup
import facebook
import time

# Funksjon for å hente posisjon fra Garmin-siden
def hent_posisjon(url):
    respons = requests.get(url)
    if respons.status_code == 200:
        soup = BeautifulSoup(respons.content, 'html.parser')
        
        # Tilpass koden for å hente faktiske bredde- og lengdegrader
        latitude = "58.9700"  # Eksempelverdi
        longitude = "5.7331"  # Eksempelverdi
        
        return latitude, longitude
    else:
        print("Kunne ikke hente data fra Garmin-siden.")
        return None, None

# Funksjon for å publisere på Facebook
def publiser_paa_facebook(tekst, access_token='DIN_FACEBOOK_ACCESS_TOKEN'):
    graph = facebook.GraphAPI(access_token)
    graph.put_object(parent_object='me', connection_name='feed', message=tekst)

# Gjentatt kjøring for å poste posisjonen hver 12. time
url = 'https://share.garmin.com/fedda'
while True:
    latitude, longitude = hent_posisjon(url)
    if latitude and longitude:
        kartlenke = f"https://www.google.com/maps?q={latitude},{longitude}"
        publiser_paa_facebook(f'Min nåværende posisjon: {kartlenke}')
    # Vent i 12 timer (43200 sekunder) før neste post
    time.sleep(43200)
