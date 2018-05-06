import pygame
from core.game import Game


def launch():
    pygame.init()
    game = Game()
    game.loop()

if __name__ == "__main__":
    launch()
