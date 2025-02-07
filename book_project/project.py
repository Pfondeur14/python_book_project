import requests
import json
import urllib.request
from fpdf import FPDF
import sys
import math

"""
Global Variables:
data = {}
volume_data = {}
"""

def main():
    """
    Main Calls back program functions and assings the return to new variables,
    respectively.
    Accepts user input as a parameter for get_data to modify URL, for API request.
    While loop: asks if user wants to keep searching for titles forever unless user
    choses not to by providing input for conditional statements
    Try/Exception statement handles keyError if book title or cover not availabe.
    """
    while True:
        try:
            get_data(input("Book Title: ").lower().strip())
            get_items_data(data)
            rating = get_avg_rating()
            author = get_book_author(volume_data)
            title = get_book_title(volume_data)
            category = get_book_category()
            pageCount = get_book_pageCount(volume_data)
            bookCover = get_book_cover()
            """urllibs retrieves cover url and transforms it into a .jpg file"""
            urllib.request.urlretrieve(bookCover, "book.jpg")
            """FPDF uses .jpg file and sets pdf paramaters"""
            pdf = FPDF(orientation = "landscape")
            pdf.add_page()
            pdf.set_font("Helvetica", "B", size = 20)
            pdf.image("book.jpg", 20, 16, 66)
            pdf.set_text_color(000, 000, 000)
            pdf.ln(35)
            pdf.cell(100)
            pdf.multi_cell(
                0, 10, f"Average rating: {rating} \n"
                f"Title: {title} \n"
                f"Author: {author} \n"
                f"Category: {category} \n"
                f"Page Count: {pageCount} \n",
                align='C'
                )
            """
            :returns: ouput PDF file including returned information from the
            fuctions called by main
            """
            pdf.output("book.pdf")
            """Gets user input for if statement to continue loop or exit program"""
            r = input("Would you like to search for another book? Yes / No: ").lower()
            if r == "yes":
                continue
            if r == "no":
                sys.exit("Happy Reading!")
        except KeyError:
            print("Book Information not available")


def get_data(r):
    """
    Accepts parameter input from main to modify URL, for request, using an f String.
    :try/except: handles HTTP request errors and exit program letting the user know
    to try later.
    """
    global data
    try:
        """ Sends HTTP request to Google Books API """
        # API key can be added at the end of the URL after the no. 1 as follows:
        # /books/v1/volumes?q={r}+title&maxResults=1&key=YOURKEY
        response = requests.get(
            f"https://www.googleapis.com/books/v1/volumes?q={r}+title&maxResults=1",
            timeout=10
        )
        """ Returns Json file data as an Python Object """
        if response.status_code == 200:
            o = response.text
            data = json.loads(o)
            """
            Asigns return value to Global variable data to be used by other
            functions
            """
            return data
        else:
            raise requests.exceptions.RequestException
    except requests.exceptions.RequestException:
        sys.exit("HTTP Error: Try Again Later")


def get_items_data(data):
    """
        Access first Dictionary using key=Items to pull list of Dictionaries.
        Then uses list comprehension to iterate through items list to access
        'Items' and pull nested Volume information.
        :return: volume data Dictionary to global variable to be use by other
        functions.
    """
    global volume_data
    info = [item_data for item_data in data['items']]
    volume_data = info[0]['volumeInfo']
    return volume_data


def get_book_author(volume_data):
    """
        Accepts variable 'volume_data' as a parameter to access book authors list.
        :returns: book authors info.
        due to json sometimes missing book info try/except handles keyError and
        returns alternate value.
    """
    bookData = volume_data['authors']
    try:
        book_authors = bookData
        for author in book_authors:
            return author
    except KeyError:
        return "Author Not Available"


def get_book_title(volume_data):
    """
        Accepts variable 'volume_data' as a parameter to access key=title
        :returns: book tile info
        if title not found main function will handle the KeyError
    """
    bookData = volume_data['title']
    book_title = bookData
    return book_title


def get_book_category():
    """
        Uses global variable 'volume_data' to iterate through book categories list.
        :returns: categories list.
        due to json sometimes missing book info try/except handles keyError and
        returns alternate value.
    """
    try:
        category_access = volume_data['categories']
        for category_data in category_access:
            return category_data
    except KeyError:
        return "No Category Available"


def get_book_pageCount(volume_data):
    """
        Accepts variable 'volume_data' as a parameter to access key=pageCount
        :returns: book page count
        due to json sometimes missing book info try/except handles keyError and
        returns alternate value.
    """
    pageData = volume_data['pageCount']
    try:
        page_count = pageData
        return page_count
    except KeyError:
        return "Page Count Not Available"


def get_book_cover():
    """
        Uses global variable 'volume_data' to access bookCover nested dict using
        key=['imageLinks']['thumbnail'].
        :returns: book cover link.
        if cover not found main function will handle the KeyError.
    """
    bookCover = volume_data['imageLinks']['thumbnail']
    return bookCover


def get_avg_rating():
    """
        Uses global variable 'volume_data' to access key=['averageRating'].
        :returns: book average rating.
        due to json sometimes missing book info try/except handles keyError
        and returns alternate value.
    """
    try:
        rating = volume_data['averageRating']
        stars = ((math.ceil(rating)) * "*")
        return stars
    except KeyError:
        return "Average rating Not Available"


if __name__ == "__main__":
    main()
