import json
import os
from typing import Optional, Union

from Book import  BookClass

DATA_FILE = "library.json"



class LibraryClass:


    def __init__(self):
        self.books: list[BookClass] = []
        self._load_books()

    def _load_books(self):

        try:
            if os.path.exists(DATA_FILE):
                with open(DATA_FILE, "r") as file:
                    data = json.load(file)
                    self.books = [BookClass.from_dict_to_object(book) for book in data]
        except:
            self.books = []

    def save_books(self):

        with open(DATA_FILE, "w") as file:
            json.dump([book.from_input_to_dict() for book in self.books], file, indent=4)

    def add_book(self, title: str, author: str, year: int) -> None:

        new_id = max((book.id for book in self.books), default=0) + 1
        new_book = BookClass(id = new_id, title=title, author=author, year=year)
        self.books.append(new_book)
        self.save_books()
        print(f"Книга '{title}' добавлена с ID {new_id}.")

    def delete_book(self, book_id: int) -> None:

        book = self.find_book_by_id(book_id)
        if book:
            self.books.remove(book)
            self.save_books()
            print(f"Книга с ID {book_id} удалена.")
        else:
            print("Книга с таким ID не найдена.")

    def find_book_by_id(self, id: int) -> Optional[BookClass]:

        for book in self.books:
            if book.id == id:
                return book
        return None

    def search_books(self, key: str, value: Union[str, int]) -> list[BookClass]:
        result = []
        for book in self.books:

            attribute = getattr(book, key, None)
            if attribute is not None and str(attribute).lower() == str(value).lower():
                result.append(book)

        return result

    def display_books(self, books: Optional[list[BookClass]] = None) -> None:

        books = books or self.books
        if not books:
            print("Библиотека пуста.")
            return
        for book in books:
            print(
                f"ID: {book.id}, Название: {book.title}, Автор: {book.author}, "
                f"Год: {book.year}, Статус: {book.status}"
            )

    def update_status(self, id: int, new_status: str) -> None:

        if new_status not in ["в наличии", "выдана"]:
            print("Некорректный статус. Допустимые значения: 'в наличии', 'выдана'")
            return
        book = self.find_book_by_id(id)

        if book:
            book.status = new_status
            self.save_books()
            print(f"Статус книги с ID {id} обновлен на '{new_status}'.")
        else:
            print("Книга с таким ID не найдена.")