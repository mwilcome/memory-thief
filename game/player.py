# game/player.py
import pygame
from config import PLAYER_SPEED, WORLD_WIDTH, WORLD_HEIGHT, FPS
from game.memory import apply_memory

class Player:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.base_speed = PLAYER_SPEED
        self.speed = PLAYER_SPEED
        self.hp = 100
        self.corruption = 0
        self.memories = []
        self.radius = 10

    def update(self, dungeon=None, neurons=None, memories=None):
        keys = pygame.key.get_pressed()
        new_x, new_y = self.x, self.y

        if keys[pygame.K_w]: new_y -= self.speed
        if keys[pygame.K_s]: new_y += self.speed
        if keys[pygame.K_a]: new_x -= self.speed
        if keys[pygame.K_d]: new_x += self.speed

        if not dungeon or dungeon.contains(new_x, new_y, self.radius):
            self.x, self.y = new_x, new_y
        self.x = max(self.radius, min(WORLD_WIDTH - self.radius, self.x))
        self.y = max(self.radius, min(WORLD_HEIGHT - self.radius, self.y))

        dt = 1 / FPS
        self.memories = [m for m in self.memories if m.update(dt)]
        if not any(m.ability == "speed" for m in self.memories):
            self.speed = self.base_speed

        if memories:
            for i, mem in enumerate(memories):
                dist = ((self.x - mem.x) ** 2 + (self.y - mem.y) ** 2) ** 0.5
                if dist < self.radius + mem.radius:
                    apply_memory(self, mem)
                    memories.pop(i)
                    break