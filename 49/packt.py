from collections import namedtuple

from bs4 import BeautifulSoup
import requests

PACKT = "https://bites-data.s3.us-east-2.amazonaws.com/packt.html"
CONTENT = requests.get(PACKT).text

Book = namedtuple("Book", "title description image link")


def get_book():
    """make a Soup object, parse the relevant html sections, and return a Book namedtuple"""
    html = CONTENT
    soup = BeautifulSoup(html, "html.parser")
    book_soup = soup.find_all("div", {"class": "dotd-main-book-image"})
    book_soup = book_soup[0]
    image = book_soup.find("img").get("src")
    link = book_soup.find("a").get("href")
    title_soup = soup.find_all("div", {"class": "dotd-title"})
    title = title_soup[0].text.strip()
    a_soup = soup.find_all("div", {"class": "dotd-main-book-summary float-left"})[0]
    description = [
        div.string.strip()
        for div in a_soup.find_all("div")
        if not div.get("class") and div.string
    ][0]
    return Book(title=title, description=description, image=image, link=link)
