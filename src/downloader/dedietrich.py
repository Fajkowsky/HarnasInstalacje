class Dedietrich:
    def __init__(self, content):
        self.content = content

    def get_title(self):
        pass

    def get_picture(self):
        pass

    def get_description(self):
        pass

    def get_values(self):
        return {
            'title': self.get_title(),
            'picture': self.get_picture(),
            'description': self.get_description()
        }
