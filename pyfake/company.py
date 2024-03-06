from .generator import Generator
import random
import yaml

class Company(Generator):
    with open('config/company.yml', 'r') as file:
        CONFIG = yaml.safe_load(file)

    def company_name(self):
        return random.choice(self.CONFIG['names'])

    def company_suffix(self):
        return random.choice(self.CONFIG['suffixes'])

    def generate(self):
        self.size = random.randint(1, 100)
        self.name = f"{self.company_name()} {self.company_suffix()}"