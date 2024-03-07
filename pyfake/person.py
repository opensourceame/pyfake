from .generator import Generator
from pathlib import Path
import random
import yaml

with open(str(Path(__file__).parent) + '/config/people.yml', 'r') as file:
    CONFIG = yaml.safe_load(file)

class Person(Generator):
    def generate(self):
        data = random.choice(CONFIG)

        self.first_name = data['first_name']
        self.last_name  = data['last_name']
        self.email      = data['email']
        self.age        = data['age']
        self.gender     = data['gender']
