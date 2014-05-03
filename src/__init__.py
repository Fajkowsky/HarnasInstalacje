from src.downloader import download_by_url
from src.uploader import upload_data

from .settings import tmp_directory


def save(data):
    with open("{}tmp.txt".format(tmp_directory), "w") as text_file:
        text_file.write("Tytul: {}".format(data['title']))
        text_file.write("\n\n")
        text_file.write("Opis: {}".format(data['description']))


def run(url):
    '''Download title, description, image for given url'''
    data = download_by_url(url)
    save(data)
    upload_data(data)