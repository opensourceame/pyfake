from .generator import Generator
from pathlib import Path
import random
import yaml

with open(str(Path(__file__).parent) + '/config/books.yml', 'r') as file:
    CONFIG = yaml.safe_load(file)

class Book(Generator):
    def generate(self):
        data = random.choice(CONFIG)

        self.author    = data['author']
        self.genre     = data['genre']
        self.title     = data['title']
        self.publisher = data['publisher']
        self.year      = data['year']
