import requests
from bs4 import BeautifulSoup

URL = "https://www.whiskybase.com/market/browse?take=50&search=JAPAN&selling_method%5B%5D=buy&price%5B%5D=-1&fillinglevel_id%5B%5D=&sort=added&direction=desc&page=1"

page = requests.get(URL, headers={'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36'})

soup = BeautifulSoup(page.content, "html.parser")

# result = soup.find('tbody')
# print(result.prettify())

gdp_table = soup.find("table", attrs={"class": "whiskytable"})
gdp_table_data = gdp_table.tbody.find_all("tr")  # contains 2 rows
print(gdp_table_data)
# Get all the headings of Lists
# headings = []
# for td in gdp_table_data[0].find_all("td"):
#     # remove any newlines and extra spaces from left and right
#
#     print(td)
    #headings.append(td.b.text.replace('\n', ' ').strip())

#print(headings)


"""
get:
name
image_url
rating
user_rating
amount_of_user_ratings
price
"""