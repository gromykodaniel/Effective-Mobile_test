import pytest

from Library import LibraryClass


@pytest.fixture
def library():

    lib = LibraryClass()
    lib.add_book("Book One", "Author A", 2000)
    lib.add_book("Book Two", "Author B", 2010)
    return lib

def test_add_book(library):

    initial_count = len(library.books)
    library.add_book("Book Three", "Author C", 2020)
    assert len(library.books) == initial_count + 1
    assert library.books[-1].title == "Book Three"

def test_remove_book(library):

    book_id = library.books[0].id
    library.delete_book(book_id)
    assert not any(book.id == book_id for book in library.books)

def test_find_book_by_id(library):

    book_id = library.books[0].id
    found_book = library.find_book_by_id(book_id)
    assert found_book is not None
    assert found_book.id == book_id

def test_search_books_by_title(library):

    results = library.search_books("title", "Book One")

    assert results[0].title == "Book One"

def test_search_books_by_author(library):

    results = library.search_books("author", "Author B")

    assert results[0].author == "Author B"

def test_change_status(library):

    book_id = library.books[0].id
    library.update_status(book_id, "выдана")
    assert library.books[0].status == "выдана"
