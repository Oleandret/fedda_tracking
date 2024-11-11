# fedda_tracking
henter ut gps data fra garmin, og poster på facebook med kart hvor han er i verden
# Facebook Position Poster

Dette Python-programmet er laget for å hente GPS-posisjonen din fra en Garmin-delingsside og publisere denne posisjonen som et innlegg på Facebook hver 12. time.

## Funksjoner
- Henter posisjon i form av breddegrad og lengdegrad fra en Garmin-delingsside.
- Genererer en Google Maps-lenke basert på posisjonen.
- Publiserer en statusoppdatering med lenken på Facebook ved hjelp av Facebook Graph API.
- Kjøres automatisk med et intervall på 12 timer.

## Forutsetninger
Før du begynner, må du ha følgende installert:
- **Python 3.7+**
- **Nødvendige Python-biblioteker**:
  - `requests`
  - `beautifulsoup4`
  - `facebook-sdk`

Installer biblioteker ved hjelp av:
```bash
pip install requests beautifulsoup4 facebook-sdk
```

## Bruk
1. **Klon dette depotet** og naviger til prosjektmappen.
2. **Sett inn din Facebook-tilgangstoken** i koden:
   
   Erstatt `'DIN_FACEBOOK_ACCESS_TOKEN'` med din gyldige tilgangstoken fra Facebook.
3. **Kjør programmet**:
   ```bash
   python facebook_position_poster.py
   ```
   Programmet vil begynne å hente posisjon fra Garmin-siden og publisere oppdateringer på Facebook hver 12. time.

## Tilpasning
- **Garmin URL**: Endre `url`-variabelen til din egen Garmin-delingsside.
- **Posisjonsdata**: Tilpass funksjonen `hent_posisjon()` basert på strukturen på Garmin-siden din.

## Sikkerhet
- Hold tilgangstoken og annen sensitiv informasjon skjult. Bruk en `.env`-fil eller et annet metode for å lagre nøkkeldata sikkert.

## Lisens
Dette prosjektet er lisensiert under MIT-lisensen. Se `LICENSE`-filen for mer informasjon.

## Forfatter
[Ole Andre Torjussen]

