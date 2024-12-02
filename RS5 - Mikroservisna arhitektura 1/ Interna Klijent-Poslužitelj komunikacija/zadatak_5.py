# 5.zadatak
"""
Nadogradite poslužitelj iz prethodnog zadatka na način da podržava i POST metodu na putanji /narudzbe .
Ova ruta prima JSON podatke o novoj narudžbu u sljedećem obliku. Za početak predstavite da je svaka
narudžba jednostavna i sadrži samo jedan proizvod i naručenu količinu:

Handler korutina ove metode mora provjeriti postoji li proizvod s traženim ID-em unutar liste proizvodi .
Ako ne postoji, vratite odgovor s statusom 404 i porukom {'error': 'Proizvod s traženim ID-em ne
postoji'} . Ako proizvod postoji, dodajte novu narudžbu u listu narudžbi i vratite odgovor s nadopunjenom
listom narudžbi u JSON formatu i prikladnim statusnim kodom.
Listu narudžbi definirajte globalno, kao praznu listu.
Vaš konačni poslužitelj mora sadržavati 3 rute: /proizvodi , /proizvodi/{id} i /narudzbe .
Testirajte poslužitelj na sve slučajeve kroz klijentsku sesiju unutar main korutine iste skripte.
"""

from aiohttp import web
from aiohttp.web import AppRunner
import asyncio, aiohttp

# Popis proizvoda
proizvodi = [
    {"id": 1, "naziv": "Laptop", "cijena": 5000},
    {"id": 2, "naziv": "Miš", "cijena": 100},
    {"id": 3, "naziv": "Tipkovnica", "cijena": 200},
    {"id": 4, "naziv": "Monitor", "cijena": 1000},
    {"id": 5, "naziv": "Slušalice", "cijena": 50}
]

narudzbe = []

async def get_proizvodi(request):
    proizvodi_id = request.match_info.get('id')

    if proizvodi_id is None:
        return web.json_response(proizvodi, status=200)
    
    for proizvod in proizvodi:
        if proizvod['id'] == int(proizvodi_id):
            return web.json_response(proizvod, status=200)
    return web.json_response({'error': 'Proizvod s traženim ID-em ne postoji'}, status=404)

async def post_narudzba(request):
    narudzba_data = await request.json()
    proizvod_id = narudzba_data.get("proizvod_id")
    kolicina = narudzba_data.get("kolicina")

    for proizvod in proizvodi:
        if proizvod["id"] == proizvod_id:
            narudzba = {"proizvod_id": proizvod_id, "kolicina": kolicina}
            narudzbe.append(narudzba)
            return web.json_response(narudzbe, status=200)

    return web.json_response({'error': 'Proizvod s traženim ID-em ne postoji'}, status=404)

app = web.Application()
app.router.add_get('/proizvodi', get_proizvodi)
app.router.add_get('/proizvodi/{id}', get_proizvodi)
app.router.add_post('/narudzbe', post_narudzba)

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

        narudzba = {"proizvod_id": 2, "kolicina": 3}
        rezultat = await session.post('http://localhost:8081/narudzbe', json=narudzba)
        rezultat_dict = await rezultat.json()
        print("Narudžbe nakon dodavanja:", rezultat_dict)

        narudzba = {"proizvod_id": 6, "kolicina": 2}
        rezultat = await session.post('http://localhost:8081/narudzbe', json=narudzba)
        rezultat_dict = await rezultat.json()
        print("Narudžbe nakon dodavanja nepostojećeg proizvoda:", rezultat_dict)

asyncio.run(main())
