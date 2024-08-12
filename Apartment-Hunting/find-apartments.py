import requests
from bs4 import BeautifulSoup
from apscheduler.schedulers.blocking import BlockingScheduler


def find_apartments(budget):
    base_url = "https://www.sleepwellmanagement.com"
    url = "https://www.sleepwellmanagement.com/apartment-search"

    # Proxy configuration
    proxy_host = ''
    proxy_port = 823
    proxy_login = ''
    proxy_password = ''
    proxy = f'http://{proxy_login}:{proxy_password}@{proxy_host}:{proxy_port}'

    proxies = {
        'http': proxy,
        'https': proxy
    }

    response = requests.get(url=url)
    soup = BeautifulSoup(response.text, 'html.parser')

    apartment_list = soup.find_all(class_="nhw-list__item")
    filtered_apartments = []

    for apartment in apartment_list:
        listing_url = apartment.find('a').get('href')
        listing_url = base_url + listing_url
        location = apartment.find('div', class_="nhw-list__location").text.strip()
        price = apartment.find('div', class_="nhw-list__price").text.strip()
        # convert price to floating point value
        price = float(price.replace("$", "").replace(",", "").replace("/mo.", ""))

        if price < budget:
            filtered_apartments.append({"listing_location": location, "rent": price, "listing_url": listing_url})

    return filtered_apartments


def apartment_finder_job():
    budget = float(input("Enter you budget: "))
    filtered_apartments = find_apartments(budget)
    if filtered_apartments:
        print(f"{ len(filtered_apartments) } listings found.")
    else:
        print("No apartments found in your budget.")


if __name__ == "__main__":
    apartment_finder_job()