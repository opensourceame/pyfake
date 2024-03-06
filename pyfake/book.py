from .renderer import Renderer
import random
import yaml

with open('config/books.yml', 'r') as file:
    CONFIG = yaml.safe_load(file)

class Book(Renderer):
    def render(self):
        data = random.choice(CONFIG)

        self.author    = data['author']
        self.genre     = data['genre']
        self.title     = data['title']
        self.publisher = data['publisher']
        self.year      = data['year']
