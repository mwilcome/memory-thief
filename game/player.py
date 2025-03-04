# game/player.py
import pygame
from config import PLAYER_SPEED, WORLD_WIDTH, WORLD_HEIGHT

class Player:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.speed = PLAYER_SPEED
        self.hp = 100
        self.corruption = 0
        self.memories = []
        self.radius = 10

    def update(self, dungeon=None):
        keys = pygame.key.get_pressed()
        new_x, new_y = self.x, self.y

        if keys[pygame.K_w]: new_y -= self.speed
        if keys[pygame.K_s]: new_y += self.speed
        if keys[pygame.K_a]: new_x -= self.speed
        if keys[pygame.K_d]: new_x += self.speed

        if dungeon and dungeon.contains(new_x, new_y, self.radius):
            self.x, self.y = new_x, new_y
        self.x = max(self.radius, min(WORLD_WIDTH - self.radius, self.x))
        self.y = max(self.radius, min(WORLD_HEIGHT - self.radius, self.y))