"""
Definirajte dvije korutine koje će simulirati dohvaćanje podataka s weba. Prva korutina neka vrati
listu proizvoljnih rječnika (npr. koji reprezentiraju podatke o korisnicima) nakon 3 sekunde, a druga
korutina neka vrati listu proizvoljnih rječnika (npr. koji reprezentiraju podatke o proizvodima) nakon 5
sekundi. Korutine pozovite konkurentno korištenjem asyncio.gather() i ispišite rezultate. Program
se mora izvršavati ~5 sekundi.
"""
import asyncio

async def fetch_api_1():
    print("Dohvaćam podake o korisnicima...")
    korisnici = [
        {"ime": "Ivan", "prezime": "Ivić", "godina_rodenja": 2000},
        {"ime": "Marko", "prezime": "Marković", "godina_rodenja": 1990},
        {"ime": "Ana", "prezime": "Anić", "godina_rodenja": 2003},
        {"ime": "Petra", "prezime": "Petrić", "godina_rodenja": 2001}
        ]
    await asyncio.sleep(3)
    print("Podaci o korisnicima dohvaćeni...")
    return korisnici

async def fetch_api_2():
    print("Dohvaćam podake o proizvodima...")
    proizvodi = [
        {"naziv": "Mlijeko", "cijena": 5.00},
        {"naziv": "Kruh", "cijena": 3.00},
        {"naziv": "Jabuka", "cijena": 2.00},
        {"naziv": "Sir", "cijena": 4.00 }
        ]
    await asyncio.sleep(5)
    print("Podaci o proizvodima dohvaćeni...")
    return proizvodi

async def main():
    podaci_1, podaci_2 = await asyncio.gather(fetch_api_1(), fetch_api_2())
    
    print(f"Podaci o korisnicima: {podaci_1}")
    print(f"Podaci o proizvodima: {podaci_2}")
    
asyncio.run(main())

    