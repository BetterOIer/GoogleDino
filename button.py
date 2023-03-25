import pygame.font

class Button:

    def __init__(self, gd_game, msg):
        self.screen = gd_game.screen
        self.settings = gd_game.settings
        self.screen_rect = self.screen.get_rect()

        self.font = pygame.font.SysFont(self.settings.button_text_font_family, self.settings.button_text_size)

        self.rect = pygame.Rect(0,0,self.settings.button_width,self.settings.button_height)
        self.rect.center = self.screen_rect.center

        self._prep_msg(msg)
    
    def _prep_msg(self,msg):
        self.msg_image = self.font.render(msg,True, self.settings.button_text_color, self.settings.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center
    
    def draw_button(self):
        self.screen.fill(self.settings.button_color,self.rect)
        self.screen.blit(self.msg_image,self.msg_image_rect)