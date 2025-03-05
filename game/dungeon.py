# game/dungeon.py
import random
from config import WORLD_WIDTH, WORLD_HEIGHT, ZONES, ZONE_MIN_RADIUS, ZONE_MAX_RADIUS, BRIDGE_WIDTH

class Dungeon:
    def __init__(self, num_zones=ZONES, min_radius=ZONE_MIN_RADIUS, max_radius=ZONE_MAX_RADIUS):
        self.zones = []
        self.bridges = []
        self.num_zones = num_zones
        self.min_radius = min_radius
        self.max_radius = max_radius
        self.generate()

    def generate(self):
        attempts = 0
        max_attempts = self.num_zones * 10
        while len(self.zones) < self.num_zones and attempts < max_attempts:
            radius = random.randint(self.min_radius, self.max_radius)
            x = random.randint(radius, WORLD_WIDTH - radius)
            y = random.randint(radius, WORLD_HEIGHT - radius)
            if not self.overlaps(x, y, radius):
                self.zones.append((x, y, radius))
            attempts += 1
        if len(self.zones) > 1:
            for i in range(len(self.zones) - 1):
                x1, y1 = self.zones[i][0], self.zones[i][1]
                x2, y2 = self.zones[i + 1][0], self.zones[i + 1][1]
                self.bridges.append((x1, y1, x2, y2))

    def overlaps(self, x, y, radius):
        padding = 30
        for zx, zy, zr in self.zones:
            dist = ((x - zx) ** 2 + (y - zy) ** 2) ** 0.5
            if dist < (radius + zr + padding):
                return True
        return False

    def contains(self, x, y, radius=10):
        for zx, zy, zr in self.zones:
            dist = ((x - zx) ** 2 + (y - zy) ** 2) ** 0.5
            if dist + radius <= zr:
                return True
        for x1, y1, x2, y2 in self.bridges:
            dx, dy = x2 - x1, y2 - y1
            length = max((dx ** 2 + dy ** 2) ** 0.5, 1)
            t = max(0, min(1, ((x - x1) * dx + (y - y1) * dy) / length ** 2))
            proj_x = x1 + t * dx
            proj_y = y1 + t * dy
            dist_to_line = ((x - proj_x) ** 2 + (y - proj_y) ** 2) ** 0.5
            if dist_to_line <= BRIDGE_WIDTH / 2 + radius:
                return True
        return False