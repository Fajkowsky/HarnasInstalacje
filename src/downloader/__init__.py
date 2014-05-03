from urllib.parse import urlparse

from requests import get
from bs4 import BeautifulSoup

from .dedietrich import Dedietrich
from .enix import Enix
from .sas import Sas
from .defro import Defro
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

    data_object = globals()[class_name](soup)

    return data_object.get_values()