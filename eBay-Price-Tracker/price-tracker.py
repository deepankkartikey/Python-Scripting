from bs4 import BeautifulSoup
import requests
import numpy as np
import csv
from datetime import datetime

LINK = "https://www.ebay.ca/sch/i.html?_from=R40&_trksid=p2334524.m570.l1311&_nkw=m3+macbook+pro&_sacat=0&_odkw=macbook+pro&_osacat=0"

def get_prices_by_link(link):
    """
    Extracts numerical price from the URL (search page query string)
    """
    r = requests.get(link)
    page_details = BeautifulSoup(r.text, 'html.parser')
    # print(page_details)
    search_results = page_details.find("ul", {"class":"srp-results"}).find_all("li", {"class":"s-item"})

    item_prices = []

    for result in search_results:
        price_as_text = result.find("span", {"class":"s-item__price"}).text
        price_as_text = price_as_text.strip()
        print(price_as_text)
        if "to" in price_as_text:
            continue
        # C $2,706.50 - price format in scraped data
        price = float(price_as_text[3:].replace(",","").strip())
        item_prices.append(price)
    return item_prices

if __name__ == "__main__":
    prices = get_prices_by_link(LINK)
    print(prices)