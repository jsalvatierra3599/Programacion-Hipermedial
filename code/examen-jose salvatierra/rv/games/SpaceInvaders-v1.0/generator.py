from alien import Alien

class Generator:
    def __init__(self, game):
        self.margin = 80
        self.width = 180

        for x in range(self.margin, game.width - self.margin, self.width):
            for y in range(self.margin, int(game.height/2), self.width):
                game.aliens.append( Alien(game, x, y) )