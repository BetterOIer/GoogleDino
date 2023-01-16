import pygame
from pygame.sprite import Sprite
from random import randint

class Barrier(Sprite):

    def __init__(self,gd_game):
        super().__init__()
        self.screen = gd_game.screen
        self.settings = gd_game.settings

        self.barriers = ("img\\cactus1.png","img\\cactus2.png","img\\cactus3.png","img\\cactus4.png","img\\cactus5.png","img\\cactus6.png")
        self.choose_barrier = randint(0,5)
        #self.choose_barrier = 4
        self.image = pygame.image.load(self.barriers[self.choose_barrier])
        self.rect = self.image.get_rect()
        self.rect.y = gd_game.bg_y+self.settings.barrier_pos_y
        self.x = float(self.settings.screen_width)
        self.rect.x = int(self.x)

