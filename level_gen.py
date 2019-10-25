import pygame
from pygame.sprite import Sprite
from blocks import Blocks
from functions import create_g_blocks
from functions import create_bg_blocks


class Chunk():
    def __init__(self, ai_settings, screen, g_blocks, bg_blocks, map):
        super(Chunk, self).__init__()
        self.screen = screen
        self.g_blocks = g_blocks
        self.bg_blocks = bg_blocks
        self.ai_settings = ai_settings
        # self.rect =
        # self.rect.y = self.rect.height
        # self.x = float(self.rect.x)
        self.image_index = 1
        self.map = map
        '''self.map = [
            "-------------------------",
            "                        -",
            "-                       -",
            "-                       -",
            "-                       -",
            "-                       -",
            "-                       -",
            "-                       -",
            "-                       -",
            "-                       -",
            "-                       -",
            "-                       -",
            "-                       -",
            "-                       -",
            "-                       -",
            "-                       -",
            "-                       -",
            "-                       -",
            "-                       -",
            "-------------------------"]'''

    def gen(self, left, chunk_type):
        x = left
        y = 0
        if chunk_type == "g":
            for row in self.map:
                for col in row:
                    if col == "1":
                        create_g_blocks(self.ai_settings, self.screen,
                                        "assets/ground_tiles/brick_1.bmp",
                                        self.g_blocks, x, y, 400)
                    x += 48
                y += 48
                x = left
        elif chunk_type == "bg":
            for row in self.map:
                for col in row:
                    if col == "b":
                        create_bg_blocks(self.ai_settings, self.screen,
                                         "assets/bg_tiles/sky.bmp",
                                         self.bg_blocks, x, y, 400)
                    elif col == "c":
                        create_bg_blocks(self.ai_settings, self.screen,
                                         "assets/bg_tiles/cloud_1_1.bmp",
                                         self.bg_blocks, x, y, 400)
                    elif col == "d":
                        create_bg_blocks(self.ai_settings, self.screen,
                                         "assets/bg_tiles/cloud_1_2.bmp",
                                         self.bg_blocks, x, y, 400)
                    elif col == "e":
                        create_bg_blocks(self.ai_settings, self.screen,
                                         "assets/bg_tiles/cloud_1_3.bmp",
                                         self.bg_blocks, x, y, 400)
                    elif col == "f":
                        create_bg_blocks(self.ai_settings, self.screen,
                                         "assets/bg_tiles/cloud_1_4.bmp",
                                         self.bg_blocks, x, y, 400)
                    elif col == "g":
                        create_bg_blocks(self.ai_settings, self.screen,
                                         "assets/bg_tiles/hill_slope_left.bmp",
                                         self.bg_blocks, x, y, 400)
                    elif col == "h":
                        create_bg_blocks(self.ai_settings, self.screen,
                                         "assets/bg_tiles/hill_top.bmp",
                                         self.bg_blocks, x, y, 400)
                    elif col == "i":
                        create_bg_blocks(self.ai_settings, self.screen,
                                         "assets/bg_tiles/hill_slope_right.bmp",
                                         self.bg_blocks, x, y, 400)
                    elif col == "j":
                        create_bg_blocks(self.ai_settings, self.screen,
                                         "assets/bg_tiles/hill.bmp",
                                         self.bg_blocks, x, y, 400)
                    elif col == "k":
                        create_bg_blocks(self.ai_settings, self.screen,
                                         "assets/bg_tiles/hill_spot_right.bmp",
                                         self.bg_blocks, x, y, 400)
                    elif col == "l":
                        create_bg_blocks(self.ai_settings, self.screen,
                                         "assets/bg_tiles/hill_spot_left.bmp",
                                         self.bg_blocks, x, y, 400)
                    elif col == "m":
                        create_bg_blocks(self.ai_settings, self.screen,
                                         "assets/bg_tiles/Lbush.bmp",
                                         self.bg_blocks, x, y, 400)
                    elif col == "n":
                        create_bg_blocks(self.ai_settings, self.screen,
                                         "assets/bg_tiles/Mbush.bmp",
                                         self.bg_blocks, x, y, 400)
                    x += 48
                y += 48
                x = left


#ground 1-1
"""0 = none
1 = brick_1



#bg 1-1
a = black
b = sky
c = cloud_1_1
d = cloud_1_2
e = cloud_1_3
f = cloud_1_4
g = hill_slope_left
h = hill_top
i = hill_slope_right
j = hill
k = hill_spot_right
l = hill_spot_left
m = Lbush
n = Mbush
o = Rbush

[ 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 ,
  1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 ,
  1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 ,
  1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 3 , 1 , 1 , 1 , 1 , 1 ,
  1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 2 , 4 , 5 , 1 , 1 , 1 , 1 ,
  1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 ,
  1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 ,
  1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 ,
  1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 ,
  1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 ,
  1 , 1 , 7 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 ,
  1 , 6 , 10, 8 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 ,
  6 , 10, 9 , 11, 8 , 1 , 1 , 1 , 1 , 1 , 1 , 12, 13, 13, 13,
  0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 ,
  0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 ] """
