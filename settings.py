class Settings:
    """Settings"""
    def __init__(self):
        self.screen_width = 1284
        self.screen_height = 220
        self.bg_color = (255,255,255)
        
        self.button_width,self.button_height = 100,50
        self.button_color = (172, 171, 176)
        self.button_text_color = (255, 255, 255)
        self.button_text_size = 36
        self.button_text_font_family = "Consolas"

        self.score_width,self.score_height = 200,50
        self.score_text_color = (172, 171, 176)
        self.score_text_size = 24
        self.score_text_font_family = "Consolas"
        self.score_origin = 0
        self.score_rise_speed = 10

        self.dino_each_jumping_time = 0.5
        self.dino_FPS = 60
        self.dino_max_jumping_height = 50
        self.dino_pos_x = 5
        self.dino_pos_y = -35
        self.gravity=1.0*4*self.dino_max_jumping_height/(self.dino_each_jumping_time*self.dino_each_jumping_time*self.dino_FPS*self.dino_FPS)
        self.dino_jumping_speed_origin = 1.0*4*self.dino_max_jumping_height/(self.dino_each_jumping_time*self.dino_FPS)
        self.dino_changing_speed = -0.1
        self.dino_choose_origin = 1.99999999999999
        self.dino_y_ducking_offset= 13

        self.barrier_pos_y = -34
        self.barrier_speed = 2.5
        self.cant_create_barrier = False
        self.cant_create_barrier_tim = 10
        self.barrier_cct_countdown_speed = 0.1
        self.barrier_create_probability_drop_speed = 0.0001
        self.barrier_create_probability_floor = 0.99
        self.barrier_create_probability_ceil = 1.999999999999
        
        self.clouds_pos_y=(-75,-90,-105)
        self.cloud_scale = ((50,20),(37.5,15),(25,10))
        self.cant_create_clouds = False
        self.clouds_create_probability_floor = 0.99
        self.clouds_create_probability_ceil = 1.999
        self.cant_create_clouds_tim = 10
        self.clouds_cct_countdown_speed = 0.1
        self.cloud_speed = (2.3,2.0,1.7)
        
        self.pteros_pos_y=-55
        self.cant_create_ptero = False
        self.cant_create_ptero_tim = 60
        self.ptero_create_probability_floor = 0.99
        self.ptero_create_probability_ceil = 1.999
        self.ptero_cct_countdown_speed = 0.1
        self.ptero_speed = 3
        self.ptero_changing_speed = -0.05
        self.ptero_choose_origin = 1.9999

        self.background_pos_y = -50
        self.background_speed = 2.5
        