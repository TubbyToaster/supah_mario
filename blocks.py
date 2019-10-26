import pygame
from pygame.sprite import Sprite


class Blocks(Sprite):
    def __init__(self, ai_settings, screen, image, x, y, num, type_):
        super(Blocks, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings
        self.image_ = 'assets/block.bmp'
        self.image = pygame.image.load(image)
        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x
        self.x = float(x)
        self.image_index = 1
        self.type_ = type_
        self.up = False
        self.down = False
        self.ypos = y
        self.up_g = 0
        self.down_g = 0

    def image_up(self):
        self.image_index += 1

    def blitme(self):
        if self.up_g > 0:
            self.rect.y -= 2
            self.up_g -= 1
        if self.down_g > 0:
            self.rect.y += 2
            self.down_g -= 1
        if self.up_g == 0 and self.up == True:
            self.up = False
            self.down_g = 5

        self.screen.blit(self.image, self.rect)

    def update_frame(self):
        if self.image_index == 1:
            self.image = self.image

    def blipup(self):
        if self.up_g == 0 and self.down_g == 0:
            self.up_g = 5
            self.up = True
