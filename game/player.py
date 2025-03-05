# game/player.py
import pygame
from config import PLAYER_SPEED, WORLD_WIDTH, WORLD_HEIGHT, FPS, MEMORY_GOAL

class Player:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.speed = PLAYER_SPEED
        self.hp = 100
        self.corruption = 0
        self.memories_collected = 0
        self.radius = 10
        self.last_hit_time = 0  # Time of last damage in milliseconds

    def update(self, dungeon, memories, boss_unlocked):
        keys = pygame.key.get_pressed()
        new_x, new_y = self.x, self.y

        if keys[pygame.K_w]: new_y -= self.speed
        if keys[pygame.K_s]: new_y += self.speed
        if keys[pygame.K_a]: new_x -= self.speed
        if keys[pygame.K_d]: new_x += self.speed

        if dungeon.contains(new_x, new_y, self.radius, boss_unlocked):
            self.x, self.y = new_x, new_y
        self.x = max(self.radius, min(WORLD_WIDTH - self.radius, self.x))
        self.y = max(self.radius, min(WORLD_HEIGHT - self.radius, self.y))

        # Check for memory collection
        for i, mem in enumerate(memories):
            dist = ((self.x - mem[0]) ** 2 + (self.y - mem[1]) ** 2) ** 0.5
            if dist < self.radius + 8:
                self.memories_collected += 1
                memories.pop(i)
                break