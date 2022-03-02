from urllib.parse import urljoin
from soup import Soup
from response import Response


class Category:
    """Classe définissant une catégorie de livres"""
    def __init__(self, category_url):
        """Création de notre contructeur
        qui prend comme attribut l'url de la categorie"""
        self.category_url = category_url
        self.soup = Soup().get_soup(Response(category_url).response)

    def all_pages_category(self):
        """Métode pour récupérer les pages d'une catégorie"""
        all_page_urls_category = [self.category_url]
        next_botton = self.soup.find("li", class_="next")
        while next_botton:
            page = urljoin(self.category_url, next_botton.a["href"])
            response = Response(page).response
            next_botton = Soup().get_soup(response).find("li", class_="next")
            all_page_urls_category.append(page)
        return all_page_urls_category

    def list_books_urls_category(self):
        """Métode pour récupérer les livres d'une catégorie"""
        books_urls = []
        for page in self.all_pages_category():
            response = Response(page).response
            soup_category_page = Soup().get_soup(response).\
                find_all("div", class_="image_container")
            for divs_book in soup_category_page:
                book_url = urljoin(self.category_url, divs_book.a["href"])
                books_urls.append(book_url)
        return books_urls

    def category_name(self):
        category_name = self.soup.find("h1").text
        return category_name
