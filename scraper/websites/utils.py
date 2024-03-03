from fake_useragent import UserAgent
from bs4 import BeautifulSoup
import asyncio
import aiohttp as aiohttp
import re


NB_PROXIES_ALTERNATE = 20
NB_TRIES_SAME_PAGE = 10

BRANDS_EN = ["Oraimo", "Xiaomi", "HUAWEI", "Joyroom", "SAMSUNG", "Honor", "Amazfit", "JOYROOM", "Apple"]
COLORS_EN = ["Beige", "Black", "Blue", "Brown", "Gold", "Green", "Grey", "Off-White", "Orange", "Pink", "Purple", "Red", "Silver", "Turquoise", "White", "Yellow"]

BRANDS_AR = ["اورايمو", "شاومي", "هواوى" , "جوي رووم", "سامسونج", "اونر", "امازفيت", "جوي رووم", "ابل"]
COLORS_AR = ["بيج", "أسود", "أزرق", "بني", "ذهبي", "متعدد", "أوف ويت", "برتقالي", "زهري", "بنفسجي", "أحمر", "فضي", "فبروزي", "أبيض" ,"أصفر", "أخضر" ,"رمادي"]


async def fetch_alls(s, urls, fetch_function):
    tasks = []
    for url in urls:
        task = asyncio.create_task(fetch_function(s, url))
        tasks.append(task)
    res = await asyncio.gather(*tasks)
    return res
