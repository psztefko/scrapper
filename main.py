import re

import requests
from bs4 import BeautifulSoup

from src.whisky import Whisky

URL = "https://www.whiskybase.com/market/browse?style=table&search=scotch&selling_method=buy&price=&shipsto=&brand_id=&fillinglevel_id=&vintage_year=&bottler_id=&bottle_date_year="

page = requests.get(URL, headers={
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36'})

soup = BeautifulSoup(page.content, "html.parser")

table_data = soup.find("table", attrs={"class": "whiskytable"})
firstrow_data = table_data.tbody.find_all("tr", attrs={"class": "mp-whisky-item-firstrow"})
secondrow_data = table_data.tbody.find_all("tr", attrs={"class": "mp-whisky-item-secondrow"})


def get_name(row):
    """Scrap whisky name"""
    return row.find("a", attrs={"mp-whisky-item-name"}).get_text().strip()


def get_whisky_url(row):
    """Scrap url of whisky"""
    return row.find("a", attrs={"mp-whisky-item-name"})['href']


def get_img_url(row):
    """Scrap url of whisky image"""
    return row.find("img", attrs={"unveil"})['data-src']


def get_rating(row):
    """Scraps rating"""
    temp = row.find("dl", attrs={"dl-horizontal"}).get_text().strip()[22:]
    pattern_rating = re.compile(r'[^\s]+')
    rating = pattern_rating.search(temp)

    return rating.group()


def get_user_rating(row):
    """Scraps user rating"""
    user_rating = str(row.find("div", attrs={"bottle-rating"}))[:-8]
    return user_rating[-4:]


def get_amount_of_user_ratings(row):
    """Scraps amount of user ratings"""
    return row.find("span", attrs={"bottle-rating-votes"}).get_text().strip()[1:]


def get_price(row):
    """Scraps price"""
    price = row.find("div", attrs={"mp-whisky-item-price"}).get_text().strip()

    if price[0] == '€':
        return price
    else:
        return row.find("div", attrs={"mp-whisky-item-price-converted"}).get_text().strip()


list_of_whisky = []

if len(firstrow_data) == len(secondrow_data):
    for i in range(len(firstrow_data)):
        """Extract data from upper of table row"""
        firstrow = firstrow_data[i]

        """Extract data from lower of table row"""
        secondrow = secondrow_data[i]

        list_of_whisky.append(Whisky(get_name(firstrow),
                                     get_whisky_url(firstrow),
                                     get_img_url(firstrow),
                                     get_rating(secondrow),
                                     get_user_rating(secondrow),
                                     get_amount_of_user_ratings(secondrow),
                                     get_price(secondrow)))

for item in list_of_whisky:
    print(item.__str__())