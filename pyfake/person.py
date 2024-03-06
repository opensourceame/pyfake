from .generator import Generator
import random
import yaml

class Person(Generator):
    with open('config/people.yml', 'r') as file:
        CONFIG = yaml.safe_load(file)

    def generate(self):
        data = random.choice(self.CONFIG)

        self.first_name = data['first_name']
        self.last_name  = data['last_name']
        self.email      = data['email']
        self.age        = data['age']
        self.gender     = data['gender']
