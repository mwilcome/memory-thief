# utils/render.py
import pygame
from config import COLORS, SCREEN_WIDTH, SCREEN_HEIGHT

def render_all(screen, player, dungeon, neurons):
    screen.fill(COLORS["BACKGROUND"])
    # Draw dungeon rooms
    for room in dungeon.rooms:
        pygame.draw.rect(screen, (50, 50, 50), room)  # Gray rooms
    # Draw corridors
    for x1, y1, x2, y2 in dungeon.corridors:
        pygame.draw.line(screen, (80, 80, 80), (x1, y1), (x2, y2), 5)  # Thicker gray lines
    # Draw player
    pygame.draw.rect(screen, COLORS["PLAYER"], (player.x, player.y, 20, 20))
    # Draw neurons
    for neuron in neurons:
        pygame.draw.rect(screen, COLORS["NEURON"], (neuron.x, neuron.y, 15, 15))
    pygame.display.flip()