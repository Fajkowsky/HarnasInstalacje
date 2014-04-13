from requests import get
from bs4 import BeautifulSoup

from .dedietrich import Dedietrich


soup = None


def download_by_url(url, obj):
    global soup

    html = get(url)
    soup = BeautifulSoup(html.content)

    data = Dedietrich(soup)