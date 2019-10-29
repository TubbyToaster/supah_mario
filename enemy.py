import pygame
from pygame.sprite import Sprite
from timer import Timer


class Enemy(Sprite):
    def __init__(self, ai_settings, screen, g_blocks, bg_blocks, enemies, type_, rcenter, bottom, center, items):
        super(Enemy, self).__init__()
        self.screen = screen
        self.items = items
        self.ai_settings = ai_settings
        self.image = pygame.image.load('assets/enemies/goomba_1.bmp')
        self.frames_ = ['assets/enemies/goomba_1.bmp', 'assets/enemies/goomba_2.bmp']
        self.timer = Timer(self.frames_, wait=150)
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.centerx = rcenter
        self.enemies = enemies
        self.rect.bottom = bottom  # self.screen_rect.bottom
        self.center = center  # float(self.rect.centerx)
        self.mov_right = False
        self.mov_left = True
        self.image_index = 1
        self.image_cap = 10
        self.spd = 5
        self.type = type_
        # self.mario = mario
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
        self.landed = True
        self.death = False
        self.died = False
        self.size = 0
        self.death_blow = False
        self.dir_face = "left"
        self.deathTime = -1

    def go_left(self):
        self.change_x -= self.fric
        self.timer.reset()

    def go_right(self):
        self.change_x += self.fric
        self.timer.reset()

    def check_screen(self):
        if self.mov_right is True:
            self.go_right()
        elif self.mov_left is True:
            self.go_left()

    def update(self):
        if self.deathTime > 0:
            self.deathTime -= 1
        if self.deathTime == 0:
            self.kill()
            print("death time zero")

        # if self.rect.left -1000 < self.mario.rect.right:
        # self.state = "active"

        if self.jumping and self.change_y == 0:
            self.change_y = -12
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
        if self.state == "active" and self.state != "dead":
            if self.mov_right and self.fric < 3:
                self.fric += ff
            elif self.fric > 0:
                self.fric -= ff
            if self.mov_left and self.fric > -3:
                self.fric -= ff
            elif self.fric < 0:
                self.fric += ff

        if self.mov_left and not self.mov_right and self.state != "dead":
            self.rect.x += self.change_x
            self.dir_face = "left"
            if self.type == "goomba":
                self.frames_ = ['assets/enemies/goomba_1.bmp', 'assets/enemies/goomba_2.bmp']
            if self.type == "koopa":
                self.frames_ = ['assets/enemies/koopa_1.bmp', 'assets/enemies/koopa_2.bmp']
            if self.type == "shell":
                self.frames_ = ['assets/enemies/shell_1.bmp', 'assets/enemies/shell_1.bmp']
            if self.type == "shell_mov":
                self.frames_ = ['assets/enemies/shell_1.bmp', 'assets/enemies/shell_1.bmp']
            if self.type == "dead":
                self.frames_ = ['assets/enemies/goomba_stomp.bmp', 'assets/enemies/goomba_stomp.bmp']
            self.timer.frames = self.frames_

        if self.mov_right and not self.mov_left and self.state != "dead":
            self.rect.x += self.change_x
            self.dir_face = "right"
            if self.type == "goomba":
                self.frames_ = ['assets/enemies/goomba_1.bmp', 'assets/enemies/goomba_2.bmp']
            if self.type == "koopa":
                self.frames_ = ['assets/enemies/koopa_3.bmp', 'assets/enemies/koopa_4.bmp']
            if self.type == "shell":
                self.frames_ = ['assets/enemies/shell_1.bmp', 'assets/enemies/shell_1.bmp']
            if self.type == "shell_mov":
                self.frames_ = ['assets/enemies/shell_1.bmp', 'assets/enemies/shell_1.bmp']
            if self.type == "dead":
                self.frames_ = ['assets/enemies/goomba_stomp.bmp', 'assets/enemies/goomba_stomp.bmp']

            self.timer.frames = self.frames_

        self.change_x = self.fric
        self.calc_grav()
        self.rect.x += self.change_x

        self.image = pygame.image.load(self.timer.imagerect())

        for block in self.g_blocks:
            if self.rect.colliderect(block.rect) and self.state != "dead":
                if self.change_x > 0 and self.rect.bottom != block.rect.top:  # right
                    self.rect.right = block.rect.left
                    self.mov_left = True
                    self.mov_right = False
                elif self.change_x < 0 and self.rect.bottom != block.rect.top:  # left
                    self.rect.left = block.rect.right
                    self.mov_right = True
                    self.mov_left = False
        self.rect.y += self.change_y
        for block in self.g_blocks:
            if self.rect.colliderect(block.rect) and self.state != "dead":
                if self.change_y > 0:
                    self.rect.bottom = block.rect.top
                elif self.change_y < 0:
                    self.rect.top = block.rect.bottom
                self.change_y = 0

        for item in self.items:
            if self.rect.colliderect(item.rect) and self.state != "dead" and item.type == "fireball":
                self.kill()
                item.kill()

    def calc_grav(self):
        if self.change_y == 0:
            self.change_y = 1
        else:
            self.change_y += 1
        if self.type == "koopa":
            if self.rect.y >= 600 - self.rect.height and self.change_y >= 0:
                self.change_y = 0
                self.rect.y = 600 - self.rect.height
        if self.type == "goomba":
            if self.rect.y >= 800 - self.rect.height and self.change_y >= 0:
                self.change_y = 0
                self.rect.y = 800 - self.rect.height
        if self.type == "shell":
            if self.rect.y >= 800 - self.rect.height and self.change_y >= 0:
                self.change_y = 0
                self.rect.y = 800 - self.rect.height

    def dead_enemy(self):
        self.image = pygame.image.load('assets/enemies/goomba_stomp.bmp')
        self.state = "dead"
        self.mov_left = False
        self.mov_right = False
        self.rect.y += 20
        self.frames_ = ['assets/enemies/goomba_stomp.bmp']
        if self.type == "goomba":
            self.frames_ = ['assets/enemies/goomba_stomp.bmp']
            self.timer.reset()
            self.deathTime = 10
        if self.type == "koopa":
            self.type = "shell"
            self.frames_ = ['assets/enemies/shell_1.bmp', 'assets/enemies/shell_1.bmp']
            self.timer.reset()
        self.timer.frames = self.frames_
        self.timer.looponce = True
        self.timer.reset()

    def blitme(self):
        self.screen.blit(self.image, self.rect)

    def center_enemy(self):
        self.center = self.screen_rect.centerx

    def image_up(self):
        self.image_index += .5
        if self.image_index > self.image_cap:
            self.image_index = 1

    def update_frame(self):
        if self.image_index == 0:
            self.image_index = self.image
