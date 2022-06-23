import pygame

class Alien:
    def __init__(self, game, x, y):
        self.game  = game
        self.x = x
        self.y = y
        self.size = 30
        self.d = 8
        self.speed = 7

    def move(self):
        self.y += self.speed    

    def draw(self):
        pygame.draw.ellipse( self.game.screen, (240, 233, 12), pygame.Rect(self.x, self.y, self.size, self.size) )
        self.y += 0.3

    def checkCollision(self, game):
        for ray in game.rays:
            if (ray.x < self.x + self.size and
                ray.x > self.x - self.size and
                ray.y < self.y + self.size and
                ray.y > self.y - self.size):
                game.rays.remove( ray )
                game.aliens.remove( self )

