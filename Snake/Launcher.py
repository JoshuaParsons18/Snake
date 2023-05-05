import pygame

from Game import Game
from Settings import * 

class Launcher:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        self.font = pygame.font.Font(None, 36)
        pygame.display.set_caption("Snake")

        self.game = Game(self.screen, self.font)

        self.running = True

        while(self.running):
            self.game.run()



if __name__ == "__main__":
    launcher = Launcher()