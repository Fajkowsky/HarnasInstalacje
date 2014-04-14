from urllib.request import urlretrieve

from src import settings


class Dedietrich:
    def __init__(self, content):
        self.content = content.select('#content')[0]

    def get_title(self):
        return self.content.h1.string

    def get_picture(self):
        img_url = settings.sites['dedietrich'] + self.picture.img['src']
        img, headers = urlretrieve(
            img_url,
            '{}file.tmp'.format(settings.tmp_directory)
        )
        return img

    def get_description(self):
        spam = self.content.select('.product')[0]
        for div in spam.findAll('div', 'pic'):
            self.picture = div.extract()
        return spam

    def get_values(self):
        return {
            'title': self.get_title(),
            'description': self.get_description(),
            'picture': self.get_picture()
        }
