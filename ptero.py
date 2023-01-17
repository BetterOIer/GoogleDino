import pygame
from pygame.sprite import Sprite
from random import randint

class Ptero(Sprite):

    def __init__(self,gd_game):
        super().__init__()
        self.secreen = gd_game.screen
        self.settings = gd_game.settings

        self.pteros = ("img\\Ptero1.png","img\\Ptero2.png")
        self.choose_ptero = float(0)
        self.image = pygame.image.load(self.pteros[int(self.choose_ptero)])
        self.rect = self.image.get_rect()
        self.rect.y = gd_game.bg_y+self.settings.pteros_pos_y
        self.x = float(self.settings.screen_width)
        self.rect.x = int(self.x)