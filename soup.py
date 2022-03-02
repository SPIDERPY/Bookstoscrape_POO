from bs4 import BeautifulSoup


class Soup:
    """Class initialisant le contenu de la page html"""
    def get_soup(self, response):
        """Méthode pour récuperer le contenu de la page html"""
        soup = BeautifulSoup(response.content,
                             "html.parser")
        return soup
