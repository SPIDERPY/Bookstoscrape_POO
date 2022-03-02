from calendar import c
from urllib.parse import urljoin
from response import URL_PRINCIPAL
from time_function import calculate_time_spent

@calculate_time_spent
class Page:
    """Classe définissant un site web caractérisée par son url"""
    def __init__(self, soup):
        self.soup = soup

    def get_category(self):
        soup_categories = self.soup.select("ul")[2].select("li")
        for soup_category in soup_categories:
            category_url = urljoin(URL_PRINCIPAL, soup_category.a["href"])
            return category_url

    def list_categories_urls(self):
        """Méthode pour récupérer la liste
        de toutes les urls des catégories du site"""
        soup_categories = self.soup.select("ul")[2].select("li")
        categories_urls = []
        for soup_category in soup_categories:
            category_url = urljoin(URL_PRINCIPAL, soup_category.a["href"])
            categories_urls.append(category_url)
        return categories_urls
