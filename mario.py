import pygame
from pygame.sprite import Sprite

from functions import create_item
from timer import Timer


class Mario(Sprite):
    def __init__(self, ai_settings, screen, g_blocks, bg_blocks, enemies, monitor, chunks, items):
        super(Mario, self).__init__()
        self.screen = screen
        self.monitor = monitor
        self.ai_settings = ai_settings
        self.chunks = chunks
        self.items = items
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
        self.state = "reg"
        self.fric = 0
        self.landed = True
        self.death = False
        self.died = False
        self.size = 0
        self.death_blow = False
        self.dir_face = "right"
        self.fireball_count = 0

    def go_left(self):
        self.change_x -= self.fric
        self.timer.reset()

    def go_right(self):
        self.change_x += self.fric
        self.timer.reset()

    def fireball(self):
        self.size = 0

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
            if self.state == "super":
                if self.dir_face == "right":
                    self.frames_ = ['assets/mario/Rsmario_stand.bmp']
                if self.dir_face == "left":
                    self.frames_ = ['assets/mario/Lsmario_stand.bmp']
            if self.state == "fire":
                if self.dir_face == "right":
                    self.frames_ = ['assets/mario/Rfmario_stand.bmp']
                if self.dir_face == "left":
                    self.frames_ = ['assets/mario/Lfmario_stand.bmp']
            self.timer.frames = self.frames_
            self.timer.reset()

        if self.mov_left and not self.mov_right:
            self.rect.x += self.change_x
            self.dir_face = "left"
            self.frames_ = ['assets/mario/Lmario_walk_1.bmp', 'assets/mario/Lmario_walk_2.bmp',
                            'assets/mario/Lmario_walk_3.bmp']
            if self.state == "super":
                self.frames_ = ['assets/mario/Lsmario_walk_1.bmp', 'assets/mario/Lsmario_walk_2.bmp',
                                'assets/mario/Lsmario_walk_3.bmp']
            if self.state == "fire":
                self.frames_ = ['assets/mario/Lfmario_walk_1.bmp', 'assets/mario/Lfmario_walk_2.bmp',
                                'assets/mario/Lfmario_walk_3.bmp']
            self.timer.frames = self.frames_
            # self.timer.reset()

        if self.mov_right and not self.mov_left:
            self.rect.x += self.change_x
            self.dir_face = "right"
            self.frames_ = ['assets/mario/Rmario_walk_1.bmp', 'assets/mario/Rmario_walk_2.bmp',
                            'assets/mario/Rmario_walk_3.bmp']
            if self.state == "super":
                self.frames_ = ['assets/mario/Rsmario_walk_1.bmp', 'assets/mario/Rsmario_walk_2.bmp',
                                'assets/mario/Rsmario_walk_3.bmp']
            if self.state == "fire":
                self.frames_ = ['assets/mario/Rfmario_walk_1.bmp', 'assets/mario/Rfmario_walk_2.bmp',
                                'assets/mario/Rfmario_walk_3.bmp']
            self.timer.frames = self.frames_
            # self.timer.reset()

        if self.mov_right and self.fric < 0:
            self.frames_ = ['assets/mario/mario_turn2R.bmp']
            if self.state == "super":
                self.frames_ = ['assets/mario/smario_turn2R.bmp']
            if self.state == "fire":
                self.frames_ = ['assets/mario/fmario_turn2R.bmp']
            self.timer.frames = self.frames_
            self.timer.reset()
        if self.mov_left and self.fric > 0:
            self.frames_ = [ 'assets/mario/mario_turn2L.bmp']
            if self.state == "super":
                self.frames_ = ['assets/mario/smario_turn2L.bmp']
            if self.state == "fire":
                self.frames_ = ['assets/mario/fmario_turn2L.bmp']
            self.timer.frames = self.frames_
            self.timer.reset()

        if self.inair and not self.died:
            if not self.landed and self.dir_face == "right":
                self.frames_ = ['assets/mario/Rmario_jump.bmp']
                if self.state == "super":
                    self.frames_ = ['assets/mario/Rsmario_jump.bmp']
                if self.state == "fire":
                    self.frames_ = ['assets/mario/Rfmario_jump.bmp']
                self.timer.frames = self.frames_
                self.timer.reset()
            if not self.landed and self.dir_face == "left":
                self.frames_ = ['assets/mario/Lmario_jump.bmp']
                if self.state == "super":
                    self.frames_ = ['assets/mario/Lsmario_jump.bmp']
                if self.state == "fire":
                    self.frames_ = ['assets/mario/Lfmario_jump.bmp']
                self.timer.frames = self.frames_
                self.timer.reset()

        # self.change_x = self.fric
        if self.rect.centerx < round(self.ai_settings.screen_width / 2) and self.mov_right and not self.mov_left:
            self.go_right()
        elif self.rect.centerx > round(self.ai_settings.screen_width / 2) and self.mov_right and not self.mov_left:
            for blocks in self.g_blocks:
                blocks.rect.x -= self.change_x
            for blocks in self.bg_blocks:
                blocks.rect.x -= self.change_x
            for item in self.items:
                item.rect.x -= self.change_x
            for enemy in self.enemies:
                enemy.rect.x -= self.change_x
            for chunk in self.chunks:
                chunk.check_edge -= self.change_x
            self.rect.x -= self.change_x

        for block in self.g_blocks:
            if self.rect.colliderect(block.rect) and not self.death and block.type_ != "hidden":
                if self.change_x > 0 and block.type_ != "hidden":  # and self.rect.bottom != block.rect.top:
                    self.rect.right = block.rect.left
                elif self.change_x < 0 and block.type_ != "hidden":  # and self.rect.bottom != block.rect.top:
                    self.rect.left = block.rect.right

        self.change_x = self.fric
        self.calc_grav()

        self.rect.y += self.change_y
        for block in self.g_blocks:
            if self.rect.colliderect(block.rect) and not self.death:
                if self.change_y > 0 and block.type_ != "hidden":
                    self.rect.bottom = block.rect.top
                    self.landed = True
                elif self.change_y < 0:
                    self.rect.top = block.rect.bottom
                    self.jumping_press = False
                    self.cur_item(block)
                    if block.type_ == "bricks" and (self.state == "super" or self.state == "fire"):
                        block.dead = 1
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
        for item in self.items:
            if self.rect.colliderect(item.rect) and self.death == False and item.type != "fireball":
                if item.type == "mushroom":
                    self.grow_up()
                    self.state = "super"
                if self.state == "super" and item.type == "fireflower":
                    self.state = "fire"
                if self.state != "super" and item.type == "fireflower":
                    self.grow_up()
                    self.state = "fire"

                self.items.remove(item)

    def grow_up(self):
        temp1 = self.screen_rect
        temp2 = self.rect.centerx
        temp3 = self.rect.bottom
        temp4 = self.center
        im = pygame.image.load('assets/mario/Rsmario_stand.bmp')
        self.rect = im.get_rect()
        self.screen_rect = temp1
        self.rect.centerx = temp2
        self.rect.bottom = temp3
        self.center = temp4


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
        return self.screen_rect.centerx

    def image_up(self):
        self.image_index += .5
        if self.image_index > self.image_cap:
            self.image_index = 1

    def update_frame(self):
        if self.image_index == 0:
            self.image_index = self.image_

    def cur_item(self, block):

        if block.type_ == "pup" and self.state == "reg":
            if self.dir_face == "right":
                l = False
                r = True
            if self.dir_face == "left":
                l = True
                r = False
            create_item(self.ai_settings, self.screen, self.g_blocks, self.bg_blocks, self, self.items,
                    "mushroom", float(block.rect.x)+25,
                        block.rect.bottom-60,
                        float(block.rect.x), l, r)
        if block.type_ == "pup" and (self.state == "super" or self.state == "fire"):
            create_item(self.ai_settings, self.screen, self.g_blocks, self.bg_blocks, self, self.items,
                    "fireflower", float(block.rect.x)+25,
                        block.rect.bottom-30,
                        float(block.rect.x), False, False)

        block.blipup()

