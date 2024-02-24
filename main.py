import asyncio
import aiohttp as aiohttp
import requests
from bs4 import BeautifulSoup


HOME_URL = "https://amazon.eg"
AMAZON_PRODUCT_URL_AR = "https://www.amazon.eg/s?bbn=18018102031&rh=n%3A21832958031&fs=true&language=ar_AE&ref=lp_21832958031_sar"
AMAZON_PRODUCT_URL_EN = "https://www.amazon.eg/s?bbn=18018102031&rh=n%3A21832958031&fs=true&language=en_AE&ref=lp_21832958031_sar"


# async def scrape(url):
#     response = requests.get(url)
#     soup = BeautifulSoup(response.content, 'html.parser')
#     products = soup.find_all('div', class_='a-section a-spacing-base')
#     print(products[0])

async def scrape(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            body = await resp.text()
            soup = BeautifulSoup(body, 'html.parser')
            print(body)

# async def fetch(url):
#     # Create HTTP session
#     async with aiohttp.ClientSession() as session:
#         # Make GET request using session
#         async with session.get(url) as response:
#             # Return text content
#             return await response.text()


asyncio.run(scrape(AMAZON_PRODUCT_URL_EN))
