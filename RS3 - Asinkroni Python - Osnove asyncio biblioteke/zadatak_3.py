"""
Definirajte korutinu autentifikacija() koja će simulirati autentifikaciju korisnika na
poslužiteljskoj strani. Korutina kao ulazni parametar prima rječnik koji opisuje korisnika, a sastoji se
od ključeva korisnicko_ime, email i lozinka. Unutar korutine simulirajte provjeru korisničkog
imena na način da ćete provjeriti nalaze li se par korisnicko_ime i email u bazi korisnika. Ova
provjera traje 3 sekunde.
baza_korisnika = [
{'korisnicko_ime': 'mirko123', 'email': 'mirko123@gmail.com'},
{'korisnicko_ime': 'ana_anic', 'email': 'aanic@gmail.com'},
{'korisnicko_ime': 'maja_0x', 'email': 'majaaaaa@gmail.com'},
{'korisnicko_ime': 'zdeslav032', 'email': 'deso032@gmail.com'}
]
Ako se korisnik ne nalazi u bazi, vratite poruku "Korisnik {korisnik} nije pronađen."
Ako se korisnik nalazi u bazi, potrebno je pozvati vanjsku korutinu autorizacija() koja će simulirati
autorizaciju korisnika u trajanju od 2 sekunde. Funkcija kao ulazni parametar prima rječnik korisnika iz baze
i lozinku proslijeđenu iz korutine autentifikacija(). Autorizacija simulira dekripciju lozinke (samo
provjerite podudaranje stringova) i provjeru s lozinkom iz baze_lozinka. Ako su lozinke jednake, korutine
vraća poruku "Korisnik {korisnik}: Autorizacija uspješna.", a u suprotnom "Korisnik
{korisnik}: Autorizacija neuspješna.".
baza_lozinka = [
{'korisnicko_ime': 'mirko123', 'lozinka': 'lozinka123'},
{'korisnicko_ime': 'ana_anic', 'lozinka': 'super_teska_lozinka'},
{'korisnicko_ime': 'maja_0x', 'email': 's324SDFfdsj234'},
{'korisnicko_ime': 'zdeslav032', 'email': 'deso123'}
]
Korutinu autentifikacija() pozovite u main() funkciji s proizvoljnim korisnikom i lozinkom.
"""

import asyncio

async def autorizacija(korisnik, lozinka):
    print("Provodim autorizaciju....")
    await asyncio.sleep(2)
    baza_lozinka = [
        {'korisnicko_ime': 'mirko123', 'lozinka': 'lozinka123'},
        {'korisnicko_ime': 'ana_anic', 'lozinka': 'super_teska_lozinka'},
        {'korisnicko_ime': 'maja_0x', 'lozinka': 's324SDFfdsj234'},
        {'korisnicko_ime': 'zdeslav032', 'lozinka': 'deso123'}
    ]
    
    for password in baza_lozinka:
        if password['korisnicko_ime'] == korisnik['korisnicko_ime'] and password['lozinka'] == lozinka:
            return f"Korisnik {korisnik}: Autorizacija uspješna."
        
    return  f"Korisnik {korisnik}: Autorizacija neuspješna."
    
    
async def autentifikacija(korisnik):
    baza_korisnika = [
    {'korisnicko_ime': 'mirko123', 'email': 'mirko123@gmail.com'},
    {'korisnicko_ime': 'ana_anic', 'email': 'aanic@gmail.com'},
    {'korisnicko_ime': 'maja_0x', 'email': 'majaaaaa@gmail.com'},
    {'korisnicko_ime': 'zdeslav032', 'email': 'deso032@gmail.com'}
    ]
    print("Provodim autentifikaciju....")
    
    await asyncio.sleep(3)
    
    for korisnici in baza_korisnika:
        if korisnici['korisnicko_ime'] == korisnik['korisnicko_ime'] and korisnici['email'] == korisnik['email']:
            print(f"Korisnik {korisnik} se nalazi u bazi korisnika.") 
            return await autorizacija(korisnici, korisnik['lozinka'])
        
    return f"Korisnik {korisnik} nije pronađen."
    
    
async def main():
    korisnik = {'korisnicko_ime': 'mirko123', 'email': 'mirko123@gmail.com', 'lozinka': 'lozinka123'}
    provjera = await autentifikacija(korisnik)
    print(provjera)
    
asyncio.run(main())
    