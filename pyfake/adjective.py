from .renderer import Renderer
import random
import yaml


class Adjective(Renderer):
    with open("config/adjectives.yml", "r") as file:
        CONFIG = yaml.safe_load(file)

    def adjective(self):
        return random.choice(self.CONFIG["adjectives"])

    def render(self):
        self.adjective = self.adjective()
