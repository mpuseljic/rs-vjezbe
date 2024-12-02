# 3. zadatak
"""
Definirajte poslužitelj koji sluša na portu 8082 i na putanji /punoljetni vraća listu korisnika starijih od 18
godina. Svaki korisnik je rječnik koji sadrži ključeve ime i godine . Pošaljite zahtjev na adresu
http://localhost:8082/stariji_korisnici i provjerite odgovor. Novu listu korisnika definirajte koristeći
funkciju filter ili list comprehension .
"""
from aiohttp import web

app = web.Application()

korisnici = [
{'ime': 'Ivo', 'godine': 25},
{'ime': 'Ana', 'godine': 17},
{'ime': 'Marko', 'godine': 19},
{'ime': 'Maja', 'godine': 16},
{'ime': 'Iva', 'godine': 22}
]


def get_punoljetni(request):
    stariji_korisnici = [korisnik for korisnik in korisnici if korisnik["godine"] > 18]
    return web.json_response(stariji_korisnici)


app.router.add_get("/stariji_korisnici", get_punoljetni)

web.run_app(app, host="localhost", port=8082)

