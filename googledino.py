import sys

import pygame
from random import uniform
from time import sleep

from settings import Settings
from dinosaur import Dino
from background import Background
from barrier import Barrier
from clouds import Clouds

class GoogleDino:

    def __init__(self):
        """Init game"""
        pygame.init()
        
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_width,self.settings.screen_height))
        pygame.display.set_caption("Google Dino")

        self.background1 = Background(self)
        self.background2 = Background(self)
        self.bg_y = self.background1.rect.y
        self.background2.x+=self.settings.screen_width
        self.background2.rect.x=self.background2.x

        self.dino = Dino(self)

        self.barriers = pygame.sprite.Group()

        self.clouds = pygame.sprite.Group()
    
    def run_game(self):
        
        while(True):
            self._check_events()
            self.screen.fill(self.settings.bg_color)
            self._update_background()

            self._update_clouds()

            self._update_barrier()

            self._update_dino()

            pygame.display.flip()

    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    sys.exit()
                elif event.key == pygame.K_UP or event.key == pygame.K_SPACE:
                    self.dino.jumping_keydown=True
            
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_UP or event.key == pygame.K_SPACE:
                    self.dino.jumping_keydown=False
    
    def _update_dino(self):
        if self.dino.jumping_keydown==True:
            self.dino.jumping=True
        if self.dino.jumping==True:
            # print(f"{self.dino.origin_y} {self.dino.v} {self.dino.rect.y} {self.dino.y}\n")
            self.dino.image = pygame.image.load("img\\DinoJumping.png")
            self.dino.v+=self.settings.gravity*self.settings.gravity_offset
            self.dino.y+=self.dino.v
            
            self.dino.rect.y=self.dino.y
            if self.dino.rect.y ==self.dino.origin_y:
                if self.dino.jumping_keydown==False:
                    self.dino.jumping=False
                self.dino.v=float(-self.settings.dino_jumping_speed_origin)
                self.dino.y =  float(self.dino.rect.y)
                # print(f"{self.dino.origin_y} {self.dino.v} {self.dino.rect.y} {self.dino.y}\n")
            
        else:
            self.dino.image = pygame.image.load(self.dino.dinos[int(self.dino.choose_dino)])
            self.dino.choose_dino = self.dino.choose_dino-0.005
            if self.dino.choose_dino<0:
                self.dino.choose_dino=1.99
        self.dino.blitme()
        self.dino.mask= pygame.mask.from_surface(self.dino.image)
        self.collision = pygame.sprite.spritecollide(self.dino, self.barriers, False,pygame.sprite.collide_mask)
        if self.collision:
            sleep(0.01)
    
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

if __name__ == "__main__":
    gd = GoogleDino()
    gd.run_game()
