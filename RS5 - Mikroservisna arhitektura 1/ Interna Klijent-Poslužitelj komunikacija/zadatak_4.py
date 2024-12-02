# 4.zadatak
"""
Definirajte aiohttp poslužitelj koji radi na portu 8081 . Poslužitelj mora imati dvije rute: /proizvodi i
/proizvodi/{id} . Prva ruta vraća listu proizvoda u JSON formatu, a druga rutu vraća točno jedan proizvod
prema ID-u. Ako proizvod s traženim ID-em ne postoji, vratite odgovor s statusom 404 i porukom
{'error': 'Proizvod s traženim ID-em ne postoji'} .
"""

from aiohttp import web
from aiohttp.web import AppRunner
import asyncio, aiohttp

proizvodi = [
{"id": 1, "naziv": "Laptop", "cijena": 5000},
{"id": 2, "naziv": "Miš", "cijena": 100},
{"id": 3, "naziv": "Tipkovnica", "cijena": 200},
{"id": 4, "naziv": "Monitor", "cijena": 1000},
{"id": 5, "naziv": "Slušalice", "cijena": 50}
]

async def get_proizvodi(request):
    proizvodi_id = request.match_info.get('id')

    if proizvodi_id is None:
        return web.json_response(proizvodi, status=200)
    
    for proizvod in proizvodi:
        if proizvod['id'] == int(proizvodi_id):
            return web.json_response(proizvod, status=200)
    return web.json_response({'error': 'Proizvod s traženim ID-em ne postoji'}, status=404)


app = web.Application()
app.router.add_get('/proizvodi', get_proizvodi)
app.router.add_get('/proizvodi/{id}', get_proizvodi)

async def start_server():
    runner = AppRunner(app)
    await runner.setup()
    site = web.TCPSite(runner, 'localhost', 8081)
    await site.start()
    print("Poslužitelj sluša na http://localhost:8081")
    
async def main():
    await start_server() 
    async with aiohttp.ClientSession() as session: 
        rezultat = await session.get('http://localhost:8081/proizvodi')
        rezultat_dict = await rezultat.json() 
        print(rezultat_dict) 
        rezultat = await session.get('http://localhost:8081/proizvodi/2')
        rezultat_dict = await rezultat.json() 
        print(rezultat_dict)
        rezultat = await session.get('http://localhost:8081/proizvodi/6')
        rezultat_dict = await rezultat.json() 
        print(rezultat_dict)      

asyncio.run(main()) 