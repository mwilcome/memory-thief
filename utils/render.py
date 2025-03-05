import pygame
from config import COLORS, SCREEN_WIDTH, SCREEN_HEIGHT, BRIDGE_WIDTH

def render_all(screen, player, dungeon, neurons, memories, camera_x, camera_y, boss_unlocked):
    screen.fill(COLORS["BACKGROUND"])
    for x, y, radius in dungeon.zones:
        pygame.draw.circle(screen, COLORS["ZONE"], (int(x - camera_x), int(y - camera_y)), radius)
    for x1, y1, x2, y2 in dungeon.bridges:
        pygame.draw.line(screen, COLORS["BRIDGE"], (int(x1 - camera_x), int(y1 - camera_y)), (int(x2 - camera_x), int(y2 - camera_y)), BRIDGE_WIDTH)
    if dungeon.boss_room and boss_unlocked:
        bx, by, br = dungeon.boss_room
        pygame.draw.circle(screen, COLORS["BOSS_ZONE"], (int(bx - camera_x), int(by - camera_y)), br)
        if dungeon.core:
            cx, cy = dungeon.core
            pygame.draw.circle(screen, (255, 255, 0), (int(cx - camera_x), int(cy - camera_y)), 10)  # Yellow core
        if dungeon.boss_bridge:
            x1, y1, x2, y2 = dungeon.boss_bridge
            pygame.draw.line(screen, COLORS["BRIDGE"], (int(x1 - camera_x), int(y1 - camera_y)), (int(x2 - camera_x), int(y2 - camera_y)), BRIDGE_WIDTH)
    for mem in memories:
        pygame.draw.circle(screen, COLORS["MEMORY"], (int(mem[0] - camera_x), int(mem[1] - camera_y)), 8)
    for neuron in neurons:
        pygame.draw.circle(screen, COLORS["NEURON"], (int(neuron.x - camera_x), int(neuron.y - camera_y)), neuron.radius)
    pygame.draw.circle(screen, COLORS["PLAYER"], (int(player.x - camera_x), int(player.y - camera_y)), player.radius)