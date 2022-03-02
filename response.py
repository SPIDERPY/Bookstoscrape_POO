import requests
URL_PRINCIPAL = "https://books.toscrape.com"


class Response:
    """Classe définissant une requete"""
    def __init__(self, url):
        """Initialise la requete de l'url"""
        self.response = requests.get(url)
