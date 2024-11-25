"""
Definirajte korutinu fetch_users koja će slati GET zahtjev na JSONPlaceholder API na URL-u:
https://jsonplaceholder.typicode.com/users. Morate simulirate slanje 5 zahtjeva konkurentno
unutar main korutine. Unutar main korutine izmjerite vrijeme izvođenja programa, a rezultate
pohranite u listu odjedanput koristeći asyncio.gather funkciju. Nakon toga koristeći map funkcije ili
list comprehension izdvojite u zasebne 3 liste: samo imena korisnika, samo email adrese korisnika i
samo username korisnika. Na kraju main korutine ispišite sve 3 liste i vrijeme izvođenja programa.
"""


import asyncio
import aiohttp
import time

async def fetch_users(session):
    response = await session.get("https://jsonplaceholder.typicode.com/users")
    user_dict = await response.json()
    return user_dict
    
async def main():
    start = time.time()
    async with aiohttp.ClientSession() as session:
        korisnici_korutine = [fetch_users(session) for _ in range(5)]
        korisnik_rezultat = await asyncio.gather(*korisnici_korutine)
        
    korisnici = [korisnik for korisnici in korisnik_rezultat for korisnik in korisnici]
        
    ime = [korisnik['name'] for korisnik in korisnici]
    email = [korisnik['email'] for korisnik in korisnici]
    username = [korisnik['username'] for korisnik in korisnici]
        
    end = time.time()
    
    print("Imena: ", ime)
    print("Email: ", email)
    print("Username: ", username)
    print(f"\nIzvršavanje programa traje {end - start:.2f} sekundi.")
    
        
asyncio.run(main())