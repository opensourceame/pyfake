from pyfake.book import Book

def test_book():
    b = Book()
    title = b.title
    author = b.author
    publisher = b.publisher
    year = b.year

    assert title is not None
    assert author is not None
    assert publisher is not None
    assert year is not None