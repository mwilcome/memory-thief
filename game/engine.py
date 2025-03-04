# game/engine.py
import pygame
from game.player import Player
from game.dungeon import Dungeon
from utils.render import render_all
from config import SCREEN_WIDTH, SCREEN_HEIGHT, FPS, ZONES, ZONE_MIN_RADIUS, ZONE_MAX_RADIUS, WORLD_WIDTH, WORLD_HEIGHT

class GameEngine:
    def __init__(self, screen):
        self.screen = screen
        self.running = True
        self.dungeon = Dungeon(ZONES, ZONE_MIN_RADIUS, ZONE_MAX_RADIUS)
        self.player = Player(self.dungeon.zones[0][0], self.dungeon.zones[0][1])
        self.neurons = []
        self.camera_x = 0
        self.camera_y = 0

    def run(self, clock):
        while self.running:
            self.handle_input()
            self.update()
            self.render()
            clock.tick(FPS)

    def handle_input(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

    def update(self):
        self.player.update(self.dungeon)
        self.camera_x = max(0, min(WORLD_WIDTH - SCREEN_WIDTH, self.player.x - SCREEN_WIDTH // 2))
        self.camera_y = max(0, min(WORLD_HEIGHT - SCREEN_HEIGHT, self.player.y - SCREEN_HEIGHT // 2))

    def render(self):
        render_all(self.screen, self.player, self.dungeon, self.neurons, self.camera_x, self.camera_y)