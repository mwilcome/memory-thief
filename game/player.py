# game/player.py
import pygame
from config import PLAYER_SPEED, SCREEN_WIDTH, SCREEN_HEIGHT  # Add SCREEN imports

class Player:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.speed = PLAYER_SPEED
        self.hp = 100
        self.corruption = 0
        self.memories = []  # Active memory effects

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]: self.y -= self.speed
        if keys[pygame.K_s]: self.y += self.speed
        if keys[pygame.K_a]: self.x -= self.speed
        if keys[pygame.K_d]: self.x += self.speed
        # Clamp to screen
        self.x = max(0, min(SCREEN_WIDTH - 20, self.x))
        self.y = max(0, min(SCREEN_HEIGHT - 20, self.y))