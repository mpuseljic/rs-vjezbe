"""
3. Definirajte korutinu get_dog_fact koja dohvaća činjenice o psima sa DOG API.
Korutina get_dog_fact neka dohvaća činjenicu o psima na URL-u: https://dogapi.dog/api/v2/facts.
Nakon toga, definirajte korutinu get_cat_fact koja dohvaća činjenicu o mačkama slanjem zahtjeva na
URL: https://catfact.ninja/fact.
Istovremeno pohranite rezultate izvršavanja ovih Taskova koristeći asyncio.gather(*dog_facts_tasks,
*cat_facts_tasks) funkciju u listu dog_cat_facts, a zatim ih koristeći list slicing odvojite u dvije liste
obzirom da znate da je prvih 5 činjenica o psima, a drugih 5 o mačkama.
Na kraju, definirajte i treću korutinu mix_facts koja prima liste dog_facts i cat_facts i vraća novu
listu koja za vrijednost indeksa i sadrži činjenicu o psima ako je duljina činjenice o psima veća od duljine
činjenice o mačkama na istom indeksu, inače vraća činjenicu o mački. Na kraju ispišite rezultate filtriranog
niza činjenica. Liste možete paralelno iterirati koristeći zip funkciju, npr. for dog_fact, cat_fact in
zip(dog_facts, cat_facts).

"""
import aiohttp
import asyncio
import time

async def get_dog_fact(session):
    response = await session.get("https://dogapi.dog/api/v2/facts")
    dog_dict = await response.json()
    return dog_dict['data'][0]['attributes']['body']

async def get_cat_fact(session):
    response = await session.get("https://catfact.ninja/fact")
    fact_dict = await response.json()
    return fact_dict['fact']

async def mix_facts(dog_facts, cat_facts):
    nova_lista = []
    
    for dog_fact, cat_fact in zip(dog_facts, cat_facts):
        if len(dog_fact) > len(cat_fact):
            nova_lista.append(dog_fact)
        else:
            nova_lista.append(cat_fact)
            
    return nova_lista
               
async def main():
    start = time.time()
    async with aiohttp.ClientSession() as session:
        dog_fact_korutine = [get_dog_fact(session) for _ in range(5)]
        cat_fact_korutine = [get_cat_fact(session) for _ in range(5)]
        facts = await asyncio.gather(*dog_fact_korutine, *cat_fact_korutine)
        
        slicing_dog_facts = facts[:5]
        slicing_cat_facts = facts[5:]
        
        mixane_cinjenice = await mix_facts(slicing_dog_facts, slicing_cat_facts)
        
    end = time.time()
 
    print("Činjenice o psima: ", slicing_dog_facts)
    print("Činjenice o mačkama: ", slicing_cat_facts)
    print("Mixane činjenice o psima i mačkama: ", mixane_cinjenice)
    
    print(f"\nIzvršavanje programa traje {end - start:.2f} sekundi.")
    
    
asyncio.run(main())