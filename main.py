# main.py
import pygame
from game.engine import GameEngine
from config import SCREEN_WIDTH, SCREEN_HEIGHT

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Memory Thief")
    clock = pygame.time.Clock()
    game = GameEngine(screen)
    game.run(clock)
    pygame.quit()

if __name__ == "__main__":
    main()