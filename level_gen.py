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
                    if col == "6":
                        create_g_blocks(self.ai_settings, self.screen,
                                        "assets/ground_tiles/stair_1.bmp",
                                        self.g_blocks, x, y, 400)
                    if col == "7":
                        create_g_blocks(self.ai_settings, self.screen,
                                        "assets/ground_tiles/brick_3.bmp",
                                        self.g_blocks, x, y, 400)
                    if col == "8":
                        create_g_blocks(self.ai_settings, self.screen,
                                        "assets/ground_tiles/brick_4.bmp",
                                        self.g_blocks, x, y, 400)
                    if col == "9":
                        create_g_blocks(self.ai_settings, self.screen,
                                        "assets/ground_tiles/pipe_15.bmp",
                                        self.g_blocks, x, y, 400)
                    if col == "a":
                        create_g_blocks(self.ai_settings, self.screen,
                                        "assets/ground_tiles/pipe_16.bmp",
                                        self.g_blocks, x, y, 400)
                    if col == "b":
                        create_g_blocks(self.ai_settings, self.screen,
                                        "assets/ground_tiles/pipe_17.bmp",
                                        self.g_blocks, x, y, 400)
                    if col == "c":
                        create_g_blocks(self.ai_settings, self.screen,
                                        "assets/ground_tiles/pipe_18.bmp",
                                        self.g_blocks, x, y, 400)
                    if col == "d":
                        create_g_blocks(self.ai_settings, self.screen,
                                        "assets/ground_tiles/pipe_19.bmp",
                                        self.g_blocks, x, y, 400)
                    if col == "e":
                        create_g_blocks(self.ai_settings, self.screen,
                                        "assets/ground_tiles/pipe_20.bmp",
                                        self.g_blocks, x, y, 400)
                    if col == "f":
                        create_g_blocks(self.ai_settings, self.screen,
                                        "assets/ground_tiles/pipe_13.bmp",
                                        self.g_blocks, x, y, 400)
                    if col == "g":
                        create_g_blocks(self.ai_settings, self.screen,
                                        "assets/ground_tiles/pipe_14.bmp",
                                        self.g_blocks, x, y, 400)
                    if col == "h":
                        create_g_blocks(self.ai_settings, self.screen,
                                        "assets/ground_tiles/pipe_5.bmp",
                                        self.g_blocks, x, y, 400)
                    if col == "i":
                        create_g_blocks(self.ai_settings, self.screen,
                                        "assets/ground_tiles/pipe_6.bmp",
                                        self.g_blocks, x, y, 400)
                    if col == "j":
                        create_g_blocks(self.ai_settings, self.screen,
                                        "assets/ground_tiles/pipe_7.bmp",
                                        self.g_blocks, x, y, 400)
                    if col == "k":
                        create_g_blocks(self.ai_settings, self.screen,
                                        "assets/ground_tiles/pipe_8.bmp",
                                        self.g_blocks, x, y, 400)
                    if col == "l":
                        create_g_blocks(self.ai_settings, self.screen,
                                        "assets/ground_tiles/pipe_9.bmp",
                                        self.g_blocks, x, y, 400)
                    if col == "m":
                        create_g_blocks(self.ai_settings, self.screen,
                                        "assets/ground_tiles/pipe_10.bmp",
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
                    elif col == "v":
                        create_bg_blocks(self.ai_settings, self.screen,
                                         "assets/bg_tiles/castle_1.bmp",
                                         self.bg_blocks, x, y, 400)
                    elif col == "w":
                        create_bg_blocks(self.ai_settings, self.screen,
                                         "assets/bg_tiles/castle_2.bmp",
                                         self.bg_blocks, x, y, 400)
                    elif col == "x":
                        create_bg_blocks(self.ai_settings, self.screen,
                                         "assets/bg_tiles/castle_3.bmp",
                                         self.bg_blocks, x, y, 400)
                    elif col == "y":
                        create_bg_blocks(self.ai_settings, self.screen,
                                         "assets/bg_tiles/castle_4.bmp",
                                         self.bg_blocks, x, y, 400)
                    elif col == "z":
                        create_bg_blocks(self.ai_settings, self.screen,
                                         "assets/bg_tiles/castle_5.bmp",
                                         self.bg_blocks, x, y, 400)
                    elif col == "1":
                        create_bg_blocks(self.ai_settings, self.screen,
                                         "assets/bg_tiles/castle_6.bmp",
                                         self.bg_blocks, x, y, 400)
                    elif col == "2":
                        create_bg_blocks(self.ai_settings, self.screen,
                                         "assets/bg_tiles/pole.bmp",
                                         self.bg_blocks, x, y, 400)
                    elif col == "3":
                        create_bg_blocks(self.ai_settings, self.screen,
                                         "assets/bg_tiles/pole_top.bmp",
                                         self.bg_blocks, x, y, 400)
                    x += 48
                y += 48
                x = left


