# game/dungeon.py
import random
import math
from config import WORLD_WIDTH, WORLD_HEIGHT, ZONES, ZONE_MIN_RADIUS, ZONE_MAX_RADIUS, BRIDGE_WIDTH, BOSS_ROOM_RADIUS, MEMORY_GOAL

class Dungeon:
    def __init__(self):
        self.zones = []
        self.bridges = []
        self.memories = []  # Pre-placed blue memories
        self.boss_room = None
        self.boss_bridge = None
        self.core = None  # Core in boss room
        self.generate()

    def generate(self):
        attempts = 0
        max_attempts = ZONES * 10
        while len(self.zones) < ZONES and attempts < max_attempts:
            radius = random.randint(ZONE_MIN_RADIUS, ZONE_MAX_RADIUS)
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
        # Place memories in zones
        for zone in self.zones:
            num_memories = random.randint(1, 3)
            for _ in range(num_memories):
                angle = random.uniform(0, 2 * math.pi)
                r = random.uniform(0, zone[2] - 10)
                mem_x = zone[0] + r * math.cos(angle)
                mem_y = zone[1] + r * math.sin(angle)
                self.memories.append((mem_x, mem_y))

    def overlaps(self, x, y, radius):
        padding = 30
        for zx, zy, zr in self.zones:
            dist = ((x - zx) ** 2 + (y - zy) ** 2) ** 0.5
            if dist < (radius + zr + padding):
                return True
        return False

    def contains(self, x, y, radius=10, boss_unlocked=False):
        for zx, zy, zr in self.zones:
            dist = ((x - zx) ** 2 + (y - zy) ** 2) ** 0.5
            if dist + radius <= zr:
                return True
        if self.boss_room and boss_unlocked:
            bx, by, br = self.boss_room
            dist = ((x - bx) ** 2 + (y - by) ** 2) ** 0.5
            if dist + radius <= br:
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
        if self.boss_bridge and boss_unlocked:
            x1, y1, x2, y2 = self.boss_bridge
            dx, dy = x2 - x1, y2 - y1
            length = max((dx ** 2 + dy ** 2) ** 0.5, 1)
            t = max(0, min(1, ((x - x1) * dx + (y - y1) * dy) / length ** 2))
            proj_x = x1 + t * dx
            proj_y = y1 + t * dy
            dist_to_line = ((x - proj_x) ** 2 + (y - proj_y) ** 2) ** 0.5
            if dist_to_line <= BRIDGE_WIDTH / 2 + radius:
                return True
        return False

    def unlock_boss_room(self):
        if self.boss_room is None:
            attempts = 0
            while attempts < 100:
                radius = BOSS_ROOM_RADIUS
                x = random.randint(radius, WORLD_WIDTH - radius)
                y = random.randint(radius, WORLD_HEIGHT - radius)
                if not self.overlaps(x, y, radius):
                    self.boss_room = (x, y, radius)
                    self.core = (x, y)  # Core at center
                    last_zone = self.zones[-1]
                    self.boss_bridge = (last_zone[0], last_zone[1], x, y)
                    break
                attempts += 1