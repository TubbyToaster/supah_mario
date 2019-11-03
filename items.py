import pygame
from pygame.sprite import Sprite
from timer import Timer


class Items(Sprite):
    def __init__(self, ai_settings, screen, g_blocks, bg_blocks, mario, type_, rcenter, bottom, center, mov_left,
                 mov_right):
        super(Items, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings
        self.type = type_
        self.load_images()
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.centerx = rcenter
        self.rect.bottom = bottom
        self.center = center
        self.mario = mario
        self.g_blocks = g_blocks
        self.bg_blocks = bg_blocks
        self.type = type_
        self.mov_right = mov_right
        self.mov_left = mov_left
        self.image_index = 1
        self.image_cap = 10
        self.spd = 5
        self.mario = mario
        self.vy = 0
        self.pos = 200
        self.jumping = False
        self.jumping_press = False
        self.change_x = 0
        self.change_y = 0
        self.g_blocks = g_blocks
        self.bg_blocks = bg_blocks
        self.cap = 8
        self.jump_scaler = 0
        self.land = True
        self.inair = False
        self.state = "idle"
        self.fric = 0
        self.falling = False
        self.landed = True
        if self.type == "fireball":
            self.landed = False
        self.timer = Timer(self.frames_, wait=150)
        self.image = pygame.image.load("assets/special/fire_1.bmp")
        self.frames_ = None

    def load_images(self):
        if self.type == "mushroom":
            self.image = pygame.image.load('assets/interactible/Rshroom.bmp')
            self.frames_ = ['assets/interactible/Rshroom.bmp']
        elif self.type == "star":
            self.image = pygame.image.load('assets/interactible/star_1.bmp')
            self.frames_ = ['assets/interactible/star_1.bmp', 'assets/interactible/star_2.bmp',
                            'assets/interactible/star_3.bmp', 'assets/interactible/star_4.bmp']
        elif self.type == "coin":
            self.image = pygame.image.load('assets/special/coin_1.bmp')
            self.frames_ = ['assets/special/coin_1.bmp', 'assets/special/coin_2.bmp',
                            'assets/special/coin_3.bmp', 'assets/special/coin_4.bmp']
        elif self.type == "fireflower":
            self.image = pygame.image.load('assets/interactible/ff_1_1.bmp')
            self.frames_ = ['assets/interactible/ff_1_2.bmp', 'assets/interactible/ff_1_2.bmp',
                            'assets/interactible/ff_1_3.bmp', 'assets/interactible/ff_1_4.bmp']
        elif self.type == "1upshroom":
            self.image = pygame.image.load('assets/interactible/L1up.bmp')
            self.frames_ = ['assets/interactible/L1up.bmp']
        elif self.type == "shell_mov":
            self.image = pygame.image.load('assets/enemies/shell_1.bmp')
            self.frames_ = ['assets/enemies/shell_1.bmp', 'assets/enemies/shell_1.bmp']
        elif self.type == "bshell_mov":
            self.image = pygame.image.load('assets/enemies/bshell.bmp')
            self.frames_ = ['assets/enemies/bshell.bmp', 'assets/enemies/bshell.bmp']
        elif self.type == "fireball":
            self.image = pygame.image.load('assets/special/fire_1.bmp')
            self.frames_ = ['assets/special/fire_1.bmp', 'assets/special/fire_2.bmp',
                            'assets/special/fire_3.bmp', 'assets/special/fire_4.bmp']

        self.timer = Timer(self.frames_, wait=150)

    def go_left(self):
        self.change_x -= self.fric

    def go_right(self):
        self.change_x += self.fric

    def check_screen(self):
        if self.mov_right is True:
            self.go_right()
        elif self.mov_left is True:
            self.go_left()

    def update(self):
        self.check_screen()
        self.image = pygame.image.load(self.timer.imagerect())

        if self.type == "fireball" and (self.rect.left < 0 or self.rect.right > self.screen_rect.right):
            self.mario.fireball_count -= 1
            self.kill()

        if (self.type == "star" or self.type == "fireball") and self.landed:
            if self.change_y == 0 and self.falling is False:
                if self.type == "star":
                    self.change_y = -12
                if self.type == "fireball":
                    self.change_y = -12
                self.falling = True
                self.landed = False
            if self.jump_scaler == 0:
                if self.jump_scaler < 12 and self.falling is False:
                    self.jump_scaler += 1
                else:
                    self.falling = False
                self.change_y -= self.jump_scaler
            else:
                self.jump_scaler = 0

        if self.type == "1upshroom" or self.type == "mushroom" or self.type == "star" \
                or self.type == "fireball" or self.type == "shell_mov" or self.type == "bshell_mov":
            ff = 1
            max_ = 3
            if self.type == "fireball" or self.type == "shell_mov" or self.type == "bshell_mov":
                max_ = 20
                ff = 10
            if self.mov_right and self.fric < max_:
                self.fric += ff
            elif self.fric > 0:
                self.fric -= ff
            if self.mov_left and self.fric > -max_:
                self.fric -= ff
            elif self.fric < 0:
                self.fric += ff

        self.change_x = self.fric
        self.calc_grav()
        self.rect.x += self.change_x

        for block in self.g_blocks:
            if self.rect.colliderect(block.rect):
                if self.change_x > 0 and self.rect.bottom != block.rect.top:  # right
                    self.rect.right = block.rect.left
                    self.mov_left = True
                    self.mov_right = False
                    if self.type == "fireball":
                        self.mario.fireball_count -= 1
                        self.kill()
                elif self.change_x < 0 and self.rect.bottom != block.rect.top:  # left
                    self.rect.left = block.rect.right
                    self.mov_right = True
                    self.mov_left = False
                    if self.type == "fireball":
                        self.mario.fireball_count -= 1
                        self.kill()
        self.rect.y += self.change_y
        for block in self.g_blocks:
            if self.rect.colliderect(block.rect):
                if self.change_y > 0:
                    self.rect.bottom = block.rect.top
                    self.landed = True
                elif self.change_y < 0:
                    self.rect.top = block.rect.bottom
                    self.landed = True
                self.change_y = 0

    def calc_grav(self):
        if self.change_y == 0:
            self.change_y = 1
            if self.type == "fireball":
                self.change_y = 2
        else:
            self.change_y += 1
            if self.type == "fireball":
                self.change_y += 1
        if self.rect.y >= 800 - self.rect.height and self.change_y >= 0:
            self.change_y = 0
            self.rect.y = 800 - self.rect.height

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
            self.image_index = self.image
