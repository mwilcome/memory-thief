# game/dungeon.py
import random
from config import WORLD_WIDTH, WORLD_HEIGHT, ZONE_MIN_COUNT, ZONE_MAX_COUNT, ZONE_MIN_RADIUS, ZONE_MAX_RADIUS, BRIDGE_WIDTH

class Dungeon:
    def __init__(self, min_zones=ZONE_MIN_COUNT, max_zones=ZONE_MAX_COUNT, min_radius=ZONE_MIN_RADIUS, max_radius=ZONE_MAX_RADIUS):
        self.zones = []
        self.bridges = []
        self.min_zones = min_zones
        self.max_zones = max_zones
        self.num_zones = random.randint(self.min_zones, self.max_zones)  # Random within range
        self.min_radius = min_radius
        self.max_radius = max_radius
        self.generate()

    def generate(self):
        attempts = 0
        max_attempts = self.num_zones * 10
        sizes = [self.max_radius] * (self.num_zones // 2) + [self.min_radius] * (self.num_zones - self.num_zones // 2)
        random.shuffle(sizes)
        while len(self.zones) < self.num_zones and attempts < max_attempts:
            radius = sizes[len(self.zones)] if len(self.zones) < len(sizes) else random.randint(self.min_radius, self.max_radius)
            x = random.randint(radius, WORLD_WIDTH - radius)
            y = random.randint(radius, WORLD_HEIGHT - radius)
            if not self.overlaps(x, y, radius):
                self.zones.append((x, y, radius))
            attempts += 1
        # Ensure at least min_zones
        while len(self.zones) < self.min_zones:
            radius = random.randint(self.min_radius, self.max_radius)
            x = random.randint(radius, WORLD_WIDTH - radius)
            y = random.randint(radius, WORLD_HEIGHT - radius)
            if not self.overlaps(x, y, radius):
                self.zones.append((x, y, radius))
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