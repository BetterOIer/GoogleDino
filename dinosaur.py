import pygame
from time import sleep

class Dino:
    """Manage items about dinosaur"""
    def __init__(self, gd_game):
        self.screen = gd_game.screen
        self.settings = gd_game.settings
        self.barriers = gd_game.barriers
        self.pteros = gd_game.pteros
        self.screen_rect = gd_game.screen.get_rect()

        self.choose_dino = float(0)
        self.dinos = ("img\\Dino1.png","img\\Dino2.png")
        self.image = pygame.image.load(self.dinos[int(self.choose_dino)])
        self.mask= pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()

        self.rect.midleft = self.screen_rect.midleft
        self.y=float(gd_game.bg_y+self.settings.dino_pos_y)
        self.origin_y = gd_game.bg_y+self.settings.dino_pos_y
        self.rect.x+=(self.settings.screen_width/self.settings.dino_pos_x)
        self.rect.y=self.y
        
        self.jumping_keydown=False
        self.jumping = False
        self.v = float(-self.settings.dino_jumping_speed_origin)

    def blitme(self):
        self.screen.blit(self.image,self.rect)
    
    def update_dino(self):
        if self.jumping_keydown==True:
            self.jumping=True
        if self.jumping==True:
            # print(f"{self.origin_y} {self.v} {self.rect.y} {self.y}\n")
            self.image = pygame.image.load("img\\DinoJumping.png")
            self.v+=self.settings.gravity*self.settings.gravity_offset
            self.y+=self.v
            
            self.rect.y=self.y
            if self.rect.y ==self.origin_y:
                if self.jumping_keydown==False:
                    self.jumping=False
                self.v=float(-self.settings.dino_jumping_speed_origin)
                self.y =  float(self.rect.y)
                # print(f"{self.origin_y} {self.v} {self.rect.y} {self.y}\n")
            
        else:
            self.image = pygame.image.load(self.dinos[int(self.choose_dino)])
            self.choose_dino = self.choose_dino+self.settings.dino_changing_speed
            if self.choose_dino<0:
                self.choose_dino=self.settings.ptero_choose_origin
        self.blitme()
        self.mask= pygame.mask.from_surface(self.image)
        self.collision = pygame.sprite.spritecollide(self, self.barriers, False, pygame.sprite.collide_mask)
        if self.collision:
            sleep(0.001)
        self.collision = pygame.sprite.spritecollide(self, self.pteros, False, pygame.sprite.collide_mask)
        if self.collision:
            sleep(0.001)