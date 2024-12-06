from aiohttp import web
import asyncio
import aiohttp

async def fetch_cat_facts(amount):
    url = f"https://catfact.ninja/facts?limit={amount}"
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return await response.json()
        
async def handle_cats(request):
    amount = int(request.match_info.get("amount", 30))
    facts = await fetch_cat_facts(amount)
    return web.json_response(facts)
    
app = web.Application()
app.router.add_get('/cats', handle_cats)
app.router.add_get('/cat/{amount}', handle_cats)

if __name__ == "__main__":
    web.run_app(app, port=8086)