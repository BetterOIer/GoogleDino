import pygame
from pygame.sprite import Sprite
from random import randint,uniform

class Barrier(Sprite):

    def __init__(self,gd_game):
        super().__init__()
        self.screen = gd_game.screen
        self.settings = gd_game.settings
        # self.barriers_group = gd_game.Barries

        self.barriers = ("img\\cactus1.png","img\\cactus2.png","img\\cactus3.png","img\\cactus4.png","img\\cactus5.png","img\\cactus6.png")
        self.choose_barrier = randint(0,5)
        #self.choose_barrier = 4
        self.image = pygame.image.load(self.barriers[self.choose_barrier])
        self.rect = self.image.get_rect()
        self.rect.y = gd_game.bg_y+self.settings.barrier_pos_y
        self.x = float(self.settings.screen_width)
        self.rect.x = int(self.x)
    
    # def update_barrier(self):
    #     self.rand_barrier()
    #     for barrier in self.barriers_group:
    #         barrier.x-=self.settings.barrier_speed
    #         barrier.rect.x=barrier.x
    #         if barrier.rect.x<(-barrier.rect.width):
    #             self.barriers_group.remove(barrier)
    #             print("deleted 1 barrier!!!\n")
    #     self.barriers_group.draw(self.screen)
    
    # def create_barrier(self):
    #     new_barrier = Barrier(self)
    #     self.barriers_group.add(new_barrier)

    # def rand_barrier(self):
    #     if(self.settings.cant_create_barrier == False):
    #         self.barrier_creating_flag = uniform(self.settings.barrier_create_probability_floor,self.settings.barrier_create_probability_ceil)
    #         # print(f"{self.barrier_creating_flag}\n")
    #         if int(self.barrier_creating_flag) == 0:
    #             self._create_barrier()
    #             self.settings.barrier_create_probability_floor-=self.settings.barrier_create_probability_drop_speed
    #             self.settings.cant_create_barrier = True
    #             self.cant_create_barrier_tim=self.settings.cant_create_barrier_tim
    #     else:
    #         self.cant_create_barrier_tim-=self.settings.barrier_cct_countdown_speed
    #         if self.cant_create_barrier_tim<=0:
    #             self.settings.cant_create_barrier=False