# game/dungeon.py
import random
from config import SCREEN_WIDTH, SCREEN_HEIGHT

class Dungeon:
    def __init__(self, num_rooms=5, min_size=50, max_size=100):
        self.rooms = []  # List of (x, y, w, h) tuples
        self.corridors = []  # List of (x1, y1, x2, y2) for lines
        self.num_rooms = num_rooms
        self.min_size = min_size
        self.max_size = max_size
        self.generate()

    def generate(self):
        # Generate random rooms
        for _ in range(self.num_rooms):
            w = random.randint(self.min_size, self.max_size)
            h = random.randint(self.min_size, self.max_size)
            x = random.randint(0, SCREEN_WIDTH - w)
            y = random.randint(0, SCREEN_HEIGHT - h)
            # Avoid overlap (simple check)
            if not self.overlaps(x, y, w, h):
                self.rooms.append((x, y, w, h))

        # Connect rooms with corridors (minimum spanning tree-ish)
        if len(self.rooms) > 1:
            for i in range(len(self.rooms) - 1):
                x1 = self.rooms[i][0] + self.rooms[i][2] // 2  # Center of room i
                y1 = self.rooms[i][1] + self.rooms[i][3] // 2
                x2 = self.rooms[i + 1][0] + self.rooms[i + 1][2] // 2  # Center of room i+1
                y2 = self.rooms[i + 1][1] + self.rooms[i + 1][3] // 2
                self.corridors.append((x1, y1, x2, y2))

    def overlaps(self, x, y, w, h):
        # Check if new room overlaps existing ones (with padding)
        padding = 10
        for rx, ry, rw, rh in self.rooms:
            if (x < rx + rw + padding and x + w + padding > rx and
                y < ry + rh + padding and y + h + padding > ry):
                return True
        return False

    def contains(self, x, y):
        # Check if point (x, y) is inside any room or near a corridor
        for rx, ry, rw, rh in self.rooms:
            if rx <= x <= rx + rw and ry <= y <= ry + rh:
                return True
        # Add corridor collision later if needed
        return False