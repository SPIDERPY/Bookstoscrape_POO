import os
from time_function import calculate_time_spent
from response import Response
from soup import Soup
from category import Category
from book import Book
from file import File
from page import Page


def main():

    response_site = Response("https://books.toscrape.com/index.html").response
    soup_site = Soup().get_soup(response_site)
    all_categories_urls = Page(soup_site).list_categories_urls()
    headers = list(Book().get_datas_book().keys())

    for category in all_categories_urls:
        list_books = Category(category).list_books_urls_category()
        category_name = Category(category).category_name()
        if not os.path.exists(category_name):
            os.mkdir(category_name)
            File(f"{category_name}").create_csv_file(headers)
            for book in list_books:
                book_datas = list(Book(book).get_datas_book().values())
                File(f"{category_name}").add_datas_csv_file(book_datas)
                book_image = Book(book).get_image_book()
                File(f"{category_name}").add_image_file(book, book_image)


if __name__ == "__main__":
    main()
