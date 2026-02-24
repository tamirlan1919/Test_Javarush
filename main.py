import asyncio
import aiohttp


async def fetch_url(session: aiohttp.ClientSession,url: str) -> dict:
    async with session.get(url) as response:
        body =  await response.text()
        return {
            "url": url,
            "status": response.status,
            "body": body
        }


async def main():
    urls = [
        "https://jsonplaceholder.typicode.com/posts/1",
        "https://jsonplaceholder.typicode.com/posts/2",
        "https://jsonplaceholder.typicode.com/posts/3"
    ]
    async with aiohttp.ClientSession() as session:
        tasks = [fetch_url(session, url) for url in urls]
        results = await asyncio.gather(*tasks)

    for result in results:
        print(f"URL: {result['url']}, Status: {result['status']}, Body: {result['body'][:100]}...")

asyncio.run(main())




