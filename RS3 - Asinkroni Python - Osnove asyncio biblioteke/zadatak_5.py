"""
Definirajte korutinu secure_data koja će simulirati enkripciju osjetljivih podataka. Kako se u
praksi enkripcija radi na poslužiteljskoj strani, korutina će simulirati enkripciju podataka u trajanju od 3
sekunde. Korutina prima kao argument rječnik osjetljivih podataka koji se sastoji od ključeva prezime,
broj_kartice i CVV. Definirajte listu s 3 rječnika osjetljivih podataka. Pohranite u listu zadaci kao u
prethodnom zadatku te pozovite zadatke koristeći asyncio.gather(). Korutina secure_data mora za
svaki rječnik vratiti novi rječnik u obliku: {'prezime':prezime , 'broj_kartice': 'enkriptirano',
'CVV': 'enkriptirano'}. Za fake enkripciju koristite funkciju hash(str) koja samo vraća hash
vrijednost ulaznog stringa.
"""

import asyncio

async def secure_data(rjecnik):
    print("Enkriptiram podatke...")
    await asyncio.sleep(3)
    
    podaci = {
        'prezime':rjecnik['prezime'],
        'broj_kartice':hash(rjecnik['broj_kartice']),
        'CVV':hash(rjecnik['CVV'])
    }
        
    return podaci

async def main():
    lista = [
        {'prezime':"Ivić", 'broj_kartice':"234252253", 'CVV':"123"},
        {'prezime':"Marić", 'broj_kartice':"654656435", 'CVV':"654"},
        {'prezime':"Marković", 'broj_kartice':"75643634", 'CVV':"765"} 
    ]
    
    zadaci = [asyncio.create_task(secure_data(rjecnik)) for rjecnik in lista]
    print(await asyncio.gather(*zadaci))
    
asyncio.run(main())

        
    
    