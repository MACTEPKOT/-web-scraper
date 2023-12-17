from functions import get_html_content, parse_books

# Получаем HTML-код страницы
url = "http://books.toscrape.com/catalogue/category/books/classics_6/index.html"
html_content = get_html_content(url)

# Парсим HTML-код с помощью BeautifulSoup
books = parse_books(html_content)

# Выводим результат
for book in books:
    print(book)