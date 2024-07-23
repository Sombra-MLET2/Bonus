import pytest
from library.book import Book
from library.documentary import Documentary
from library.libraryItem import LibraryItem
from library.magazine import Magazine


def test_inheritance():
    lib_item_book: LibraryItem = Book(title='The Hitchhiker\'s Guide to the Galaxy',
                                      author='Douglas Adams',
                                      year=1979,
                                      publisher='Pan Books',
                                      pages_number=180)

    book_book = Book(title='It',
                     author='Stephen King',
                     year=1986,
                     publisher='Viking',
                     pages_number=1138)

    lib_item_doc: LibraryItem = Documentary(title='Cosmos',
                                            director='Carl Sagan',
                                            year=1980,
                                            producer='Carl Sagan',
                                            duration=60)

    lib_item_mag: LibraryItem = Magazine(title='National Geographic',
                                         publisher='National Geographic Society',
                                         pages_number=82)

    assert isinstance(book_book, Book)
    assert isinstance(lib_item_book, Book)
    assert isinstance(lib_item_doc, Documentary)
    assert isinstance(lib_item_mag, Magazine)


def test_abstract_class():
    with pytest.raises(TypeError):
        item = LibraryItem(title="Library Item name", sector="Library")
