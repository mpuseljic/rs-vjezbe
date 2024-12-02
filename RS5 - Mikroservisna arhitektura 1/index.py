import asyncio
import aiohttp
from aiohttp import web # Server API - za poslužitelj


app = web.Application()


def handler_function(request):
    data = {'ime':'Ivo', 'prezime':'ivić', 'godine': 25}
    return web.json_response(data)

async def post_function(request):
    data = await request.json()
    print(data)
    return web.json_response(data)

#1.zadatak
"""
Definirajte aiohttp poslužitelj koji radi na portu 8081 koji na putanji /proizvodi vraća listu proizvoda u
JSON formatu. Svaki proizvod je rječnik koji sadrži ključeve naziv , cijena i količina . Pošaljite zahtjev na
adresu http://localhost:8080/proizvodi koristeći neki od HTTP klijenata ili curl i provjerite odgovor.
"""

proizvodi = [
        {'naziv':'Kruh', 'cijena':2.00, 'kolicina': 2},
        {'naziv':'Mlijeko', 'cijena': 3.00, 'kolicina': 3},
        {'naziv':'Sir', 'cijena': 4.00, 'kolicina': 4},       
    ]
def get_proizvodi(request):
    return web.json_response(proizvodi)
    
    
# 2. zadatak
async def post_proizvodi(request):
    proizvodi = await request.json()

    return web.json_response(proizvodi)
    
    
    
app.router.add_get("/", handler_function)
app.router.add_post("/", post_function)
app.router.add_get("/proizvodi", get_proizvodi)
app.router.add_post("/proizvodi", post_proizvodi)

web.run_app(app, host="localhost", port=8080)


