import pygame
from pygame.sprite import Sprite


class Blocks(Sprite):
    def __init__(self, ai_settings, screen, image, x, y):
        super(Blocks, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings
        self.image = pygame.image.load(image)
        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x
        self.x = float(x)
        self.image_index = 1

    def image_up(self):
        self.image_index += 1

    def blitme(self):
        self.screen.blit(self.image, self.rect)

    def update_frame(self):
        if self.image_index == 1:
            self.image = self.image
