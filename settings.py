import random


class Settings:
    def __init__(self):
        self.screen_width = 1440
        self.screen_height = 720
        self.bg_color = (1, 0, 0)
        self.mario_lives = 3
        self.speedup_scale = 1.5
        self.score_scale = 1.5
        self.high_score = 0
        self.frame = 0
        self.frame_end = 20
        self.level = 1

    def get_frame(self):
        return self.frame
