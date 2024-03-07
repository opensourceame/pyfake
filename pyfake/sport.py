from .generator import Generator
from pathlib import Path
import yaml
import random

with open(str(Path(__file__).parent) + '/config/sports.yml', 'r') as file:
    CONFIG = yaml.safe_load(file)

class Sport(Generator):
    def generate(self):
        data = random.choice(CONFIG)

        self.name         = data['name']
        self.players      = data['players']
        self.field_size   = data['field_size']
        self.equipment    = data['equipment']
        self.outdoor      = data['outdoor']
