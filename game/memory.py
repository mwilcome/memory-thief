# game/memory.py
from config import MEMORY_DURATION, MEMORY_CORRUPTION, CORRUPTION_MAX

class Memory:
    def __init__(self, x, y, duration=MEMORY_DURATION):
        self.x = x
        self.y = y
        self.ability = "speed"
        self.time_left = duration
        self.radius = 8

    def update(self, dt):
        self.time_left -= dt
        return self.time_left > 0

def apply_memory(player, memory):
    if memory.ability == "speed":
        player.speed += 2
    player.corruption += MEMORY_CORRUPTION
    if player.corruption > CORRUPTION_MAX:
        player.hp -= 10
        player.corruption = CORRUPTION_MAX
    player.memories.append(memory)