from aiohttp import web
import asyncio
import aiohttp

async def check_fact(facts):
    filtered_facts = []
    for fact in facts:
        if 'cat' in fact.lower():
            filtered_facts.append(fact)
    return filtered_facts

async def handle_facts(request):
    data = await request.json()
    facts = data.get("facts", [])
    filtered_facts = await check_fact(facts)
    return web.json_response({"filtirane činjenice": filtered_facts})

app = web.Application()
app.router.add_post('/facts', handle_facts)

if __name__ == "__main__":
    web.run_app(app, port=8087)
