import asyncio
import aiohttp


async def fetch_url(session: aiohttp.ClientSession,url: str) -> dict:
    try:
        async with session.get(url) as response:
            body =  await response.text()
            return {
                "url": url,
                "status": response.status,
                "body": body
            }
    except Exception as e:
        return {
            "url": url,
            "status": "Error",
            "body": str(e)
        }


async def send_data(session: aiohttp.ClientSession, url: str, data: dict) -> dict:
    try:
        async with session.post(url, json=data) as response:
            body = await response.text()
            return {
                "url": url,
                "status": response.status,
                "body": body
            }
    except Exception as e:
        return {
            "url": url,
            "status": "Error",
            "body": str(e)
        }


async def update_data(session: aiohttp.ClientSession, url: str, data: dict) -> dict:
    try:
        async with session.put(url, json=data) as response:
            body = await response.text()
            return {
                "url": url,
                "status": response.status,
                "body": body
            }
    except Exception as e:
        return {
            "url": url,
            "status": "Error",
            "body": str(e)
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




