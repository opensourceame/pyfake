from .generator import Generator
import yaml
import random

class Country(Generator):
    with open('config/countries.yml', 'r') as file:
        CONFIG = yaml.safe_load(file)

    def generate(self):
        data = random.choice(self.CONFIG)

        self.name         = data['name']
        self.currency     = data['currency']
        self.capital_city = data['capital_city']
        self.population   = data['population']
        self.area         = data['area']
        self.languages    = data['languages']
