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
        self.home_zone = zone  # Keep track of spawn zone
        self.angle = random.uniform(0, 2 * math.pi)  # Random direction

    def update(self, dungeon):
        # Move in current direction
        new_x = self.x + math.cos(self.angle) * self.speed
        new_y = self.y + math.sin(self.angle) * self.speed
        
        # Bounce if hitting zone "wall" or leaving containment
        if not dungeon.contains(new_x, new_y, self.radius) or not self.in_home_zone(new_x, new_y):
            self.angle += math.pi  # Reverse direction (bounce)
            new_x = self.x + math.cos(self.angle) * self.speed  # Recalculate with bounce
            new_y = self.y + math.sin(self.angle) * self.speed
            # Slight random tweak to avoid repetition
            self.angle += random.uniform(-0.5, 0.5)
        
        # Ensure movement stays valid
        if dungeon.contains(new_x, new_y, self.radius) and self.in_home_zone(new_x, new_y):
            self.x, self.y = new_x, new_y
        
        self.x = max(self.radius, min(WORLD_WIDTH - self.radius, self.x))
        self.y = max(self.radius, min(WORLD_HEIGHT - self.radius, self.y))

    def in_home_zone(self, x, y):
        # Check if still within home zone boundaries
        zx, zy, zr = self.home_zone
        dist = ((x - zx) ** 2 + (y - zy) ** 2) ** 0.5
        return dist + self.radius <= zr

    def drop_memory(self):
        return (self.x, self.y)