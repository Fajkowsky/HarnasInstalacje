from urllib.parse import urlparse

from requests import get
from bs4 import BeautifulSoup

from .dedietrich import Dedietrich
from ..settings import sites

soup = None


def get_class(url):
    spam = urlparse(url)
    for key, value in sites.items():
        if spam.netloc in value:
            return key.capitalize()


def download_by_url(url):
    global soup

    html = get(url)
    soup = BeautifulSoup(html.content)

    class_name = get_class(url)

    return globals()[class_name](soup)