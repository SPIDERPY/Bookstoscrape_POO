from urllib.parse import urljoin
from slugify import slugify
from response import URL_PRINCIPAL, Response
from soup import Soup


class Book:
    def __init__(self, url_book="https://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html"):
        self.url_book = url_book
        self.book_soup = Soup().get_soup(Response(url_book).response)
        self.star_rating = {"One": "1",
                            "Two": "2",
                            "Three": "3",
                            "Four": "4",
                            "Five": "5"}

    def get_datas_book(self):
        tds = self.book_soup.select("td")
        product_description = self.book_soup.select_one('#product_description')
        if product_description:
            product_description = self.book_soup.select("p")[3].text.lower()
            product_description = slugify(product_description, separator=" ")
        else:
            product_description = "none"
        review_rating = self.book_soup.find(class_="star-rating")["class"][1]
        datas = {"product_page_url": self.url_book,
                 "title": slugify(self.book_soup.h1.text,
                                  lowercase=False,
                                  separator=" "),
                 "universal_product_code": tds[0].text,
                 "price_including_tax": tds[2].text,
                 "price_excluding_tax": tds[3].text,
                 "number_available": tds[5].text,
                 "product_description": product_description,
                 "review_rating": self.star_rating[review_rating],
                 "image_url": urljoin(URL_PRINCIPAL,
                                      self.book_soup.find("img")["src"])}
        return datas

    def get_image_book(self):
        image_url = urljoin(URL_PRINCIPAL, self.book_soup.find("img")["src"])
        image = Response(image_url).response
        return image.content
    

