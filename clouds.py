import pygame
from pygame.sprite import Sprite
from random import randint

class Clouds(Sprite):
    def __init__(self,gd_game):
        super().__init__()
        self.screen = gd_game.screen
        self.settings = gd_game.settings

        self.image = pygame.image.load("img\\cloud.png")
        self.rect = self.image.get_rect()
        self.choose = randint(0,2)
        self.rect.y = gd_game.bg_y+self.settings.clouds_pos_y[self.choose]
        self.image = pygame.transform.smoothscale(self.image,self.settings.cloud_scale[self.choose])
        self.x = float(self.settings.screen_width)
        self.rect.x = int(self.x)
    