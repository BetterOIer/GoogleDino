import pygame

class Dino:
    """Manage items about dinosaur"""
    def __init__(self, gd_game):
        self.screen = gd_game.screen
        self.settings = gd_game.settings
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