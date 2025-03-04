# utils/render.py
from config import COLORS, SCREEN_WIDTH, SCREEN_HEIGHT

def render_all(screen, player, dungeon, neurons):
    screen.fill(COLORS["BACKGROUND"])
    # Draw dungeon rooms
    for room in dungeon.rooms:
        pygame.draw.rect(screen, (50, 50, 50), room)
    # Draw player
    pygame.draw.rect(screen, COLORS["PLAYER"], (player.x, player.y, 20, 20))
    # Draw neurons
    for neuron in neurons:
        pygame.draw.rect(screen, COLORS["NEURON"], (neuron.x, neuron.y, 15, 15))
    pygame.display.flip()