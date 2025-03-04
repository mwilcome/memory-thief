# utils/render.py
import pygame
from config import COLORS, SCREEN_WIDTH, SCREEN_HEIGHT, BRIDGE_WIDTH

def render_all(screen, player, dungeon, neurons, camera_x, camera_y):
    screen.fill(COLORS["BACKGROUND"])
    for x, y, radius in dungeon.zones:
        pygame.draw.circle(screen, COLORS["ZONE"], (x - camera_x, y - camera_y), radius)
    for x1, y1, x2, y2 in dungeon.bridges:
        pygame.draw.line(screen, COLORS["BRIDGE"], (x1 - camera_x, y1 - camera_y), (x2 - camera_x, y2 - camera_y), BRIDGE_WIDTH)
    pygame.draw.circle(screen, COLORS["PLAYER"], (player.x - camera_x, player.y - camera_y), player.radius)
    for neuron in neurons:
        pygame.draw.rect(screen, COLORS["NEURON"], (neuron.x - camera_x, neuron.y - camera_y, 15, 15))
    pygame.display.flip()