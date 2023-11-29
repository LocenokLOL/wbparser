import requests
from bs4 import BeautifulSoup
# establishing session
s = requests.Session()
s.headers.update({
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36 OPR/104.0.0.0 (Edition Yx GX)'
    })


def load_user_data(session):
    product_id = input()
    url = 'https://easysellers.ru/wb/product/%s' % product_id
    request = session.get(url)
    return request.text


def contain_movies_data(text):
    soup = BeautifulSoup(text, 'html.parser')
    product_data = soup.find('p', {'class': 'title'})
    return product_data is not None


def load_page():
    data = load_user_data(s)
    if contain_movies_data(data):
        with open('./test2.html', 'w', encoding="utf-8") as output_file:
            output_file.write(data)


def read_file(filename):
    with open(filename, encoding="utf-8") as input_file:
        text = input_file.read()
    return text


def parse_user_datafile_bs(filename):
    result = []
    text = read_file(filename)
    soup = BeautifulSoup(text, 'html.parser')
    product_info = soup.find('div', {'class': 'column is-three-quarters'})
    items = product_info.find_all('p', {'class': 'title'})
    product_name = soup.find('h1', {'class': 'title is-3'}).text
    day_profit = items[0].text
    week_profit = items[1].text
    alltime_profit = items[2].text
    result.append({
        'Имя товара': product_name,
        'Дневная выручка': day_profit,
        'Недельная выручка': week_profit,
        'Выручка за все вреся': alltime_profit,
    })
    return result

load_page()
print(parse_user_datafile_bs('test2.html'))