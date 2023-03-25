import pygame

class Background:
    def __init__(self, gd_game):
        self.screen = gd_game.screen
        self.settings = gd_game.settings
        self.screen_rect = gd_game.screen.get_rect()

        self.image = pygame.image.load("img\\ground.png")
        self.rect = self.image.get_rect()

        self.rect.bottomleft = self.screen_rect.bottomleft
        self.rect.y+=self.settings.background_pos_y
        self.x = float(self.rect.x)
    
    def blitme(self):
        self.screen.blit(self.image,self.rect)
    
    def update_background(self):
        self.x-=self.settings.background_speed
        if self.x<(-self.settings.screen_width):
            self.x=float(self.settings.screen_width)
        self.rect.x=self.x