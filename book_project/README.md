# BOOK SEARCH ENGINE
#### Video Demo:  <URL https://www.youtube.com/watch?v=uomx8RABZZQ>
#### Description: Python program that uses the Google Books API adding user input to search for book Titles. Results are printed on a PDF including the Title, Author, Category, Page Count, average rating and an Image of the Book cover, if the book is not found the program will let the user know the information is not available. Users will be able to continue searching for book titles until they decide to exit the program.

About me:
Name: A. Patricia Fondeur
I live in Sonoma, California

The files for this project include the following:
1. project.py
2. test_project.py
3. requirements.txt
4. README.md
5. data_sample.json (An example of the data contained in the request response)

Requirements.txt:
1. Import json
2. Import requests
3. urllib.request
4. From fpdp import FPDF
5. Import sys
6. math
7. Import pytest

Notes:
Json Data quite complex to understand since the data in the response was nested within different data types. One of the most important things I learned while working on this project is that testing as you go is probably better than after your code is finished, or even creating the testing program before starting your code otherwise it takes a lot of refactoring and possibly breaking your program several times to get to a good place to pass your tests.

I tried to incorporated the concepts I have learned so far including conditionals, loops, exceptions, libraries, unit test with pytest and file I/O as well as parametrize, pulling images from urls, global variables and API keys.

Also, now I know I need to learn a lot more about how to tests API requests to avoid repeated request, mocking is definetly on my list of things to learn as I continue my learing journey.

Finally, in a real world program the requests in this code should include an API key so the API producer can identify the calling project, the API key can also be used to restrict their use and block anonymous traffic, etc.


TODO
1. Read Google Books API documentation
2. Created an API key to use Google Books API
3. Read requests library Documentation (https://requests.readthedocs.io/en/latest/user/quickstart/#make-a-request)
4. Read json library Documentation https://requests.readthedocs.io/en/latest/user/quickstart/#json-response-content
5. Read fpdf Documentation (https://pypi.org/project/fpdf2/)
6. Read pytest documentantion
7. Create a youtube account
8. Write the program
9. Write tests
10. Record Video


Resources:

Create API Key:
https://developers.google.com/books/docs/v1/using
http://www.penguinrandomhouse.biz/webservices/rest/

Research Google Cloud Console
Google Books API: https://developers.google.com/books/docs/v1/getting_started

How to create an API Key or Auth: https://developers.google.com/books/docs/v1/using

Learn to use Postman: API Platform: https://learning.postman.com/docs/getting-started/introduction/

BISAC - Book Subject Heading: https://bisg.org/page/Fiction
Book Metadata Support https://support.google.com/books/partner/answer/3237055?hl=en


Functions in project.py

main:

"""
    Main Calls back program functions and assings the return to new variables, respectively.

    Gets user input as a parameter for get_data to modify URL, for API request.

    While loop: asks if user wants to keep searching for titles forever unless user choses not to by providing input for conditional statements

    Try/Exception statement handles keyError if book title or cover not availabe.

    urllibs retrieves cover url and transforms it into a .jpg file

    FPDF uses .jpg file and sets pdf paramaters

    :returns: ouput PDF file including returned information from the fuctions called by main

    Gets user input for if statement to continue loop or exit program
"""

get_data:

"""
    Accepts parameter input from main to modify URL, for request, using an f String

    try/except statements handle HTTP request errors and exit program letting the user know to try later

    Sends HTTP request to Google Books API

    Returns Json file data as an Python Object

    Asigns return value to Global variable data
"""


get_items_data:

"""
    Access first Dictionary using key=Items to pull list of Dictionaries

    Then uses list comprehension to iterate through items list to access 'Items' and pull nested Volume information

    :return: volume data Dictionary to global variable to be use by other functions
"""


get book_author:

"""
    Accepts variable 'volume_data' as a parameter to access book authors list

    :returns: book authors info

    due to json sometimes missing book info try/except handles keyError and returns alternate value

"""


get_book_title:

"""
        Accepts variable 'volume_data' as a parameter to access key=title

        :returns: book tile info

        if title not found main function will handle the KeyError
"""


get_book_category:

"""
    Uses global variable 'volume_data' to iterate through book categories list

    :returns: categories list

    due to json sometimes missing book info try/except handles keyError and returns alternate value
"""


get_book_pageCount:

"""
    Accepts variable 'volume_data' as a parameter to access key=pageCount

    :returns: book page count

    due to json sometimes missing book info try/except handles keyError and returns alternate value

"""


get_book_cover:

"""
    Uses global variable 'volume_data' to access bookCover nested dict using key='imageLinks''thumbnail'

    :returns: book cover link

    if cover not found main function will handle the KeyError

"""


get_avg_rating:

"""
    Uses global variable 'volume_data' to access key='averageRating'
    :returns: book average rating

    due to json sometimes missing book info try/except handles
    keyError and returns alternate value
"""

Functions in test_project.py:

test_get_data:
Test the request response is working by asserting the status code is 200 for three different requests using parametrize.

test_get_book_author:
Test get book author in project.py by accepting parameters for three different books and comparing the results with the local request

test_get_book_title:
Test get book title in project.py by accepting parameters for three different books and comparing the results with the local request

test_get_book_pageCount:
Test get book pageCount in project.py by accepting parameters for three different books and comparing the results with the local request


Cheers!