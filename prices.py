from numpy import product
import requests
from bs4 import BeautifulSoup
import pandas as pd

url = 'https://www.wickes.co.uk/search?text=ball+valve'


def get_data(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    return soup


def parse(soup):
    productslist = []
    results = soup.find_all('div', {'class': 'card product-card'})
    for item in results:
        product = {
            'title': item.find('a', {'class': 'product-card__title product-card__title-v2'}).text,
            'price': float(item.find('div', {'class': 'product-card__price-value'}).text.replace('£', '').replace(',', '').strip()),
            'link': url + item.find('a', {'class': 'product-card__title product-card__title-v2'})['href'],
        }
        productslist.append(product)
    return productslist


def output(productslist):
    productsdf = pd.DataFrame(productslist)
    productsdf.to_csv('output.csv', index=False)
    print('Saved to CSV')
    return


soup = get_data(url)
productslist = parse(soup)
output(productslist)
