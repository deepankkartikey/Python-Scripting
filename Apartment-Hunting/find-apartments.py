import requests
from bs4 import BeautifulSoup

base_url = "https://www.sleepwellmanagement.com"
url = "https://www.sleepwellmanagement.com/apartment-search"
budget = float(input("Enter your rent budget: "))

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
print(f'Total Apartments found: {len(apartment_list)}')

filtered_apartments = []

for apartment in apartment_list:
    # apartment.get()
    listing_url = apartment.find('a').get('href')
    listing_url = base_url + listing_url
    location = apartment.find('div', class_="nhw-list__location").text.strip()
    price = apartment.find('div', class_="nhw-list__price").text.strip()
    # convert price to floating point value
    price = float(price.replace("$", "").replace(",", "").replace("/mo.", ""))

    # print(listing_url)
    # print(location)
    # print(price)
    if price < budget:
        filtered_apartments.append({"listing_location": location, "rent": price, "listing_url": listing_url})

print("Aparments with rent in your budget: ", len(filtered_apartments))
print(filtered_apartments)