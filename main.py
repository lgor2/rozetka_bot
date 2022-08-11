import requests
from bs4 import BeautifulSoup


def parse_categories():
    """This function get all the categories (links) of the goods with discount from website ROZETKA"""
    
    cat_links = []
    response = requests.get('https://rozetka.com.ua/rasprodaja/c83850/')
    page = response.text
    soup = BeautifulSoup(page, 'lxml')
    cats = soup.findAll('a', class_='portal-navigation__link')

    for cat_link in cats:
        cat_links.append(cat_link.get('href'))

    return cat_links


def get_all_goods(link):
    """TEST"""
    response = requests.get(link)
    page = response.text
    soup = BeautifulSoup(page, 'lxml')
    goods = soup.findAll('div', class_='goods-tile__inner')

    for product in goods:
        product_analysis(product)


def product_analysis(product):
    """TEST"""
    pass


def write_product_to_database():
    pass


# def teeest():
#     response = requests.get('https://rozetka.com.ua/utsenennye-mobilnye-telefony/c83854/')
#     page = response.text
#     print(page)
#     soup = BeautifulSoup(page, 'lxml')
#     goods = soup.findAll('div', class_='goods-tile__inner')
#
#     res = ''
#
#     for i in goods:
#         temp = []
#         temp += i.find('span', class_='goods-tile__title').text
#         temp += '\n'
#         temp += i.find('span', class_='goods-tile__price-value').text, i.find('span', class_='goods-tile__price-currency').text
#         temp += '\n--------------------------------\n'
#         temp = ''.join(temp)
#         res += temp
#
#     return res
