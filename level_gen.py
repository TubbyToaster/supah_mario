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
                    if col == "2":
                        create_g_blocks(self.ai_settings, self.screen,
                                        "assets/ground_tiles/pipe_1.bmp",
                                        self.g_blocks, x, y, 400)
                    if col == "3":
                        create_g_blocks(self.ai_settings, self.screen,
                                        "assets/ground_tiles/pipe_2.bmp",
                                        self.g_blocks, x, y, 400)
                    if col == "4":
                        create_g_blocks(self.ai_settings, self.screen,
                                        "assets/ground_tiles/pipe_3.bmp",
                                        self.g_blocks, x, y, 400)
                    if col == "5":
                        create_g_blocks(self.ai_settings, self.screen,
                                        "assets/ground_tiles/pipe_4.bmp",
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
                    elif col == "o":
                        create_bg_blocks(self.ai_settings, self.screen,
                                         "assets/bg_tiles/Rbush.bmp",
                                         self.bg_blocks, x, y, 400)
                    elif col == "p":
                        create_bg_blocks(self.ai_settings, self.screen,
                                         "assets/bg_tiles/cloud_2_1.bmp",
                                         self.bg_blocks, x, y, 400)
                    elif col == "q":
                        create_bg_blocks(self.ai_settings, self.screen,
                                         "assets/bg_tiles/cloud_2_2.bmp",
                                         self.bg_blocks, x, y, 400)
                    elif col == "r":
                        create_bg_blocks(self.ai_settings, self.screen,
                                         "assets/bg_tiles/cloud_2_3.bmp",
                                         self.bg_blocks, x, y, 400)
                    elif col == "s":
                        create_bg_blocks(self.ai_settings, self.screen,
                                         "assets/bg_tiles/cloud_2_4.bmp",
                                         self.bg_blocks, x, y, 400)
                    elif col == "t":
                        create_bg_blocks(self.ai_settings, self.screen,
                                         "assets/bg_tiles/cloud_2_5.bmp",
                                         self.bg_blocks, x, y, 400)
                    elif col == "u":
                        create_bg_blocks(self.ai_settings, self.screen,
                                         "assets/bg_tiles/cloud_2_6.bmp",
                                         self.bg_blocks, x, y, 400)
                    x += 48
                y += 48
                x = left


#ground 1-1
"""0 = none
1 = brick_1
2 = pipe_1
3 = pipe_2
4 = pipe_3
5 = pipe_4

g1_1_1
"000000000000000",
"000000000000000",
"000000000000000",
"000000000000000",
"000000000000000",
"000000000000000",
"000000000000000",
"000000000000000",
"000000000000000",
"000000000000000",
"000000000000000",
"000000000000000",
"000000000000000",
"111111111111111",
"111111111111111" 

g1_1_2
"000000000000000",
"000000000000000",
"000000000000000",
"000000000000000",
"000000000000000",
"000000000000000",
"000000000000000",
"000000000000000",
"000000000000000",
"000000000000000",
"000000000000000",
"000000000000023",
"000000000000054",
"111111111111111",
"111111111111111"

g1_1_3
"000000000000000",
"000000000000000",
"000000000000000",
"000000000000000",
"000000000000000",
"000000000000000",
"000000000000000",
"000000000000000",
"000000000000000",
"000000000000000",
"000000002300000",
"000000005400000",
"000000005400000",
"111111111111111",
"111111111111111"

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
p = cloud_2_1
q = cloud_2_2
r = cloud_2_3
s = cloud_2_4
t = cloud_2_5
u = cloud_2_6"""

1_1_1
"bbbbbbbbbbbbbbb",
"bbbbbbbbbbbbbbb",
"bbbbbbbbbdbbbbb",
"bbbbbbbbcefbbbb",
"bbbbbbbbbbbbbbb",
"bbbbbbbbbbbbbbb",
"bbbbbbbbbbbbbbb",
"bbbbbbbbbbbbbbb",
"bbbbbbbbbbbbbbb",
"bbbbbbbbbbbbbbb",
"bbhbbbbbbbbbbbb",
"bgkibbbbbbbbbbb",
"gkjlibbbbbbmnnn",
"aaaaaaaaaaaaaaa",
"aaaaaaaaaaaaaaa"

1_1_2
"bbbbbbbbbbbbbbb",
"bbbbbbbbbbbbbbb",
"bbbbpqrbbbbbbbb",
"bbbbstubbbbbpqq",
"bbbbbbbbbbbbstt",
"bbbbbbbbbbbbbbb",
"bbbbbbbbbbbbbbb",
"bbbbbbbbbbbbbbb",
"bbbbbbbbbbbbbbb",
"bbbbbbbbbbbbbbb",
"bbbbbbbbbbbbbbb",
"bbhbbbbbbbbbbbb",
"bbbbbbbbbbbmnno",
"aaaaaaaaaaaaaaa",
"aaaaaaaaaaaaaaa"

1_1_3
"bbbbbbbbbbbbbbb",
"bbbbbbbbbbbbbbb",
"bbbbbbpqqrbbbbb",
"qrbbbbsttubbbbb",
"tubbbbbbbbbbbbb",
"bbbbbbbbbbbbbbb",
"bbbbbbbbbbbbbbb",
"bbbbbbbbbbbbbbb",
"bbbbbbbbbbbbbbb",
"bbbbbbbbbbbbbbb",
"bbbbbbbbbbbbbbb",
"bbbbbbbbbbbbbbb",
"bbbbbbbbmnobbbb",
"aaaaaaaaaaaaaaa",
"aaaaaaaaaaaaaaa"
