import requests

URL = "http://www.whiskybase.com/"

page = requests.get(URL, headers={'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36'})

print(page.status_code)
print(page.text)