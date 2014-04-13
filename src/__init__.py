from src.downloader import download_by_url


def run(obj, url):
    data = download_by_url(url, obj)