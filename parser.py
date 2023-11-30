import requests
from bs4 import BeautifulSoup
# establishing session
s = requests.Session()
s.headers.update({
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36 OPR/104.0.0.0 (Edition Yx GX)'
    })


def load_user_data(session, product_id):
    url = 'https://easysellers.ru/wb/product/%s' % product_id
    request = session.get(url)
    return request.text


def contain_product_data(text):
    soup = BeautifulSoup(text, 'html.parser')
    product_data = soup.find('p', {'class': 'title'})
    if product_data:
        parse_user_datafile_bs(text)




def parse_user_datafile_bs(text):
    soup = BeautifulSoup(text, 'html.parser')
    product_info = soup.find('div', {'class': 'column is-three-quarters'})
    items = product_info.find_all('p', {'class': 'title'})
    product_name = soup.find('h1', {'class': 'title is-3'}).text
    product_type = soup.find('section', {'class': 'section'}).find('p').findNext('a').text
    seller_info = soup.findAll('div', {'class': 'container'})
    seller = seller_info[2].findNext('a').text
    day_profit = items[0].text
    week_profit = items[1].text
    alltime_profit = items[2].text
    append_data({
        'Имя товара': product_name,
        'Тип товара': product_type,
        'Дневная выручка': day_profit,
        'Недельная выручка': week_profit,
        'Выручка за все время': alltime_profit,
        'Продавец': seller
    })


def append_data(data):
    with open("fulldata.txt", "a", encoding="utf-8") as myfile:
        myfile.write(str(data)+'\n')


for i in range(999999999):
    data = load_user_data(s, i)
    contain_product_data(data)
