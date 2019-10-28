import pygame
from pygame.sprite import Sprite
from timer import Timer


class Mario(Sprite):
    def __init__(self, ai_settings, screen, g_blocks, bg_blocks, enemies, monitor, chunks):
        super(Mario, self).__init__()
        self.screen = screen
        self.monitor = monitor
        self.ai_settings = ai_settings
        self.chunks = chunks
        self.image = pygame.image.load('assets/mario/Rmario_stand.bmp')
        self.frames_ = ['assets/mario/fmario_turn2L.bmp', 'assets/mario/fmario_turn2R.bmp']
        self.timer = Timer(self.frames_, wait=150)
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
        self.death = False
        self.died = False
        self.size = 0
        self.death_blow = False
        self.dir_face = "right"

    def go_left(self):
        self.change_x -= self.fric
        self.timer.reset()


    def go_right(self):
        self.change_x += self.fric
        self.timer.reset()


    def update(self):

        self.image = pygame.image.load(self.timer.imagerect())

        if self.rect.y >= 720 - self.rect.height and self.change_y >= 0 and not self.died or self.death_blow:
            self.change_y = -26
            self.jumping = False
            self.death = True
            self.died = True
            self.death_blow = False
            self.frames_ = ['assets/mario/mario_dead.bmp']
            self.timer.frames = self.frames_
            self.timer.reset()

        if self.jumping and self.change_y == 0:
            self.change_y = -26
            self.jumping = False
        if self.jumping_press and self.jump_scaler == 0:
            if self.jump_scaler < 20:
                self.jump_scaler += 1
            else:
                self.jumping_press = False
            self.change_y -= self.jump_scaler
        else:
            self.jump_scaler = 0

        ff = 2
        if self.mov_right and self.fric < 12:
            self.fric += ff
        elif self.fric > 0:
            self.fric -= ff
        if self.mov_left and self.fric > -12:
            self.fric -= ff
        elif self.fric < 0:
            self.fric += ff

        if self.change_x == 0 and self.change_y == 0 and not self.died:
            if self.dir_face == "right":
                self.frames_ = ['assets/mario/Rmario_stand.bmp']
            if self.dir_face == "left":
                self.frames_ = ['assets/mario/Lmario_stand.bmp']
            self.timer.frames = self.frames_
            self.timer.reset()



        if self.mov_left and not self.mov_right:
            self.rect.x += self.change_x
            self.dir_face = "left"
            self.frames_ = ['assets/mario/Lmario_walk_1.bmp', 'assets/mario/Lmario_walk_2.bmp',
                            'assets/mario/Lmario_walk_3.bmp']
            self.timer.frames = self.frames_
            #self.timer.reset()


        if self.mov_right and not self.mov_left:
            self.rect.x += self.change_x
            self.dir_face = "right"
            self.frames_ = ['assets/mario/Rmario_walk_1.bmp', 'assets/mario/Rmario_walk_2.bmp',
                            'assets/mario/Rmario_walk_3.bmp']
            self.timer.frames = self.frames_
            #self.timer.reset()

        if self.inair:
            if not self.landed and self.dir_face == "right":
                self.frames_ = ['assets/mario/Rmario_jump.bmp']
                self.timer.frames = self.frames_
                self.timer.reset()
            if not self.landed and self.dir_face == "left":
                self.frames_ = ['assets/mario/Lmario_jump.bmp']
                self.timer.frames = self.frames_
                self.timer.reset()

        # self.change_x = self.fric
        if self.rect.centerx < round(self.ai_settings.screen_width / 2) and self.mov_right and not self.mov_left:
            self.go_right()
        elif self.rect.centerx > round(self.ai_settings.screen_width / 2) and self.mov_right and not self.mov_left:
            for blocks in self.g_blocks:
                # blocks.x -= self.change_x
                blocks.rect.x -= self.change_x
            for blocks in self.bg_blocks:
                # blocks.x -= self.change_x
                blocks.rect.x -= self.change_x
            for enemy in self.enemies:
                enemy.rect.x -= self.change_x
            for chunk in self.chunks:
                chunk.check_edge -= self.change_x
            self.rect.x -= self.change_x

        for block in self.g_blocks:
            if self.rect.colliderect(block.rect) and self.death == False:
                if self.change_x > 0: # and self.rect.bottom != block.rect.top:
                    self.rect.right = block.rect.left
                elif self.change_x < 0: # and self.rect.bottom != block.rect.top:
                    self.rect.left = block.rect.right

        self.change_x = self.fric
        self.calc_grav()


        self.rect.y += self.change_y
        for block in self.g_blocks:
            if self.rect.colliderect(block.rect) and self.death == False:
                if self.change_y > 0:
                    self.rect.bottom = block.rect.top
                    self.landed = True
                elif self.change_y < 0:
                    self.rect.top = block.rect.bottom
                    self.jumping_press = False
                    block.blipup()
                self.change_y = 0
        for enemy in self.enemies:
            if self.rect.colliderect(enemy.rect) and self.death == False:
                if self.change_y > 0:
                    self.rect.bottom = enemy.rect.top
                    self.change_y = -5
                    self.jumping = True
                    self.change_y = 0
                    self.enemies.remove(enemy)
                elif self.change_y < 0:
                    self.rect.top = enemy.rect.bottom
                else:
                    self.death_blow = True
                self.change_y = 0

    def calc_grav(self):
        if self.change_y == 0:
            self.change_y = 2
        else:
            self.change_y += 2
        if self.rect.y >= 720 - self.rect.height and self.change_y >= 0 and not self.died:
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

