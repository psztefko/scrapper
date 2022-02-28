import requests
from bs4 import BeautifulSoup

URL = "https://www.whiskybase.com/market/browse?style=table&search=scotch&selling_method=buy&price=&shipsto=&brand_id=&fillinglevel_id=&vintage_year=&bottler_id=&bottle_date_year="

page = requests.get(URL, headers={'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36'})

soup = BeautifulSoup(page.content, "html.parser")


table_data = soup.find("table", attrs={"class": "whiskytable"})
firstrow_data = table_data.tbody.find_all("tr", attrs={"class": "mp-whisky-item-firstrow"})
secondrow_data = table_data.tbody.find_all("tr", attrs={"class": "mp-whisky-item-secondrow"})

def get_name(row):
    return row.find("a", attrs={"mp-whisky-item-name"}).get_text()

def get_img_url(row):
    img_tag = row.find("img", attrs={"unveil"})
    print(img_tag['data-src'])

for row in firstrow_data:
    """Extract data from upper of table row"""

    get_img_url(row)

for row in secondrow_data:
    """Extract data from lower of table row"""



"""
get:
    firstrow:
        name
        image_url

    secondrow:
        rating
        user_rating
        amount_of_user_ratings
        price
"""