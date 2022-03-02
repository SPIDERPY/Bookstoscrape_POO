from pathlib import Path
from book import Book


class File:
    def __init__(self, name_file):
        self.name_file = name_file

    def create_csv_file(self, datas):
        with open(Path(self.name_file, f"{self.name_file}.csv"),
                  "w", encoding="utf-8-sig") as file:
            category_file = file.write(" ; ".join(datas) + "\n")
            return category_file

    def add_datas_csv_file(self, datas):
        with open(Path(self.name_file, f"{self.name_file}.csv"),
                  "a", encoding="utf-8-sig") as file:
            data_file = file.write(" ; ".join(datas) + "\n")
            return data_file

    def add_image_file(self, book, image):
        title = Book(book).get_datas_book()["title"]
        with open(Path(self.name_file, f"{title}.jpg"), "wb") as file:
            data_file = file.write(image)
            return data_file
