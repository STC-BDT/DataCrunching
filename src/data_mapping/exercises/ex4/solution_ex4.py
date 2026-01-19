import json
import csv
from dataclasses import dataclass


@dataclass
class Book:
    id: int
    title: str
    author: str

    def to_repr(self):
        return {
            "id": self.id,
            "title": self.title,
            "author": self.author
        }

    @staticmethod
    def from_repr(raw_data):
        id = raw_data["id"]
        title = raw_data["title"]
        author = raw_data["author"]

        if not isinstance(author, str):
            raise ValueError
        if not isinstance(id, int):
            raise ValueError
        if not isinstance(title, str):
            raise ValueError

        return Book(
            id=id,
            title=title,
            author=author
        )

books = []

with open("books.json", "r") as fin:
    raw_data = json.load(fin)
    for raw_book in raw_data:
        books.append(
            Book.from_repr(raw_book)
        )

print(books)

with open("books.csv", "w") as fout:
    writer = csv.DictWriter(fout, fieldnames=["id", "title", "author"])
    writer.writeheader()

    for book in books:
        writer.writerow(book.to_repr())