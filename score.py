import pygame.font

class Score:

    def __init__(self, gd_game):
        self.screen = gd_game.screen
        self.settings = gd_game.settings
        self.screen_rect = self.screen.get_rect()

        self.font = pygame.font.SysFont(self.settings.score_text_font_family, self.settings.score_text_size)

        self.rect = pygame.Rect(0,0,self.settings.score_width,self.settings.score_height)
        self.rect.right = self.screen_rect.right

        self.score = self.settings.score_origin
    
    def update_score(self):
        self.score = self.score+self.settings.score_rising_speed
        self._prep_msg(str(self.score))
        
    
    def _prep_msg(self,msg):
        self.msg_image = self.font.render(msg,True, self.settings.score_text_color, self.settings.score_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center
    
    def draw_score(self):
        self.screen.fill(self.settings.score_color,self.rect)
        self.screen.blit(self.msg_image,self.msg_image_rect)