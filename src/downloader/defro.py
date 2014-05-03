from urllib.request import urlretrieve

from src import settings


class Defro:
    def __init__(self, content):
        self.content = content.select(".entry")[0]

    def get_title(self):
        return self.content.span.text

    def get_picture(self):
        img_url = settings.sites['defro'] + self.content.select('img')[0]['src']
        img, headers = urlretrieve(
            img_url,
            '{}file.png'.format(settings.tmp_directory)
        )
        return img

    def get_description(self):
        description = self.content.select('.toggle')[0]
        return description

    def get_values(self):
        return {
            'title': self.get_title(),
            'description': self.get_description(),
            'picture': self.get_picture()
        }
