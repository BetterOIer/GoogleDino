import sys

import pygame
from random import uniform
from time import sleep

from settings import Settings
from dinosaur import Dino
from background import Background
from barrier import Barrier
from clouds import Clouds
from ptero import Ptero
from stats import Stats

class GoogleDino:

    def __init__(self):
        """Init game"""
        pygame.init()
        self.clock = pygame.time.Clock()  
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_width,self.settings.screen_height))
        pygame.display.set_caption("Google Dino")

        self.stats = Stats()

        self.background1 = Background(self)
        self.background2 = Background(self)
        self.bg_y = self.background1.rect.y
        self.background2.x+=self.settings.screen_width
        self.background2.rect.x=self.background2.x

        self.barriers = pygame.sprite.Group()

        self.pteros = pygame.sprite.Group()

        self.clouds = pygame.sprite.Group()

        self.dino = Dino(self)
    
    def run_game(self):
        while True:
            self._check_events()
            if self.stats.game_active==True:
                self._update_game()
                pygame.display.flip()
            self.clock.tick(120)

    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    sys.exit()
                elif self.stats.game_active == True:
                    if event.key == pygame.K_UP or event.key == pygame.K_SPACE:
                        self.dino.jumping_keydown=True
                    elif event.key == pygame.K_DOWN:
                        if self.dino.jumping == False:
                            self.dino.ducking_keydown=True
                elif event.key == pygame.K_SPACE:
                    self.stats.game_active = True
            
            elif event.type == pygame.KEYUP:
                if self.stats.game_active==True:
                    if event.key == pygame.K_UP or event.key == pygame.K_SPACE:
                        self.dino.jumping_keydown=False
                    elif event.key == pygame.K_DOWN:
                        self.dino.ducking_keydown=False
    
    def _update_game(self):

        self._update_screen()

        self._update_background()

        self._update_clouds()

        self._update_barrier()
            
        self._update_ptero()

        self.dino.update_dino()
    
    def _update_screen(self):
        self.screen.fill(self.settings.bg_color)

    def _update_background(self):
        self.background1.x-=self.settings.background_speed
        if self.background1.x<(-self.settings.screen_width):
            self.background1.x=float(self.settings.screen_width)
        self.background1.rect.x=self.background1.x
        self.background2.x-=self.settings.background_speed
        if self.background2.x<(-self.settings.screen_width):
            self.background2.x=float(self.settings.screen_width)
        self.background2.rect.x=self.background2.x
        self.background1.blitme()
        self.background2.blitme()

    def _create_clouds(self):
        new_clouds = Clouds(self)
        self.clouds.add(new_clouds)

    def _rand_clouds(self):
        if(self.settings.cant_create_clouds==False):
            self.clouds_creating_flag = uniform(self.settings.clouds_create_probability_floor,self.settings.clouds_create_probability_ceil)
            #print(f"{self.clouds_creating_flag}\n")
            if int(self.clouds_creating_flag) == 0:
                self._create_clouds()
                self.settings.cant_create_clouds = True
                self.cant_create_clouds_tim=self.settings.cant_create_clouds_tim
        else:
            self.cant_create_clouds_tim-=self.settings.clouds_cct_countdown_speed
            #print(f"{self.cant_create_clouds_tim}\n")
            if int(self.cant_create_clouds_tim)<=0:
                self.settings.cant_create_clouds=False
    
    def _update_clouds(self):
        self._rand_clouds()
        for cloud in self.clouds:
            cloud.x-=self.settings.cloud_speed[cloud.choose]
            cloud.rect.x=cloud.x
            if cloud.rect.x<(-cloud.rect.width):
                self.clouds.remove(cloud)
                #print("deleted 1 cloud!!!\n")
        self.clouds.draw(self.screen) 

    def _update_barrier(self):
        self._rand_barrier()
        for barrier in self.barriers:
            barrier.x-=self.settings.barrier_speed
            barrier.rect.x=barrier.x
            if barrier.rect.x<(-barrier.rect.width):
                self.barriers.remove(barrier)
                #print("deleted 1 barrier!!!\n")
        self.barriers.draw(self.screen)
    
    def _create_barrier(self):
        new_barrier = Barrier(self)
        self.barriers.add(new_barrier)

    def _rand_barrier(self):
        if(self.settings.cant_create_barrier == False):
            self.barrier_creating_flag = uniform(self.settings.barrier_create_probability_floor,self.settings.barrier_create_probability_ceil)
            # print(f"{self.barrier_creating_flag}\n")
            if int(self.barrier_creating_flag) == 0:
                self._create_barrier()
                self.settings.barrier_create_probability_floor-=self.settings.barrier_create_probability_drop_speed
                self.settings.cant_create_barrier = True
                self.cant_create_barrier_tim=self.settings.cant_create_barrier_tim
        else:
            self.cant_create_barrier_tim-=self.settings.barrier_cct_countdown_speed
            if self.cant_create_barrier_tim<=0:
                self.settings.cant_create_barrier=False
    
    def _create_ptero(self):
        new_ptero = Ptero(self)
        self.pteros.add(new_ptero)

    def _rand_ptero(self):
        if(self.settings.cant_create_ptero==False):
            self.ptero_creating_flag = uniform(self.settings.ptero_create_probability_floor,self.settings.ptero_create_probability_ceil)
            #print(f"{self.ptero_creating_flag}\n")
            if int(self.ptero_creating_flag) == 0:
                self._create_ptero()
                self.settings.cant_create_ptero = True
                self.cant_create_ptero_tim=self.settings.cant_create_ptero_tim
        else:
            self.cant_create_ptero_tim-=self.settings.ptero_cct_countdown_speed
            #print(f"{self.cant_create_ptero_tim}\n")
            if int(self.cant_create_ptero_tim)<=0:
                self.settings.cant_create_ptero = False

    def _update_ptero(self):
        self._rand_ptero()
        for ptero in self.pteros:
            ptero.image = pygame.image.load(ptero.pteros[int(ptero.choose_ptero)])
            ptero.choose_ptero = ptero.choose_ptero+self.settings.ptero_changing_speed
            if ptero.choose_ptero<0:
                ptero.choose_ptero=self.settings.ptero_choose_origin
            ptero.x-=self.settings.ptero_speed
            ptero.rect.x=ptero.x
            if ptero.rect.x<(-ptero.rect.width):
                self.pteros.remove(ptero)
                # print("deleted 1 ptero!!!\n")
        self.pteros.draw(self.screen)

if __name__ == "__main__":
    gd = GoogleDino()
    gd.run_game()
