import aiohttp
import asyncio
import os
import sys


async def img_install(session, url, path):
    try:
        async with session.get(url) as response:
            if response.status == 200:
                with open(path, 'wb') as f:
                    while True:
                        chunk = await response.content.read(1024)
                        if not chunk:
                            break
                        f.write(chunk)
            else:
                print(f"Response status: {response.status}")
    except Exception as e:
        print(f"Error: {e}")


async def main(img_num, img_dir):
    url = "https://picsum.photos/200"

    async with aiohttp.ClientSession(connector=aiohttp.TCPConnector(ssl=False)) as session:
        tasks = []
        for i in range(img_num):
            path = os.path.join(img_dir, f"image_{i}.png")
            tasks.append(img_install(session, url, path))

        await asyncio.gather(*tasks)

if __name__ == "__main__":
    img_num = 10
    img_dir = "artifacts/img"
    if len(sys.argv) > 1:
        img_num = int(sys.argv[1])
        if len(sys.argv) > 2:
            img_dir = sys.argv[2]

    asyncio.run(main(img_num, img_dir))
