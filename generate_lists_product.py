import time
import requests
from bs4 import BeautifulSoup

headers_v = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'
                        ' AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.81 Safari/537.36 Edg/104.0.1293.54'}

def find_str_count():
    response = requests.get('https://scrapingclub.com/exercise/list_basic/', headers=headers_v)
    soup_site = BeautifulSoup(response.text, 'lxml')
    data = soup_site.find_all('li', class_='page-item')
    return len(data) + 1

def find_url_product():
    for count in range(1,find_str_count()):
        time.sleep(1)
        url_str = f'https://scrapingclub.com/exercise/list_basic/?page={count}'
        response = requests.get(url_str, headers=headers_v)
        soup = BeautifulSoup(response.text, 'lxml')
        data = soup.find_all('div', class_='col-lg-4 col-md-6 mb-4')
        for m in data:
            card_url = 'https://scrapingclub.com' + m.find('a').get('href')
            yield card_url

def array():
    for card_url in find_url_product():
        response_card = requests.get(card_url, headers=headers_v)
        soup_card = BeautifulSoup(response_card.text, 'lxml')
        data_card = soup_card.find('div', class_='card mt-4 my-4')
        card_title = data_card.find('h3', class_='card-title').text
        price_card = data_card.find('h4').text
        description = data_card.find('p', class_='card-text').text
        url_image = 'https://scrapingclub.com' + data_card.find('img', class_='card-img-top img-fluid').get('src')
        result = (card_title, price_card, description, url_image)
        yield result

