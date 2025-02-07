import pytest
import requests
from project import get_book_author, get_book_title, get_book_pageCount


@pytest.mark.parametrize("x", [("Cultish"), ("Neuromancer"), ("Helter Skelter")])
def test_get_data(x):
    response = requests.get(f"https://www.googleapis.com/books/v1/volumes?q={x}+title&maxResults=1")
    assert response.status_code == 200


@pytest.mark.parametrize("x", [("Cultish"), ("Neuromancer"), ("Nineteen Eighty-Four")])
def test_get_book_author(x):
    response = requests.get(f"https://www.googleapis.com/books/v1/volumes?q={x}+title&maxResults=1")
    dictionary = response.json()
    data = dictionary["items"][0]["volumeInfo"]
    #book_authors = data['authors']
    assert get_book_author(data) in ['Amanda Montell', 'William Gibson', 'George Orwell']


@pytest.mark.parametrize("x", [("Cultish"), ("Neuromancer"), ("Nineteen Eighty-Four")])
def test_get_book_title(x):
    response = requests.get(f"https://www.googleapis.com/books/v1/volumes?q={x}+title&maxResults=1")
    dictionary = response.json()
    data = dictionary["items"][0]["volumeInfo"]
    #book_title = data['title']
    assert get_book_title(data) in ["Cultish", "Neuromancer", "Nineteen Eighty-Four"]


@pytest.mark.parametrize("x", [("Cultish"), ("Neuromancer"), ("Nineteen Eighty-Four")])
def test_get_book_pageCount(x):
    response = requests.get(f"https://www.googleapis.com/books/v1/volumes?q={x}+title&maxResults=1")
    dictionary = response.json()
    data = dictionary["items"][0]["volumeInfo"]
    #book_pageCount = data['pageCount']
    assert get_book_pageCount(data) in [320, 306, 327]




if __name__ == "__main__":
    pytest.main()