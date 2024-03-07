from .generator import Generator
from pathlib import Path
import random
import yaml

with open(str(Path(__file__).parent) + '/config/company.yml', 'r') as file:
    CONFIG = yaml.safe_load(file)

class Company(Generator):
    def company_name(self):
        return random.choice(CONFIG['names'])

    def company_suffix(self):
        return random.choice(CONFIG['suffixes'])

    def generate(self):
        self.size = random.randint(1, 100)
        self.name = f"{self.company_name()} {self.company_suffix()}"