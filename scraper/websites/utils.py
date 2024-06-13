import requests
from bs4 import BeautifulSoup
import asyncio
import re
import convert_numbers
from random import choice
from time import sleep
from random import randint
from fake_useragent import UserAgent


NB_PROXIES_ALTERNATE = 20
NB_TRIES_SAME_PAGE = 10

BRANDS_EN = [
    "Apple", "Samsung", "Huawei", "Sony", "Oppo", "Xiaomi", "Nokia", "Amazfit",
    "Garmin", "Fitbit", "Realme", "OnePlus", "Lenovo", "Honor", "Motorola", "Infinix",
    "Fossil", "Casio", "Rolex", "Hublot", "TAG Heuer", "Tissot", "Timex", "Seiko",
    "Citizen", "Diesel", "Emporio Armani", "Michael Kors", "Skagen", "Suunto",
    "Polar", "Withings", "Zepp", "Mobvoi", "Zeblaze", "Corn", "Joyroom", "Oraimo", "Kospet",
    "Redmi", "Cardoo", "Devia", "Generic", "Imilab", "Kieslect", "Mibro", "Tommy Hilfiger",
    "G-shock", "Guess", "Barbie"
]

BRANDS_AR = [
    "أبل", "سامسونج", "هواوي", "سوني", "أوبو", "شاومي", "نوكيا", "أمازفيت",
    "غارمين", "فيتبيت", "ريلمي", "ون بلس", "لينوفو", "هونر", "موتورولا", "إنفينيكس",
    "فوسيل", "كاسيو", "رولكس", "هوبلو", "تاغ هوير", "تيسو", "تايمكس", "سيكو",
    "سيتيزن", "ديزل", "إمبريو أرماني", "مايكل كورس", "سكان", "سنتو",
    "بولار", "ويذينجز", "زيب", "موبفوي", "زيبليز", "كورن", "جوي روم", "أورايمو", "كوسبت",
    "ريدمى", "كاردو", "ديفيا", "جينيريك", "إيمي لاب", "كيسليكت", "ميبرو", "تومي هيلفيغر",
    "جي-شوك", "جيس", "باربي"
]

COLORS_EN = [
    "Black", "White", "Red", "Green", "Blue", "Silver", "Orange", "Yellow",
    "Purple", "Pink", "Gold", "Brown", "Grey", "Beige", "Navy", "Maroon",
    "Turquoise", "Teal", "Olive", "Coral", "Lavender", "Peach", "Cyan", "Magenta",
    "Mystic Silver", "Natural Silver", "Mecha Gray", "Quiet Blue", "Performance Blue",
    "Ceramic White", "Graphite Grey", "Mica Silver", "Cyan Lake", "Rock Grey",
    "Midnight Black", "Light-Blue", "Blue-black", "Starlight", "Cyber Grey"
]

COLORS_AR = [
    "أسود", "أبيض", "أحمر", "أخضر", "أزرق", "فضي", "برتقالي", "أصفر",
    "أرجواني", "وردي", "ذهبي", "بني", "رمادي", "بيج", "كحلي", "ماروني",
    "فيروزي", "أخضر مزرق", "زيتوني", "مرجاني", "لافندر", "خوخي", "سماوي", "قرمزي",
    "فضي غامض", "فضي طبيعي", "رمادي ميكانيكي", "أزرق هادئ", "أزرق الأداء",
    "أبيض خزفي", "رمادي جرافيتي", "فضي ميكا", "بحيرة سماوية", "رمادي صخري",
    "أسود منتصف الليل", "أزرق فاتح", "أزرق غامق", "ضوء النجوم", "رمادي سيبر"
]


def proxy_scraper():
    response = requests.get("https://sslproxies.org/")

    soup = BeautifulSoup(response.content, 'html.parser')
    table = soup.find('table', class_="table table-striped table-bordered")

    ip_addresses = table.find_all('td')[::8]
    ports = table.find_all('td')[1::8]

    ip_port_tuples = list(zip(map(lambda x: x.text, ip_addresses), map(lambda x: x.text, ports)))
    ips_with_ports = list(map(lambda x: x[0]+':'+x[1], ip_port_tuples))
    return ips_with_ports


def proxy_generator():
    proxy_list = proxy_scraper()
    chosen_proxy = choice(proxy_list)
    proxy = {'http': chosen_proxy}
    return proxy


def check_proxy(url, **kwargs):
    alternating_proxies = []
    count = 0
    while len(alternating_proxies) < NB_PROXIES_ALTERNATE and count < 10:
        try:
            proxy = proxy_generator()
            print("Proxy currently being used: {}".format(proxy))
            response = requests.get(url, proxies=proxy, **kwargs)
            print(response.status_code)
            print(response.text)
            proxy['http'] = f"http://{proxy['http']}"
            alternating_proxies.append(proxy['http'])
            # sleep(randint(3, 7)) # Sleep a random number of seconds (between 1 and 5)

            # if the request is successful, no exception is raised
        except:
            print("Connection error, looking for another proxy")
            pass
        count += 1
    return alternating_proxies


def find_product_attribute(attribute_list, description_text):
    for attribute in attribute_list:
        if (attribute in description_text.split()) or (attribute.lower() in description_text.split()) or (attribute.upper() in description_text.split()):
            return attribute


def extract_brand_and_color(text, brands, colors):
    # join the list into a regex pattern, using | to match any word in the list
    brand_pattern = r'\b(?:' + '|'.join(map(re.escape, brands)) + r')\b'
    color_pattern = r'\b(?:' + '|'.join(map(re.escape, colors)) + r')\b'

    # search for patterns in the text and extract the matched strings
    brand = re.search(brand_pattern, text, re.IGNORECASE)
    color = re.search(color_pattern, text, re.IGNORECASE)

    return brand.group(0).title() if brand else None, color.group(0).title() if color else None


async def fetch_alls(s, url, last_page, fetch_function, file_path, brand_list, color_list, currency):
    tasks = []
    for nb_page in range(1, last_page + 1):
        # create a user_agent object
        ua = UserAgent()
        # rotate user_agent
        headers = {"User-Agent": ua.random}
        task = asyncio.create_task(fetch_function(s, url, nb_page, headers, file_path, brand_list, color_list, currency))
        tasks.append(task)
    res = await asyncio.gather(*tasks)
    return res


def convert_arabic_price(ar_price):
    if '٫' in ar_price:
        integer_part, decimal_part = ar_price.split('٫')
        integer_part_en = convert_numbers.hindi_to_english(integer_part)
        decimal_part_en = convert_numbers.hindi_to_english(decimal_part)
        en_price = f"{integer_part_en}.{decimal_part_en}"
    else:
        # if the price is an integer, simply convert it
        en_price = convert_numbers.hindi_to_english(ar_price)
    return en_price


def normalize_url(url):
    if 'amazon.eg' in url:
        parts = url.split('/')
        dp_index = parts.index('dp')
        return parts[dp_index + 1]  # product id
    elif '2b.com' in url:
        return url.replace('ar/', 'en/')
    else:
        return url.replace('ar/', '')
