# game/dungeon.py
import random
from config import SCREEN_WIDTH, SCREEN_HEIGHT

class Dungeon:
    def __init__(self):
        self.rooms = []
        self.generate()

    def generate(self):
        # Simple: 5 random rooms for now
        for _ in range(5):
            x = random.randint(0, SCREEN_WIDTH - 100)
            y = random.randint(0, SCREEN_HEIGHT - 100)
            self.rooms.append((x, y, 100, 100))  # x, y, w, h