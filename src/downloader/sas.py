from urllib.request import urlretrieve

from src import settings


class Sas:
    def __init__(self, content):
        self.left_panel = None
        self.content = content.select(".nopad")[0]

    def get_title(self):
        content = self.content.select("#tabs-1")[0]
        self.left_panel = content.select('td')[1]
        return self.left_panel.strong.text

    def get_picture(self):
        img_url = self.content.select('.multithumb')[0]['src']
        img, headers = urlretrieve(
            img_url,
            '{}file.png'.format(settings.tmp_directory)
        )
        return img

    def get_description(self):
        return self.left_panel.table

    def get_values(self):
        return {
            'title': self.get_title(),
            'description': self.get_description(),
            'picture': self.get_picture()
        }
