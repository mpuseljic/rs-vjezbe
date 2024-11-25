import asyncio
import requests
import aiohttp
import time

async def get_cat_fact(session, i):
    response = await session.get("https://catfact.ninja/fact")
    fact_dict = await response.json()
    print(f"{i + 1}: {fact_dict['fact']}")
    return fact_dict['fact']
    
async def main():
    start = time.time()
    async with aiohttp.ClientSession() as session:
        cat_fact_tasks = [asyncio.create_task(get_cat_fact(session, i)) for i in range(5)]
        actual_cat_facts = await asyncio.gather(*cat_fact_tasks)
              
    end = time.time()
    print(f"\nIzvršavanje programa traje {end - start:.2f} sekundi.")
        
asyncio.run(main())

