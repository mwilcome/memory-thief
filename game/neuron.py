# game/neuron.py
import random
from config import NEURON_SPEED, WORLD_WIDTH, WORLD_HEIGHT

class Neuron:
    def __init__(self, dungeon):
        zone = random.choice(dungeon.zones)
        x, y, radius = zone
        self.x = random.randint(x - radius + 15, x + radius - 15)
        self.y = random.randint(y - radius + 15, y + radius - 15)
        self.speed = NEURON_SPEED
        self.radius = 15

    def update(self, player, dungeon):
        if dungeon.contains(self.x, self.y, self.radius):
            dx = player.x - self.x
            dy = player.y - self.y
            dist = max((dx ** 2 + dy ** 2) ** 0.5, 1)
            if dist > self.radius + player.radius:
                self.x += (dx / dist) * self.speed
                self.y += (dy / dist) * self.speed
        self.x = max(self.radius, min(WORLD_WIDTH - self.radius, self.x))
        self.y = max(self.radius, min(WORLD_HEIGHT - self.radius, self.y))

    def drop_memory(self):
        return (self.x, self.y)