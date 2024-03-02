
async def fetch_alls(s, urls):
    tasks = []
    for url in urls:
        task = asyncio.create_task(fetch(s, url))
        tasks.append(task)
    res = await asyncio.gather(*tasks)
    return res

async def main():
    urls = range(1, 38)
    async with aiohttp.ClientSession() as session:
        htmls = await fetch_alls(session, urls)
        return htmls


asyncio.run(main())
