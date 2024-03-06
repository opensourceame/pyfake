from .generator import Generator
import random
import yaml


class Adjective(Generator):
    with open("config/adjectives.yml", "r") as file:
        CONFIG = yaml.safe_load(file)

    def adjective(self):
        return random.choice(self.CONFIG["adjectives"])

    def generate(self):
        self.adjective = self.adjective()
