import random


class Dice:

    def __init__(self):
        self.value = None

    def roll(self, face=6):
        self.value = random.randint(0, face)
        return self.value
