# game/neuron.py
import random
import math
from config import NEURON_SPEED, WORLD_WIDTH, WORLD_HEIGHT

class Neuron:
    def __init__(self, dungeon):
        zone = random.choice(dungeon.zones)
        x, y, radius = zone
        self.x = random.randint(x - radius + 15, x + radius - 15)
        self.y = random.randint(y - radius + 15, y + radius - 15)
        self.speed = NEURON_SPEED
        self.radius = 15
        self.home_zone = zone
        self.angle = random.uniform(0, 2 * math.pi)

    def update(self, dungeon):
        new_x = self.x + math.cos(self.angle) * self.speed
        new_y = self.y + math.sin(self.angle) * self.speed
        if not dungeon.contains(new_x, new_y, self.radius) or not self.in_home_zone(new_x, new_y):
            self.angle += math.pi  # Bounce
            new_x = self.x + math.cos(self.angle) * self.speed
            new_y = self.y + math.sin(self.angle) * self.speed
            self.angle += random.uniform(-0.5, 0.5)
        if dungeon.contains(new_x, new_y, self.radius) and self.in_home_zone(new_x, new_y):
            self.x, self.y = new_x, new_y
        self.x = max(self.radius, min(WORLD_WIDTH - self.radius, self.x))
        self.y = max(self.radius, min(WORLD_HEIGHT - self.radius, self.y))

    def in_home_zone(self, x, y):
        zx, zy, zr = self.home_zone
        dist = ((x - zx) ** 2 + (y - zy) ** 2) ** 0.5
        return dist + self.radius <= zr