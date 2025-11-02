import asyncio
import aiohttp
import time

async def fetch_url(session, url):
    start_time = time.time()
    async with session.get(url) as response:
        elapsed = time.time() - start_time
        print(f"✅ Fetched {url} (Delay: 2s) | Status: {response.status} | Total Time: {elapsed:.2f}s")

async def main():
    urls = ["https://httpbin.org/delay/2"] * 3 
    async with aiohttp.ClientSession() as session:
        tasks = [fetch_url(session, url) for url in urls]
        print(f"🚀 Starting {len(urls)} concurrent fetch tasks at {time.strftime('%X')}...")
        await asyncio.gather(*tasks) #unpacking
        print("🎉 All network requests are complete.")

if __name__ == "__main__":
    asyncio.run(main())