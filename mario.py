import pygame
import math
from pygame.sprite import Sprite
from pygame.math import Vector2


class Mario(Sprite):
    def __init__(self, ai_settings, screen,  g_blocks, bg_blocks, enemies, monitor, chunks):
        super(Mario, self).__init__()
        self.screen = screen
        self.monitor = monitor
        self.ai_settings = ai_settings
        self.chunks = chunks
        self.image = pygame.image.load('assets/mario/smario_turn2L.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.centerx = self.screen_rect.centerx - 200
        self.rect.bottom = self.screen_rect.bottom - 200
        self.center = float(self.rect.centerx)
        self.mov_right = False
        self.mov_left = False
        self.image_index = 1
        self.image_cap = 10
        self.image_ = pygame.image.load('assets/ship.bmp')
        self.spd = 5
        self.vy = 0
        self.pos = 200
        self.jumping = False
        self.jumping_press = False
        self.change_x = 0
        self.change_y = 0
        self.g_blocks = g_blocks
        self.bg_blocks = bg_blocks
        self.enemies = enemies
        self.cap = 8
        self.jump_scaler = 0
        self.land = True
        self.inair = False
        self.state = "idle"
        self.fric = 0
        self.landed = True

    def go_left(self):
        self.change_x -= self.fric

    def go_right(self):
        self.change_x += self.fric



    def update(self):
        if self.jumping and self.change_y == 0:
            self.change_y = -18
            self.jumping = False
        if self.jumping_press and self.jump_scaler == 0:
            if self.jump_scaler < 12:
                self.jump_scaler += 1
            else:
                self.jumping_press = False
            self.change_y -= self.jump_scaler
        else:
            self.jump_scaler = 0

        ff = 1
        if self.mov_right and self.fric < 8:
            self.fric += ff
        elif self.fric > 0:
            self.fric -= ff
        if self.mov_left and self.fric > -8:
            self.fric -= ff
        elif self.fric < 0:
            self.fric += ff

        self.rect.x += self.change_x
        # self.change_x = self.fric
        if self.rect.centerx > self.ai_settings.screen_width / 2 and self.mov_right:
            for blocks in self.g_blocks:
                blocks.x -= self.change_x
                blocks.rect.x -= self.change_x
            for blocks in self.bg_blocks:
                blocks.x -= self.change_x
                blocks.rect.x -= self.change_x
            for enemy in self.enemies:
                enemy.rect.x -= self.change_x
            for chunk in self.chunks:
                chunk.check_edge -= self.change_x
            self.rect.x -= self.change_x

        self.change_x = self.fric
        self.calc_grav()

        for block in self.g_blocks:
            if self.rect.colliderect(block.rect):
                if self.change_x > 0 and self.rect.bottom != block.rect.top:
                    self.rect.right = block.rect.left
                elif self.change_x < 0 and self.rect.bottom != block.rect.top:
                    self.rect.left = block.rect.right
        self.rect.y += self.change_y
        for block in self.g_blocks:
            if self.rect.colliderect(block.rect):
                if self.change_y > 0:
                    self.rect.bottom = block.rect.top
                    self.landed = True
                elif self.change_y < 0:
                    self.rect.top = block.rect.bottom
                    self.jumping_press = False
                    block.blipup()
                self.change_y = 0
        for enemy in self.enemies:
            if self.rect.colliderect(enemy.rect):
                if self.change_y > 0:
                    self.rect.bottom = enemy.rect.top
                    self.change_y = -5
                    self.jumping = True
                    self.change_y = 0
                elif self.change_y < 0:
                    self.rect.top = enemy.rect.bottom
                self.change_y = 0

    def calc_grav(self):
        if self.change_y == 0:
            self.change_y = 1
        else:
            self.change_y += 1
        if self.rect.y >= 720 - self.rect.height and self.change_y >= 0:
            self.change_y = 0
            self.rect.y = 720 - self.rect.height

    def blitme(self):
        self.screen.blit(self.image, self.rect)

    def center_mario(self):
        self.center = self.screen_rect.centerx

    def image_up(self):
        self.image_index += .5
        if self.image_index > self.image_cap:
            self.image_index = 1

    def update_frame(self):
        if self.image_index == 0:
            self.image_index = self.image_
