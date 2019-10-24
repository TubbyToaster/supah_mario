import pygame
from pygame.sprite import Sprite
from blocks import Blocks
from functions import create_blocks


class Chunk():
    def __init__(self, ai_settings, screen, blocks):
        super(Chunk, self).__init__()
        self.screen = screen
        self.blocks = blocks
        self.ai_settings = ai_settings
        self.rect = self.image.get_rect()
        self.rect.y = self.rect.height
        self.x = float(self.rect.x)
        self.image_index = 1
        self.map = [
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
            "-------------------------"]

    def gen(self):
        x = y = 0 
        for row in self.map: 
            for col in row:  
                if col == "-":
                    create_blocks(self.ai_settings, self.screen, self.blocks, x, y, 400)
                x += 32  
            y += 32  
            x = 0  
