# game/engine.py
from game.player import Player
from game.dungeon import Dungeon
from utils.render import render_all

class GameEngine:
    def __init__(self, screen):
        self.screen = screen
        self.running = True
        self.player = Player(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
        self.dungeon = Dungeon()
        self.neurons = []  # Populate later

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
        self.player.update()
        # Update neurons, memories, etc.

    def render(self):
        render_all(self.screen, self.player, self.dungeon, self.neurons)