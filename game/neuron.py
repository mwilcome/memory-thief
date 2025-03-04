# game/neuron.py
class Neuron:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.speed = 2

    def update(self, player):
        if self.x < player.x: self.x += self.speed
        if self.x > player.x: self.x -= self.speed
        if self.y < player.y: self.y += self.speed
        if self.y > player.y: self.y -= self.speed