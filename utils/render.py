# utils/render.py
import pygame
from config import COLORS, SCREEN_WIDTH, SCREEN_HEIGHT, BRIDGE_WIDTH

def render_all(screen, player, dungeon, neurons, memories, camera_x, camera_y):
    screen.fill(COLORS["BACKGROUND"])
    for x, y, radius in dungeon.zones:
        pygame.draw.circle(screen, COLORS["ZONE"], (x - camera_x, y - camera_y), radius)
    for x1, y1, x2, y2 in dungeon.bridges:
        pygame.draw.line(screen, COLORS["BRIDGE"], (x1 - camera_x, y1 - camera_y), (x2 - camera_x, y2 - camera_y), BRIDGE_WIDTH)
    for mem in memories:
        pygame.draw.circle(screen, COLORS["MEMORY"], (mem.x - camera_x, mem.y - camera_y), mem.radius)
    pygame.draw.circle(screen, COLORS["PLAYER"], (player.x - camera_x, player.y - camera_y), player.radius)
    for neuron in neurons:
        pygame.draw.circle(screen, COLORS["NEURON"], (neuron.x - camera_x, neuron.y - camera_y), neuron.radius)
    pygame.display.flip()