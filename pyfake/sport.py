from .generator import Generator
import yaml
import random

class Sport(Generator):
    with open('config/sports.yml', 'r') as file:
        CONFIG = yaml.safe_load(file)

    def generate(self):
        data = random.choice(self.CONFIG)

        self.name         = data['name']
        self.players      = data['players']
        self.field_size   = data['field_size']
        self.equipment    = data['equipment']
        self.outdoor      = data['outdoor']
