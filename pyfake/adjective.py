from .generator import Generator
from pathlib import Path
import random
import yaml

with open(str(Path(__file__).parent) + '/config/adjectives.yml', 'r') as file:
    CONFIG = yaml.safe_load(file)

class Adjective(Generator):
    def adjective(self):
        print(CONFIG)
        return random.choice(CONFIG)

    def generate(self):
        self.adjective = self.adjective()
