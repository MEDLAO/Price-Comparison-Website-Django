import asyncio
from pyppeteer import launch
from fake_useragent import UserAgent


HOME_PAGE_URL_JUMIA = "https://www.jumia.com.eg/"
JUMIA_PRODUCT_URL_AR = "https://www.jumia.com.eg/ar/catalog/?q=smart+watches"
JUMIA_PRODUCT_URL_EN = "https://www.jumia.com.eg/catalog/?q=smart+watches"
NB_PAGES_JUMIA_EG = 50


async def scrape(url):
    ua = UserAgent()
    browser = await launch()
    page = await browser.newPage()
    user_agent = ua.random
    await page.setUserAgent(user_agent)
    await page.goto(url)
    content = await page.content()
    await browser.close()
    return content

async def main_noon_jumia():
    content = await scrape('https://www.jumia.com.eg/catalog/?q=smart+watch')
    print(content)

asyncio.run(main())