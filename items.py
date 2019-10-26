import pygame
from pygame.sprite import Sprite


class Items(Sprite):
    def __init__(self, ai_settings, screen, blocks, mario, type_, rcenter, bottom, center):
        super(Items, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings
        self.image_ = pygame.image.load('assets/ship.bmp')
        self.rect = self.image_.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.centerx = rcenter
        self.rect.bottom = bottom
        self.center = center
        self.mario = mario
        self.blocks = blocks
        self.type = type_
        self.mov_right = False
        self.mov_left = True
        self.image_index = 1
        self.image_cap = 10
        self.spd = 5
        self.type = type_
        self.mario = mario
        self.vy = 0
        self.pos = 200
        self.jumping = False
        self.jumping_press = False
        self.change_x = 0
        self.change_y = 0
        self.blocks = blocks
        self.cap = 8
        self.jump_scaler = 0
        self.land = True
        self.inair = False
        self.state = "idle"
        self.fric = 0
        self.falling = False

    def go_left(self):
        self.change_x -= self.fric

    def go_right(self):
        self.change_x += self.fric

    def check_screen(self):
        if self.mov_right == True:
            self.go_right()
        elif self.mov_left == True:
            self.go_left()

    def update(self):
        self.check_screen()
        if self.type == "star":
            if self.change_y == 0 and self.falling == False:
                self.change_y = -12
                self.falling = True
            if self.jump_scaler == 0:
                if self.jump_scaler < 12 and self.falling == False:
                    self.jump_scaler += 1
                else:
                    self.falling = False
                self.change_y -= self.jump_scaler
            else:
                self.jump_scaler = 0

        if self.type == "mushroom" and self.type == "star":
            ff = 1
            if self.mov_right and self.fric < 3:
                self.fric += ff
            elif self.fric > 0:
                self.fric -= ff
            if self.mov_left and self.fric > -3:
                self.fric -= ff
            elif self.fric < 0:
                self.fric += ff

        self.change_x = self.fric
        self.calc_grav()
        self.rect.x += self.change_x

        for block in self.blocks:
            if self.rect.colliderect(block.rect):
                if self.change_x > 0 and self.rect.bottom != block.rect.top:  # right
                    self.rect.right = block.rect.left
                    self.mov_left = True
                    self.mov_right = False
                    if self.type == "mushroom":
                        self.image_ == pygame.image.load('assets/assets/interactible/Rshroom.bmp')


                elif self.change_x < 0 and self.rect.bottom != block.rect.top:  # left
                    self.rect.left = block.rect.right
                    self.mov_right = True
                    self.mov_left = False
        self.rect.y += self.change_y
        for block in self.blocks:
            if self.rect.colliderect(block.rect):
                if self.change_y > 0:
                    self.rect.bottom = block.rect.top
                elif self.change_y < 0:
                    self.rect.top = block.rect.bottom
                self.change_y = 0

    def calc_grav(self):
        if self.change_y == 0:
            self.change_y = 1
        else:
            self.change_y += 1
        if self.rect.y >= 600 - self.rect.height and self.change_y >= 0:
            self.change_y = 0
            self.rect.y = 600 - self.rect.height

    def blitme(self):
        if self.type == "star":
            self.image_ = pygame.image.load('assets/assets/interactible/star_1.bmp')
        elif self.type == "coin":
            self.image_ = pygame.image.load('assets/assets/interactible/coin_1_1.bmp')
        elif self.type == "mushroom":
            self.image_ = pygame.image.load('assets/assets/interactible/Lshroom.bmp')
        elif self.type == "fireflower":
            self.image_ = pygame.image.load('assets/assets/interactible/ff_1_1.bmp')
        elif self.type == "1upshroom":
            self.image_ = pygame.image.load('assets/assets/interactible/L1up.bmp')
        self.screen.blit(self.image_, self.rect)

    def center_mario(self):
        self.center = self.screen_rect.centerx

    def image_up(self):
        self.image_index += .5
        if self.image_index > self.image_cap:
            self.image_index = 1

    def update_frame(self):
        if self.image_index == 0:
            self.image_index = self.image_
