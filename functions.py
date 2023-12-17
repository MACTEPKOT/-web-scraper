import requests
from bs4 import BeautifulSoup

def get_html_content(url):
    response = requests.get(url)
    return response.content

def parse_books(html_content):
    soup = BeautifulSoup(html_content, "html.parser")
    book_elements = soup.find_all("li", class_="col-xs-6 col-sm-4 col-md-3 col-lg-3")
    books = []
    for book_element in book_elements:
        title_element = book_element.find("h3")
        price_element = book_element.find("p", class_="price_color")
        if title_element and price_element:
            title = title_element.text.strip()
            price = price_element.text.strip()
            books.append((title, price))
    return books