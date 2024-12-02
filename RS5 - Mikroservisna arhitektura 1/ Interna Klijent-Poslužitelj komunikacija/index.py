from aiohttp import web
from aiohttp.web import AppRunner
import asyncio, aiohttp

async def get_users(request):
    return web.json_response({'korisnici': ['Ivo', 'Ana', 'Marko', 'Maja', 'Iva', 'Ivan']})

app = web.Application()
app.router.add_get('/korisnici', get_users)

async def start_server():
    runner = AppRunner(app)
    await runner.setup()
    site = web.TCPSite(runner, 'localhost', 8080)
    await site.start()
    print("Poslužitelj sluša na http://localhost:8080")
    
async def main():
    await start_server() 
    async with aiohttp.ClientSession() as session: 
        rezultat = await session.get('http://localhost:8080/korisnici') 
        print(await rezultat.text()) 

asyncio.run(main()) 