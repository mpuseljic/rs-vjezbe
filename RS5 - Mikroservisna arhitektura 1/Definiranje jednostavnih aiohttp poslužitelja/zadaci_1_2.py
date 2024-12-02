#1.zadatak
"""
Definirajte aiohttp poslužitelj koji radi na portu 8081 koji na putanji /proizvodi vraća listu proizvoda u
JSON formatu. Svaki proizvod je rječnik koji sadrži ključeve naziv , cijena i količina . Pošaljite zahtjev na
adresu http://localhost:8080/proizvodi koristeći neki od HTTP klijenata ili curl i provjerite odgovor.
"""

# 2.zadatak
"""
Nadogradite poslužitelj iz prethodnog zadatka na način da na istoj putanji /proizvodi prima POST zahtjeve
s podacima o proizvodu. Podaci se šalju u JSON formatu i sadrže ključeve naziv , cijena i količina .
Handler funkcija treba ispisati primljene podatke u terminalu, dodati novi proizvod u listu proizvoda i vratiti
odgovor s novom listom proizvoda u JSON formatu.
"""

from aiohttp import web

app = web.Application()

proizvodi = [
        {'naziv':'Kruh', 'cijena':2.00, 'kolicina': 2},
        {'naziv':'Mlijeko', 'cijena': 3.00, 'kolicina': 3},
        {'naziv':'Sir', 'cijena': 4.00, 'kolicina': 4},       
    ]
async def get_proizvodi(request):
    return web.json_response(proizvodi)

async def post_proizvodi(request):
    novi_proizvod = await request.json()
    proizvodi.append(novi_proizvod)
    
    return web.json_response(proizvodi)

app.router.add_get("/proizvodi", get_proizvodi)
app.router.add_post("/proizvodi", post_proizvodi)

web.run_app(app, host="localhost", port=8080)





