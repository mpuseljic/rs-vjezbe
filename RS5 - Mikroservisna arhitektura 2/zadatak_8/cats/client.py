import aiohttp
import asyncio

async def fetch_cat_facts(session, amount):
    url = f'http://localhost:8086/cat/{amount}'
    async with session.get(url) as response:
        return await response.json()

async def check_facts(session, facts):
    url = 'http://localhost:8087/facts'
    json_data = {"facts": facts}
    async with session.post(url, json=json_data) as response:
        return await response.json()

async def main():
    amount = 30
    async with aiohttp.ClientSession() as session:
        cat_facts = await fetch_cat_facts(session, amount)
        print("Činjenice:", cat_facts)
        
        if 'data' in cat_facts:
            facts_to_check = [fact['fact'] for fact in cat_facts['data']]
            filtered_facts = await check_facts(session, facts_to_check)
            print("Filtrirane činjenice:", filtered_facts)
        else:
            print("Greška pri dohvaćanju činjenica")


if __name__ == "__main__":
    asyncio.run(main())
