# game/memory.py
from config import MEMORY_DURATION, CORRUPTION_MAX

class Memory:
    def __init__(self, ability, duration=MEMORY_DURATION):
        self.ability = ability  # e.g., "speed", "invis"
        self.time_left = duration

    def update(self, dt):
        self.time_left -= dt
        return self.time_left > 0  # True if active

def apply_memory(player, memory):
    if memory.ability == "speed":
        player.speed *= 1.5
    player.corruption += 10
    if player.corruption > CORRUPTION_MAX:
        player.hp -= 10  # Corruption penalty