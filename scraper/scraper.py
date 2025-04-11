import asyncio
import sys

import aiohttp
from bs4 import BeautifulSoup
import json
import aiofiles
from datetime import datetime


async def save_offers(offers):
    if not offers:
        return

    for offer in offers:
        filename = f"{offers_dir}/{datetime.now().strftime('%Y%m%d_%H%M')}.json"

        async with aiofiles.open(filename, 'w') as f:
            await f.write(json.dumps(offer, indent=2, ensure_ascii=False))


async def fetch():
    async with aiohttp.ClientSession(connector=aiohttp.TCPConnector(ssl=False)) as session:
        async with session.get("https://www.avito.ru/sankt-peterburg/kvartiry/sdam?cd=1") as response:
            if response.status == 200:
                html = await response.text()
                soup = BeautifulSoup(html, 'html.parser')
                return [
                    {
                        'title': offer.select_one('[itemprop="name"]').get_text(strip=True),
                        'price': offer.select_one('[itemprop="price"]').get('content'),
                        'address': offer.select_one('[data-marker="item-address"]').get_text(strip=True),
                        'description': offer.select_one('[itemprop="description"]').get('content'),
                        'url': "https://www.avito.ru" + offer.select_one('a[itemprop="url"]')['href'],
                        'time': datetime.now().isoformat()
                    }
                    for offer in soup.select('[data-marker="item"]')
                ]
            else:
                print(f"Response status: {response.status}")
    return []


async def main():
    while True:
        offers = await fetch()
        await save_offers(offers)
        await asyncio.sleep(check_time)


if __name__ == "__main__":
    check_time = 600 # в секундах
    offers_dir = "artifacts/avito"
    if len(sys.argv) > 1:
        check_time = int(sys.argv[1])
        if len(sys.argv) > 2:
            offers_dir = sys.argv[2]
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\nScraper stopped")