import time

import requests
from bs4 import BeautifulSoup
result = []
headers_v = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'
                        ' AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.81 Safari/537.36 Edg/104.0.1293.54'}
list_card_url = []
resource_v = None
description_list = []

def find_product(url):
    responce = requests.get(url, headers=headers_v)
    soup = BeautifulSoup(responce.text, 'lxml')
    data = soup.find_all('div', class_='col-lg-4 col-md-6 mb-4')
    time.sleep(1)
    for i in data:
        name = i.find('h4', class_='card-title').text
        name = name.strip('\n')
        price = i.find('h5').text
        url_img = 'https://scrapingclub.com' + (i.find('img', class_='card-img-top img-fluid').get('src'))
        url_product = 'https://scrapingclub.com' + i.find('a').get('href')
        result.append({f'{name}': [price, url_img, url_product]})
        list_card_url.append(url_product)
    return result, list_card_url

for count in range(1, 8):
    url = f'https://scrapingclub.com/exercise/list_basic/?page={count}'
    resource_v = find_product(url)

for card_url in resource_v[1]:
    response_card = requests.get(card_url, headers=headers_v)
    soup_card = BeautifulSoup(response_card.text, 'lxml')
    data_card = soup_card.find('div', class_='card mt-4 my-4')
    card_title = data_card.find('h3', class_='card-title').text
    price_card = data_card.find('h4').text
    description = data_card.find('p', class_='card-text').text
    url_image = 'https://scrapingclub.com' + data_card.find('img', class_='card-img-top img-fluid').get('src')
    print(card_title, price_card, description, url_image)

