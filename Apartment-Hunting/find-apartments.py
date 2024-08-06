import requests
from bs4 import BeautifulSoup

url = "https://www.sleepwellmanagement.com/apartment-search"

# Proxy configuration
# proxy_host = ''
# proxy_port = 823
# proxy_login = ''
# proxy_password = ''
# proxy = f'http://{proxy_login}:{proxy_password}@{proxy_host}:{proxy_port}'

proxies = {
    # 'http': proxy,
    # 'https': proxy
}

response = requests.get(url=url, proxies=proxies)
soup = BeautifulSoup(response.text, 'html.parser')
# print(soup)

# useful classes in parsed html
# per listing - nhw-list__item
# name - nhw-list__location
# price - nhw-list__price

apartment_list = soup.find_all(class_="nhw-list__item")
# print(len(apartment_list))

for apartment in apartment_list:
    # apartment.get()
    location = apartment.find('div', class_="nhw-list__location").text.strip()
    price = apartment.find('div', class_="nhw-list__price").text.strip()
    print(location, price)
    # print(apartment)