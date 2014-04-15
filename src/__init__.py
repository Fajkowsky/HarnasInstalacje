from src.downloader import download_by_url
from src.uploader import upload_data

def run(url):
    '''Download title, description, image for given url'''
    data = download_by_url(url)
    upload_data(data)