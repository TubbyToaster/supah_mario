import pygame
from pygame.sprite import Sprite

from functions import create_item
from timer import Timer


class Mario(Sprite):
    def __init__(self, ai_settings, screen, g_blocks, bg_blocks, enemies, monitor, chunks, items, scores):
        super(Mario, self).__init__()
        self.screen = screen
        self.monitor = monitor
        self.ai_settings = ai_settings
        self.scores = scores
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
        self.image_ = pygame.image.load('assets/special/fire_1.bmp')
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
        self.crouch = False
        self.invinc = 0
        self.flag = False
        self.temp_go = 0
        self.walk_an = "r"
        self.star_power = False
        self.next_level = "reg"

    def go_left(self):
        self.change_x -= self.fric
        self.timer.reset()

    def go_right(self):
        self.change_x += self.fric
        self.timer.reset()

    def go_right_winner(self):
        self.fric = 3
        self.rect.x += 3

    def fireball(self):
        self.size = 0

    def update(self, music, mario):
        self.image = pygame.image.load(self.timer.imagerect())

        if self.state == "goright":
            self.go_right_winner()
            if self.temp_go == 0:
                self.temp_go = 1

        if self.temp_go == 1:
            if self.walk_an == "r":
                self.grow_up('assets/mario/Rmario_walk_1.bmp')
                self.frames_ = ['assets/mario/Rmario_walk_1.bmp', 'assets/mario/Rmario_walk_2.bmp',
                                'assets/mario/Rmario_walk_3.bmp']
            if self.walk_an == "f":
                self.grow_up('assets/mario/Rfmario_walk_1.bmp')
                self.frames_ = ['assets/mario/Rfmario_walk_1.bmp', 'assets/mario/Rfmario_walk_2.bmp',
                                'assets/mario/Rfmario_walk_3.bmp']
            if self.walk_an == "s":
                self.grow_up('assets/mario/Rsmario_walk_1.bmp')
                self.frames_ = ['assets/mario/Rsmario_walk_1.bmp', 'assets/mario/Rsmario_walk_2.bmp',
                                'assets/mario/Rsmario_walk_3.bmp']
            self.timer.frames = self.frames_
            self.timer.reset()
            self.temp_go = 2

        if self.jumping and self.change_y == 0:
            self.change_y = -20
            self.jumping = False
            if self.state == "super" or self.state == "fire":
                pygame.mixer.Channel(1).play(music.big_j)
            else:
                pygame.mixer.Channel(1).play(music.small_j)
        if self.jumping_press and self.jump_scaler == 0:
            if self.jump_scaler < 20:
                self.jump_scaler += 2
            else:
                self.jumping_press = False
            self.change_y -= self.jump_scaler
        else:
            self.jump_scaler = 0

        ff = 1
        ma = 12
        if self.mov_right and self.fric < ma and not self.died and not self.flag:
            self.fric += ff
        elif self.fric > 0:
            self.fric -= ff
        if self.mov_left and self.fric > -ma and not self.died and not self.flag:
            self.fric -= ff
        elif self.fric < 0:
            self.fric += ff

        if self.change_x == 0 and self.change_y == 0 and not self.flag and not self.died and self.state != "dead":
            if self.dir_face == "right":
                self.frames_ = ['assets/mario/Rmario_stand.bmp']
                if self.star_power is True:
                    self.frames_ = ['assets/mario/Rmario_standi.bmp', 'assets/mario/Rmario_stand.bmp']
            if self.dir_face == "left":
                self.frames_ = ['assets/mario/Lmario_stand.bmp']
                if self.star_power is True:
                    self.frames_ = ['assets/mario/Lmario_standi.bmp', 'assets/mario/Lmario_stand.bmp']
            if self.state == "super":
                if self.dir_face == "right":
                    self.frames_ = ['assets/mario/Rsmario_stand.bmp']
                    if self.star_power is True:
                        self.frames_ = ['assets/mario/Rsmario_standi.bmp', 'assets/mario/Rsmario_stand.bmp']
                if self.dir_face == "left":
                    self.frames_ = ['assets/mario/Lsmario_stand.bmp']
                    if self.star_power is True:
                        self.frames_ = ['assets/mario/Lsmario_standi.bmp', 'assets/mario/Lsmario_stand.bmp']
            if self.state == "fire":
                if self.dir_face == "right":
                    self.frames_ = ['assets/mario/Rfmario_stand.bmp']
                    if self.star_power is True:
                        self.frames_ = ['assets/mario/Rsmario_standi.bmp', 'assets/mario/Rfmario_stand.bmp']
                if self.dir_face == "left":
                    self.frames_ = ['assets/mario/Lfmario_stand.bmp']
                    if self.star_power is True:
                        self.frames_ = ['assets/mario/Lsmario_standi.bmp', 'assets/mario/Lfmario_stand.bmp']
            self.timer.frames = self.frames_
            self.timer.reset()

        if self.mov_left and not self.mov_right and not self.flag and self.state != "dead":
            self.rect.x += self.change_x
            self.dir_face = "left"
            self.frames_ = ['assets/mario/Lmario_walk_1.bmp', 'assets/mario/Lmario_walk_2.bmp',
                            'assets/mario/Lmario_walk_3.bmp', 'assets/mario/Lmario_walk_1.bmp',
                            'assets/mario/Lmario_walk_2.bmp', 'assets/mario/Lmario_walk_3.bmp']
            if self.star_power is True:
                self.frames_ = ['assets/mario/Lmario_walk_1.bmp', 'assets/mario/Lmario_walk_2i.bmp',
                                'assets/mario/Lmario_walk_3.bmp', 'assets/mario/Lmario_walk_1i.bmp',
                                'assets/mario/Lmario_walk_2.bmp', 'assets/mario/Lmario_walk_3i.bmp']
            if self.state == "super":
                self.frames_ = ['assets/mario/Lsmario_walk_1.bmp', 'assets/mario/Lsmario_walk_2.bmp',
                                'assets/mario/Lsmario_walk_3.bmp', 'assets/mario/Lsmario_walk_1.bmp',
                                'assets/mario/Lsmario_walk_2.bmp', 'assets/mario/Lsmario_walk_3.bmp']
                if self.star_power is True:
                    self.frames_ = ['assets/mario/Lsmario_walk_1.bmp', 'assets/mario/Lsmario_walk_2i.bmp',
                                    'assets/mario/Lsmario_walk_3.bmp', 'assets/mario/Lsmario_walk_1i.bmp',
                                    'assets/mario/Lsmario_walk_2.bmp', 'assets/mario/Lsmario_walk_3i.bmp']
            if self.state == "fire":
                self.frames_ = ['assets/mario/Lfmario_walk_1.bmp', 'assets/mario/Lfmario_walk_2.bmp',
                                'assets/mario/Lfmario_walk_3.bmp', 'assets/mario/Lfmario_walk_1.bmp',
                                'assets/mario/Lfmario_walk_2.bmp', 'assets/mario/Lfmario_walk_3.bmp']
                if self.star_power is True:
                    self.frames_ = ['assets/mario/Lfmario_walk_1.bmp', 'assets/mario/Lsmario_walk_2i.bmp',
                                    'assets/mario/Lfmario_walk_3.bmp', 'assets/mario/Lsmario_walk_1i.bmp',
                                    'assets/mario/Lfmario_walk_2.bmp', 'assets/mario/Lsmario_walk_3i.bmp']

            self.timer.frames = self.frames_
            # self.timer.reset()

        if self.mov_right and not self.mov_left and self.state != "dead" and not self.flag:
            self.rect.x += self.change_x
            self.dir_face = "right"
            self.frames_ = ['assets/mario/Rmario_walk_1.bmp', 'assets/mario/Rmario_walk_2.bmp',
                            'assets/mario/Rmario_walk_3.bmp', 'assets/mario/Rmario_walk_1.bmp',
                            'assets/mario/Rmario_walk_2.bmp', 'assets/mario/Rmario_walk_3.bmp']
            if self.star_power is True:
                self.frames_ = ['assets/mario/Rmario_walk_1.bmp', 'assets/mario/Rmario_walk_2i.bmp',
                                'assets/mario/Rmario_walk_3.bmp', 'assets/mario/Rmario_walk_1i.bmp',
                                'assets/mario/Rmario_walk_2.bmp', 'assets/mario/Rmario_walk_3i.bmp']
            if self.state == "super":
                self.frames_ = ['assets/mario/Rsmario_walk_1.bmp', 'assets/mario/Rsmario_walk_2.bmp',
                                'assets/mario/Rsmario_walk_3.bmp', 'assets/mario/Rsmario_walk_1.bmp',
                                'assets/mario/Rsmario_walk_2.bmp', 'assets/mario/Rsmario_walk_3.bmp']
                if self.star_power is True:
                    self.frames_ = ['assets/mario/Rsmario_walk_1.bmp', 'assets/mario/Rsmario_walk_2i.bmp',
                                    'assets/mario/Rsmario_walk_3.bmp', 'assets/mario/Rsmario_walk_1i.bmp',
                                    'assets/mario/Rsmario_walk_2.bmp', 'assets/mario/Rsmario_walk_3i.bmp']
            if self.state == "fire":
                self.frames_ = ['assets/mario/Rfmario_walk_1.bmp', 'assets/mario/Rfmario_walk_2.bmp',
                                'assets/mario/Rfmario_walk_3.bmp', 'assets/mario/Rfmario_walk_1.bmp',
                                'assets/mario/Rfmario_walk_2.bmp', 'assets/mario/Rfmario_walk_3.bmp']
                if self.star_power is True:
                    self.frames_ = ['assets/mario/Rfmario_walk_1.bmp', 'assets/mario/Rsmario_walk_2i.bmp',
                                    'assets/mario/Rfmario_walk_3.bmp', 'assets/mario/Rsmario_walk_1i.bmp',
                                    'assets/mario/Rfmario_walk_2.bmp', 'assets/mario/Rsmario_walk_3i.bmp']
            self.timer.frames = self.frames_
            # self.timer.reset()

        if self.mov_right and self.fric < 0 and self.state != "dead" and not self.flag:
            self.frames_ = ['assets/mario/mario_turn2R.bmp', 'assets/mario/mario_turn2R.bmp']
            if self.star_power is True:
                self.frames_ = ['assets/mario/mario_turn2R.bmp', 'assets/mario/mario_turn2Ri.bmp']
            if self.state == "super":
                self.frames_ = ['assets/mario/smario_turn2R.bmp', 'assets/mario/smario_turn2R.bmp']
                if self.star_power is True:
                    self.frames_ = ['assets/mario/smario_turn2R.bmp', 'assets/mario/smario_turn2Ri.bmp']
            if self.state == "fire":
                self.frames_ = ['assets/mario/fmario_turn2R.bmp', 'assets/mario/fmario_turn2R.bmp']
                if self.star_power is True:
                    self.frames_ = ['assets/mario/fmario_turn2R.bmp', 'assets/mario/fmario_turn2Ri.bmp']

            self.timer.frames = self.frames_
            self.timer.reset()
        if self.mov_left and self.fric > 0 and self.state != "dead" and not self.flag:
            self.frames_ = ['assets/mario/mario_turn2L.bmp', 'assets/mario/mario_turn2L.bmp']
            if self.star_power is True:
                self.frames_ = ['assets/mario/mario_turn2L.bmp', 'assets/mario/mario_turn2Li.bmp']
            if self.state == "super":
                self.frames_ = ['assets/mario/smario_turn2L.bmp', 'assets/mario/smario_turn2L.bmp']
                if self.star_power is True:
                    self.frames_ = ['assets/mario/smario_turn2L.bmp', 'assets/mario/smario_turn2Li.bmp']
            if self.state == "fire":
                self.frames_ = ['assets/mario/fmario_turn2L.bmp', 'assets/mario/fmario_turn2L.bmp']
                if self.star_power is True:
                    self.frames_ = ['assets/mario/fmario_turn2L.bmp', 'assets/mario/fmario_turn2Li.bmp']
            self.timer.frames = self.frames_
            self.timer.reset()

        if self.inair and not self.died and not self.flag:
            if not self.landed and self.dir_face == "right":
                self.frames_ = ['assets/mario/Rmario_jump.bmp', 'assets/mario/Rmario_jump.bmp']
                if self.state == "super":
                    self.frames_ = ['assets/mario/Rsmario_jump.bmp', 'assets/mario/Rsmario_jump.bmp']
                if self.state == "fire":
                    self.frames_ = ['assets/mario/Rfmario_jump.bmp', 'assets/mario/Rfmario_jump.bmp']
                self.timer.frames = self.frames_
                self.timer.reset()
            if not self.landed and self.dir_face == "left":
                self.frames_ = ['assets/mario/Lmario_jump.bmp', 'assets/mario/Lmario_jump.bmp']
                if self.state == "super":
                    self.frames_ = ['assets/mario/Lsmario_jump.bmp', 'assets/mario/Lsmario_jump.bmp']
                if self.state == "fire":
                    self.frames_ = ['assets/mario/Lfmario_jump.bmp', 'assets/mario/Lfmario_jump.bmp']
                self.timer.frames = self.frames_
                self.timer.reset()

        if self.crouch and not self.flag and not self.died:
            if self.state == "fire" and self.dir_face == "right":
                self.grow_up('assets/mario/Rfmario_crouch.bmp')
                self.frames_ = ['assets/mario/Rfmario_crouch.bmp', 'assets/mario/Rfmario_crouch.bmp']
            if self.state == "fire" and self.dir_face == "left":
                self.grow_up('assets/mario/Rfmario_crouch.bmp')
                self.frames_ = ['assets/mario/Lfmario_crouch.bmp', 'assets/mario/Lfmario_crouch.bmp']
            if self.state == "super" and self.dir_face == "right":
                self.grow_up('assets/mario/Rfmario_crouch.bmp')
                self.frames_ = ['assets/mario/Rsmario_crouch.bmp', 'assets/mario/Rsmario_crouch.bmp']
            if self.state == "super" and self.dir_face == "left":
                self.grow_up('assets/mario/Rfmario_crouch.bmp')
                self.frames_ = ['assets/mario/Lsmario_crouch.bmp', 'assets/mario/Lsmario_crouch.bmp']
            self.timer.frames = self.frames_
            # self.timer.reset()

        # self.change_x = self.fric
        if self.rect.centerx < round(self.ai_settings.screen_width / 2) \
                and self.mov_right and not self.mov_left and not self.died and not self.flag:
            self.go_right()
        elif self.rect.centerx > round(self.ai_settings.screen_width / 2) and self.mov_right \
                and not self.mov_left and not self.died and not self.flag:
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
            if self.rect.colliderect(block.rect):
                if block.type_ == "winner":
                    self.state = "next!"
            if self.rect.colliderect(block.rect) and not self.flag and not self.death and block.type_ != "hidden":
                if self.change_x > 0 and block.type_ != "hidden":  # and self.rect.bottom != block.rect.top:
                    self.rect.right = block.rect.left
                elif self.change_x < 0 and block.type_ != "hidden":  # and self.rect.bottom != block.rect.top:
                    self.rect.left = block.rect.right
                if block.type_ == "winner":
                    self.state = "next!"

                if block.type_ == "invs":
                    self.next_level = self.state
                    if self.state == "fire":
                        self.state = "flagf"
                    if self.state == "super":
                        self.state = "flags"
                    if self.state == "reg":
                        self.state = "flagr"

        if self.state == "flagf" or self.state == "flags" or self.state == "flagr" and not self.flag:
            self.flag = True
            if self.state == "flagf":
                self.grow_up('assets/mario/Rfmario_pole_1.bmp')
                self.frames_ = ['assets/mario/Rfmario_pole_1.bmp']
                self.walk_an = "f"
            if self.state == "flags":
                self.grow_up('assets/mario/Rsmario_pole_1.bmp')
                self.frames_ = ['assets/mario/Rsmario_pole_1.bmp']
                self.walk_an = "s"
            if self.state == "flagr":
                self.grow_up('assets/mario/Rmario_pole_1.bmp')
                self.frames_ = ['assets/mario/Rmario_pole_1.bmp']
                self.walk_an = "r"
            self.timer.frames = self.frames_
            self.rect.x += 20
            self.timer.reset()
            self.state = "nextlevel"

        if not self.died and self.state != "dead" and self.rect.left > 0:
            self.change_x = self.fric
        if self.rect.left < 0:
            self.rect.left = 0
        self.calc_grav()

        self.rect.y += self.change_y
        for block in self.g_blocks:
            if self.rect.colliderect(block.rect) and not self.death and not self.flag:
                if self.change_y > 0 and block.type_ != "hidden":
                    self.rect.bottom = block.rect.top
                    self.landed = True
                elif self.change_y < 0:
                    self.rect.top = block.rect.bottom
                    self.jumping_press = False
                    self.cur_item(block, music, mario)
                    if block.type_ == "bricks" and (self.state == "super" or self.state == "fire"):
                        block.dead = 1
                self.change_y = 0

        if self.invinc > 0:
            self.invinc -= 1
        if self.invinc == 0 and self.star_power is True:
            self.star_power = False

        for enemy in self.enemies:
            if self.rect.right + 720 > enemy.rect.left:
                enemy.state = "active"
            if self.rect.colliderect(enemy.rect) and self.star_power is True:
                enemy.kill()

            if self.rect.colliderect(enemy.rect) and self.death is False and self.invinc == 0:
                if self.change_y > 0:
                    self.rect.bottom = enemy.rect.top
                    self.change_y = -5
                    self.jumping = True
                    self.change_y = 0
                    if enemy.state != "dead":
                        enemy.dead_enemy(music)
                elif enemy.type == "shell":
                    if self.dir_face == "right":
                        create_item(self.ai_settings, self.screen, self.g_blocks, self.bg_blocks, self,
                                    self.items, "shell_mov", enemy.rect.right, enemy.rect.bottom,
                                    enemy.rect.center, False, True)
                        enemy.kill()
                    elif self.dir_face == "left":
                        create_item(self.ai_settings, self.screen, self.g_blocks, self.bg_blocks, self,
                                    self.items, "shell_mov", enemy.rect.left, enemy.rect.bottom,
                                    enemy.rect.center, True, False)
                        enemy.kill()
                elif enemy.type == "bshell":
                    if self.dir_face == "right":
                        create_item(self.ai_settings, self.screen, self.g_blocks, self.bg_blocks, self,
                                    self.items, "bshell_mov", enemy.rect.right, enemy.rect.bottom,
                                    enemy.rect.center, False, True)
                        enemy.kill()
                    elif self.dir_face == "left":
                        create_item(self.ai_settings, self.screen, self.g_blocks, self.bg_blocks, self,
                                    self.items, "bshell_mov", enemy.rect.left, enemy.rect.bottom,
                                    enemy.rect.center, True, False)
                        enemy.kill()

                elif enemy.type != "shell":
                    if self.state == "reg":
                        self.death_blow = True
                    elif self.state == "fire":
                        self.invinc = 60
                        self.grow_up('assets/mario/Rsmario_stand.bmp')
                        self.state = "super"
                        pygame.mixer.Channel(5).play(music.pdown)
                    else:
                        self.invinc = 60
                        self.grow_up('assets/mario/Rmario_stand.bmp')
                        self.state = "reg"
                        pygame.mixer.Channel(5).play(music.pdown)
                self.change_y = 0

        for item in self.items:
            if self.rect.colliderect(item.rect) and self.death is False and item.type != "fireball":
                if item.type == "mushroom":
                    self.grow_up('assets/mario/Rsmario_stand.bmp')
                    self.state = "super"
                    pygame.mixer.Channel(2).play(music.pup)
                if item.type == "coin":
                    self.ai_settings.coins += 1
                    self.ai_settings.high_score -= 800
                    self.scores.prep_coins()
                    pygame.mixer.Channel(2).play(music.coin)
                if item.type == "star":
                    self.invinc = 300
                    self.star_power = True
                    pygame.mixer.Channel(2).play(music.pup)
                if item.type == "1upshroom":
                    self.ai_settings.mario_lives += 1
                    self.scores.prep_lives()
                    pygame.mixer.Channel(2).play(music.one_up)
                if self.state == "super" and item.type == "fireflower":
                    self.state = "fire"
                    pygame.mixer.Channel(2).play(music.pup)
                if self.state != "super" and item.type == "fireflower":
                    self.grow_up('assets/mario/Rsmario_stand.bmp')
                    pygame.mixer.Channel(2).play(music.pup)
                    self.state = "fire"
                if item.type != "shell_mov":
                    self.items.remove(item)
                self.ai_settings.high_score += 1000
                self.scores.prep_score()

        if self.rect.y >= 720 - self.rect.height and self.change_y >= 0 and not self.died or self.death_blow:
            self.change_y = -26
            self.jumping = False
            self.death = True
            self.died = True
            self.state = "dead"
            self.death_blow = False
            self.frames_ = ['assets/mario/mario_dead.bmp']
            self.timer.frames = self.frames_
            self.fric = 0
            self.change_x = 0
            self.timer.reset()

    def hurt(self):
        temp1 = self.screen_rect
        temp2 = self.rect.centerx
        temp3 = self.rect.bottom
        temp4 = self.center
        im = pygame.image.load('assets/mario/Lmario_mid')
        self.rect = im.get_rect()
        self.screen_rect = temp1
        self.rect.centerx = temp2
        self.rect.bottom = temp3
        self.center = temp4

    def grow_up(self, str_):
        temp1 = self.screen_rect
        temp2 = self.rect.centerx
        temp3 = self.rect.bottom
        temp4 = self.center
        im = pygame.image.load(str_)
        self.rect = im.get_rect()
        self.screen_rect = temp1
        self.rect.centerx = temp2
        self.rect.bottom = temp3
        self.center = temp4

    def calc_grav(self):
        if self.change_y == 0:
            self.change_y = 2
        else:
            if self.state == "nextlevel":
                self.change_y += .5
            else:
                self.change_y += 2

        if self.state != "nextlevel" and self.state != "goright":
            if self.rect.y >= 720 - self.rect.height and self.change_y >= 0 and not self.died:
                self.change_y = 0
                self.rect.y = 720 - self.rect.height
        else:
            if self.rect.y >= 720 - (48 * 2) - self.rect.height and self.change_y >= 0 and not self.died:
                self.change_y = 0
                self.rect.y = 720 - (48 * 2) - self.rect.height
                self.state = "goright"

    def blitme(self):
        if not(self.invinc == 10 or self.invinc == 20 or self.invinc == 30 or self.invinc == 40):
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

    def cur_item(self, block, music, mario):
        if (block.type_ == "pup" or block.type_ == "pup2" or block.type_ == "pup3") \
                and self.state == "reg":
            if self.dir_face == "right":
                left = False
                right = True
            else:
                left = True
                right = False
            create_item(self.ai_settings, self.screen, self.g_blocks, self.bg_blocks, self, self.items,
                        "mushroom", float(block.rect.x) + 25,
                        block.rect.bottom - 60,
                        float(block.rect.x), left, right)
        if (block.type_ == "pup" or block.type_ == "pup2" or block.type_ == "pup3") \
                and (self.state == "super" or self.state == "fire"):
            create_item(self.ai_settings, self.screen, self.g_blocks, self.bg_blocks, self, self.items,
                        "fireflower", float(block.rect.x) + 25,
                        block.rect.bottom - 30,
                        float(block.rect.x), False, False)

        if block.type_ == "qcoin" or block.type_ == "qcoin2":
            create_item(self.ai_settings, self.screen, self.g_blocks, self.bg_blocks, self, self.items,
                        "coin", float(block.rect.x) + 25,
                        block.rect.bottom - 30,
                        float(block.rect.x), False, False)

        if block.type_ == "hidden" or block.type_ == "1up2":
            create_item(self.ai_settings, self.screen, self.g_blocks, self.bg_blocks, self, self.items,
                        "1upshroom", float(block.rect.x) + 25,
                        block.rect.bottom - 30,
                        float(block.rect.x), False, True)

        if block.type_ == "bcoin" or block.type_ == "bcoin2":
            create_item(self.ai_settings, self.screen, self.g_blocks, self.bg_blocks, self, self.items,
                        "coin", float(block.rect.x) + 25,
                        block.rect.bottom - 30,
                        float(block.rect.x), False, False)

        if block.type_ == "star" or block.type_ == "star2":
            create_item(self.ai_settings, self.screen, self.g_blocks, self.bg_blocks, self, self.items,
                        "star", float(block.rect.x) + 25,
                        block.rect.bottom - 60,
                        float(block.rect.x), False, True)

        block.blipup(music, mario)
