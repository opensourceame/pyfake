from .generator import Generator
from pathlib import Path
import yaml
import random

with open(str(Path(__file__).parent) + '/config/countries.yml', 'r') as file:
    CONFIG = yaml.safe_load(file)

class Country(Generator):
    def generate(self):
        data = random.choice(CONFIG)

        self.name         = data['name']
        self.currency     = data['currency']
        self.capital_city = data['capital_city']
        self.population   = data['population']
        self.area         = data['area']
        self.languages    = data['languages']
