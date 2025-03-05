# game/engine.py
import pygame
from game.player import Player
from game.dungeon import Dungeon
from game.neuron import Neuron
from utils.render import render_all
from config import SCREEN_WIDTH, SCREEN_HEIGHT, FPS, ZONES, ZONE_MIN_RADIUS, ZONE_MAX_RADIUS, WORLD_WIDTH, WORLD_HEIGHT, NEURON_COUNT, MEMORY_GOAL

class GameEngine:
    def __init__(self, screen):
        self.screen = screen
        self.running = True
        self.font = pygame.font.SysFont(None, 24)  # Regular UI font
        self.win_font = pygame.font.SysFont(None, 72)  # Big victory font
        self.game_over = False
        self.game_over_timer = 0
        self.win = False
        self.win_timer = 0
        self.reset()

    def reset(self):
        """Reset the game state for a new run."""
        self.dungeon = Dungeon()
        self.player = Player(self.dungeon.zones[0][0], self.dungeon.zones[0][1])
        self.neurons = [Neuron(self.dungeon) for _ in range(NEURON_COUNT)]
        self.camera_x = 0
        self.camera_y = 0
        self.boss_unlocked = False
        self.game_over = False
        self.game_over_timer = 0
        self.win = False
        self.win_timer = 0

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
        if not self.game_over and not self.win:
            self.player.update(self.dungeon, self.dungeon.memories, self.boss_unlocked)
            for neuron in self.neurons:
                neuron.update(self.dungeon)
                dist = ((self.player.x - neuron.x) ** 2 + (self.player.y - neuron.y) ** 2) ** 0.5
                if dist < self.player.radius + neuron.radius:
                    self.player.hp -= 10
                    if self.player.hp <= 0:
                        self.game_over = True
                        self.game_over_timer = 180  # 3 seconds at 60 FPS
                        break
            if self.player.memories_collected >= MEMORY_GOAL and not self.boss_unlocked:
                self.dungeon.unlock_boss_room()
                self.boss_unlocked = True
            if self.dungeon.core and self.boss_unlocked:
                cx, cy = self.dungeon.core
                if ((self.player.x - cx) ** 2 + (self.player.y - cy) ** 2) ** 0.5 < self.player.radius + 10:
                    self.win = True
                    self.win_timer = 180  # 3 seconds at 60 FPS
            self.camera_x = max(0, min(WORLD_WIDTH - SCREEN_WIDTH, self.player.x - SCREEN_WIDTH // 2))
            self.camera_y = max(0, min(WORLD_HEIGHT - SCREEN_HEIGHT, self.player.y - SCREEN_HEIGHT // 2))
        elif self.game_over:
            self.game_over_timer -= 1
            if self.game_over_timer <= 0:
                self.reset()
        elif self.win:
            self.win_timer -= 1
            if self.win_timer <= 0:
                self.reset()

    def render(self):
        render_all(self.screen, self.player, self.dungeon, self.neurons, self.dungeon.memories, self.camera_x, self.camera_y, self.boss_unlocked)
        # UI Elements
        memory_text = self.font.render(f"Memories: {self.player.memories_collected}/{MEMORY_GOAL}", True, (255, 255, 255))
        hp_text = self.font.render(f"HP: {self.player.hp}", True, (255, 255, 255))
        self.screen.blit(memory_text, (10, 10))
        self.screen.blit(hp_text, (10, 40))
        if self.boss_unlocked:
            boss_text = self.font.render("Boss Room Unlocked!", True, (255, 255, 0))
            self.screen.blit(boss_text, (10, 70))
        if self.game_over:
            game_over_text = self.font.render("You were overwhelmed! Resetting...", True, (255, 0, 0))
            self.screen.blit(game_over_text, (SCREEN_WIDTH // 2 - 100, SCREEN_HEIGHT // 2))
        if self.win:
            win_text = self.win_font.render("Victory! Core Secured!", True, (0, 255, 0))
            self.screen.blit(win_text, (SCREEN_WIDTH // 2 - 200, SCREEN_HEIGHT // 2 - 36))
        pygame.display.flip()