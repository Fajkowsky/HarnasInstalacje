from urllib.request import urlretrieve

from src import settings


class Enix:
    def __init__(self, content):
        self.content = content.select(".product")[0]

    def get_title(self):
        return self.content.h1.string

    def get_picture(self):
        content = self.content.select(".easyzoom")[0]
        img_url = content.a['href']
        img, headers = urlretrieve(
            img_url,
            '{}file.png'.format(settings.tmp_directory)
        )
        return img

    def get_description(self):
        return self.content.select(".text")[0]

    def get_values(self):
        return {
            'title': self.get_title(),
            'description': self.get_description(),
            'picture': self.get_picture()
        }
