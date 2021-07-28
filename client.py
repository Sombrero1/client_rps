import random
import threading
import time
import aiohttp
import asyncio
API_HOST = "172.19.0.4"
API_PORT = 4567
RPS = 2
loop = asyncio.get_event_loop()

async def request(body):
    async with aiohttp.ClientSession() as session:
        async with session.post(f"http://{API_HOST}:{API_PORT}/send", json=body) as response:
            pass

async def per_for_second(rps):
    bodys = []
    for _ in range(rps):
        body = {'body':'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa!'
                }
        bodys.append(body)

    tasks = [asyncio.create_task(request(bodys[i])) for i in range(rps)]
    await asyncio.gather(*tasks)

def start(rps):
    while True:
        print(threading.activeCount())
        if threading.activeCount() < 5:
            asyncio.run_coroutine_threadsafe(per_for_second(rps), loop)
        deadline = time.monotonic() + 1
        while time.monotonic() < deadline:
            pass

thread = threading.Thread(target=start, args=(RPS,))
thread.start()
loop.run_forever()
