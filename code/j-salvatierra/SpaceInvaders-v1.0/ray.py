import pygame

class Ray:
    def __init__(self, game, x, y):
        self.game = game
        self.x = x
        self.y = y

    def draw(self):
        pygame.draw.rect( self.game.screen, (200, 22, 10), pygame.Rect(self.x, self.y, 10, 30) )
        self.y -= 7