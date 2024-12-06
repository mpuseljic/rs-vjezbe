import aiohttp
import asyncio
import time

async def fetch_service(url, port):
    async with aiohttp.ClientSession() as session:
        async with session.get(f"http://{url}:{port}/pozdrav") as response:
            return await response.json()

async def main():
    url = "localhost"
    ports = [8081, 8082]

    print("Sekvencijalno slanje zahtjeva...")
    start_time = time.time()
    service1_response = await fetch_service(url, 8081)
    print(f"Odgovor mikroservisa 1: {service1_response}")
    service2_response = await fetch_service(url, 8082)
    print(f"Odgovor mikroservisa 2: {service2_response}")
    end_time = time.time()
    print(f"Vrijeme izvršavanja (sekvencijalno): {end_time - start_time:.2f} sekundi\n")

    print("Konkurentno slanje zahtjeva...")
    start_time = time.time()
    tasks = [fetch_service(url, port) for port in ports]
    results = await asyncio.gather(*tasks)
    print(results)
    end_time = time.time()
    print(f"Vrijeme izvršavanja (konkurentno): {end_time - start_time:.2f} sekundi")

if __name__ == "__main__":
    asyncio.run(main())