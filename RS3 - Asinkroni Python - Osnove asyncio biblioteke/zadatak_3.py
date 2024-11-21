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
    