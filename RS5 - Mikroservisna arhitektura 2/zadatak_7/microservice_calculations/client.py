import aiohttp
import asyncio

async def fetch_zbroj(session, data_json):
    response = await session.post('http://localhost:8083/zbroj', json=data_json)
    return await response.json()

async def fetch_umnozak(session, data_json):
    response = await session.post('http://localhost:8084/umnozak', json=data_json)
    return await response.json()

async def fetch_kolicnik(session, data_json):
    response = await session.post('http://localhost:8085/kolicnik', json=data_json)
    return await response.json()

async def main():
    print("Pokrećem main korutinu")
    data = [i for i in range(1, 11)]
    data_json = {"podaci": data}  
    async with aiohttp.ClientSession() as session:
        microservice_1, microservice_2 = await asyncio.gather(
            fetch_zbroj(session, data_json),
            fetch_umnozak(session, data_json)
        )
        
        zbroj = microservice_1.get("zbroj")
        umnozak = microservice_2.get("umnozak")

        kolicnik_data = {"zbroj": zbroj, "umnozak": umnozak}
        
        microservice_3 = await fetch_kolicnik(session, kolicnik_data)
        kolicnik = microservice_3.get("kolicnik")

        # Ispisujemo rezultate
        print(f"Zbroj: {zbroj}")
        print(f"Umnozak: {umnozak}")
        print(f"Kolicnik: {kolicnik}")

if __name__ == "__main__":
    asyncio.run(main())
