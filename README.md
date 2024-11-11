# fedda_tracking og fedda_autopost - Program som tracker posisjon til Fredrik sin gps, og legger det på facebook. + autoposting av innlegg på facebook frem i tid.
Sør-Amerika på tvers for Mental Helse Ungdom
Alle pengene går til Mental Helse Ungdom for å styrke Hjelpechatten, deres viktige chat-tjeneste for ungdom med psykiske utfordringer. Støtten vil også bidra til økt synlighet, slik at flere unge over hele Norge kan få hjelp.
Hei! Mitt navn er Fredrik Huth Jensen, og i desember 2024 legger jeg ut på mitt hittil største eventyr. Jeg skal gå over 2000 kilometer fra Stillehavet i Chile til Atlanterhavet i Argentina, over Andesfjellene og gjennom Patagonia. Målet mitt er å fullføre reisen på 120 dager. Men - turen handler ikke bare om utholdenhet, den handler om noe mye viktigere: å gi ungdom håp og inspirasjon. Jeg har derfor opprettet en spleis for å støtte arbeidet til Mental Helse Ungdom. Målet er å samle inn 200 000 kroner innen 1. mai 2025.

Hvorfor Mental Helse Ungdom?

Jeg har gjennom deler av livet slitt med dødsangst, og i perioder har jeg vært så deprimert at jeg har vurdert å ta mitt eget liv. Jeg vet hva et godt støtteapparat betyr, og uten det ville ikke ekspedisjonen jeg nå skal ut på ha blitt virkelighet. Mental Helse Ungdom er der for unge som sliter, for de som føler seg alene og som ikke ser noen utvei. For de som ikke har det samme støtteapparatet som jeg har hatt. De søker å gi unge en mening med livet – følelsen av at de er verdt noe for andre og at de kan påvirke verden rundt seg. Nettopp derfor er arbeidet deres så utrolig viktig - det redder liv.

Hvorfor Sør-Amerika på tvers?

Helt siden jeg var liten har jeg søkt fart og spenning. Jeg har jobbet som ranger og safariguide i Sør-Afrika og jeg har drevet eget safariselskap i Tanzania. I 2022 gikk jeg alene fra Svartehavet i Georgia og helt til Det kaspiske hav i Aserbajdsjan – 1000 kilometer til fots.

Takket være terapi, gode venner og egen innsats, har jeg klart å finne balansen og bygge et liv jeg er stolt av. Å utfordre meg selv og å søke nye utfordringer er en viktig del av dette, og ekspedisjonen jeg nå skal ut på er et resultat av alt jeg har vært gjennom. Dette blir den ultimate testen på min styrke og utholdenhet, både fysisk og psykisk – men også min sjanse til å bidra til en sak som er større enn meg selv.

Bli med på reisen

Ekspedisjonen vil bli dokumentert underveis, og produksjonsselskapet Vinterfilm vil jobbe for å skape en dokumentar eller TV-serie om turen. Hvis jeg fullfører, blir jeg den første nordmannen som gjennomfører en slik tur. Sammen håper Vinterfilm og jeg å nå ut til enda flere med det viktige budskapet om mental helse!

Hvis du vil følge meg underveis på turen kan du gjøre det på Instagram.

Alle pengene som samles inn, går direkte til Mental Helse Ungdom. Jeg håper du vil bidra – enten ved å bidra økonomisk eller ved å dele denne spleisen med ditt nettverk. Tusen takk!




henter ut gps data fra garmin, og poster på facebook med kart hvor fredrik er i verden
hans garmin side er: https://share.garmin.com/fedda

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

