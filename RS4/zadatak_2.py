"""
Definirajte dvije korutine, od kojih će jedna služiti za dohvaćanje činjenica o mačkama koristeći
get_cat_fact korutinu koja šalje GET zahtjev na URL: https://catfact.ninja/fact. Izradite 20
Task objekata za dohvaćanje činjenica o mačkama te ih pozovite unutar main korutine i rezultate
pohranite odjednom koristeći asyncio.gather funkciju. Druga korutina filter_cat_facts ne šalje
HTTP zahtjeve, već mora primiti gotovu listu činjenica o mačkama i vratiti novu listu koja sadrži samo
one činjenice koje sadrže riječ "cat" ili "cats" (neovisno o velikim/malim slovima).
"""

import asyncio
import aiohttp
import time

async def get_cat_fact(session):
    response = await session.get("https://catfact.ninja/fact")
    fact_dict = await response.json()
    return fact_dict['fact']
    
async def filter_cat_facts(lista):
     return [fact for fact in lista if fact and ("cat" in fact.lower() or "cats" in fact.lower())]
    
    
async def main():
    start = time.time()
    
    async with aiohttp.ClientSession() as session:
        cat_fact_tasks = [asyncio.create_task(get_cat_fact(session)) for _ in range(5)]
        actual_cat_facts = await asyncio.gather(*cat_fact_tasks)
        
    filtered_facts = await filter_cat_facts(actual_cat_facts)

    
    end = time.time()
    print(actual_cat_facts)
    print("\nČinjenice koje sadrže riječ cat ili cats")
    print(filtered_facts)
    print(f"\nIzvršavanje programa traje {end - start:.2f} sekundi.")
    
asyncio.run(main())
    
