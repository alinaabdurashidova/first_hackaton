import requests
from bs4 import BeautifulSoup as BS
import csv

def get_html(url):
    response = requests.get(url)
    return response.text

result = []
def get_data(html):
    soup = BS(html, 'lxml')
    page = soup.find('div', class_='content-wrapper clr home-page')
    wrap = page.find('div', class_='left-wrap')
    catalog = wrap.find('div', class_='listing-main-block')
    cars = catalog.find('div', class_='category-block cars')
    cars1 = cars.find('div', class_='category-block-content')
    sedans = cars1.find_all('div', class_='category-block-content-item')
    for transport in sedans:
        try:
            transport = sedans.find('div', class_='main-image')
            transport1 = transport.find('div', class_='bottom-info')
            transport2 = transport.find('div', class_='modal-main-image hidden')
            transport3 = transport.find('div', class_='modal-main-price').find_next('p', class_='price')
            title = transport1.find('div', class_='main-title')
        except:
            title = ''
        # try:
        #     image = sedan.find('dev', class_='main-image-item visible').get('src')
        #     image = f'https://www.mashina.kg/{image}'
        # except:
        #     image = ''

        # data = {
        #     'title':title,
        #     'image':image
        #     # 'price':price
        # }
    # write_csv(data)
    # result.append(title)
    print(title)
    

    
    
    


def write_csv(data):
    with open('transport.csv', 'a') as csv_file:
        names = ['title', 'image']
        writer = csv.DictWriter(csv_file, delimiter='|', fieldnames=names)
        writer.writerow(data)

def main():
    url = 'https://www.mashina.kg/'
    html = get_html(url)
    data = get_data(html)

main()