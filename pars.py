
from bs4 import BeautifulSoup as Bs
import requests
import csv

URL = 'https://enter.kg/computers/noutbuki_bishkek'
    
def parse():
    response = requests.get(url = URL)
    soup = Bs(response.content,'html.parser')
    items = soup.find_all('div', class_ = "product vm-col vm-col-1")
    new_list = []
    for i in items:
        try:
            new_list.append({'название':i.find('span',class_ = 'prouct_name').get_text(strip = True),
                            'цена':i.find('span', class_ = 'price').get_text(strip = True),
                             'изображение': i.find('a', class_ = 'product-image-link').find('img').get('src')
                            })
        except Exception as error:
            print(f'Ошибка --{error}')

    with open('information.csv', 'w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=['название', 'цена', 'изображение'])
        writer.writeheader()
        writer.writerows(new_list)

    return new_list

print(parse())
