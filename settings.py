class Settings:
    """Settings"""
    def __init__(self):
        self.screen_width = 1284
        self.screen_height = 240
        self.bg_color = (255,255,255)
        self.gravity=float(256/2160)

        self.dino_pos_x = 5
        self.dino_pos_y = -35
        self.dino_jumping_speed_origin = (16/3)
        self.dino_changing_speed = -0.05
        self.dino_choose_origin = 1.99

        self.barrier_pos_y = -36
        self.barrier_speed = 0.2
        self.cant_create_barrier = False
        self.cant_create_barrier_tim = 10
        self.barrier_cct_countdown_speed = 0.01
        self.barrier_create_probability_drop_speed = 0.0001
        self.barrier_create_probability_floor = 0.9999
        self.barrier_create_probability_ceil = 1.999
        
        self.clouds_pos_y=(-75,-90,-105)
        self.cloud_scale = ((50,20),(37.5,15),(25,10))
        self.cant_create_clouds = False
        self.clouds_create_probability_floor = 0.999
        self.clouds_create_probability_ceil = 1.999
        self.cant_create_clouds_tim = 10
        self.clouds_cct_countdown_speed = 0.01
        self.cloud_speed = (0.16,0.13,0.1)
        
        self.pteros_pos_y=-55
        self.cant_create_ptero = False
        self.cant_create_ptero_tim = 60
        self.ptero_create_probability_floor = 0.999
        self.ptero_create_probability_ceil = 1.999
        self.ptero_cct_countdown_speed = 0.01
        self.ptero_speed = 0.3
        self.ptero_changing_speed = -0.005
        self.ptero_choose_origin = 1.99

        self.background_pos_y = -50
        self.background_speed = 0.2
        