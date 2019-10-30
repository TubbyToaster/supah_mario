import pygame


class Music:

    def __init__(self):
        self.normal = True
        self.normal_playing = True
        self.speedup_normal = False
        self.speedup_normal_playing = False
        self.underg = False
        self.underg_playing = False
        self.speedup_underg = False
        self.speedup_underg_playing = False
        self.star = False
        self.star_playing = False
        self.pipe = False
        self.pipe_playing = False
        self.flagpole = False
        self.flagpole_playing = False
        self.dies = False
        self.dies_playing = False
        self.game_over = False
        self.game_over_playing = False
        self.level_complete = False
        self.level_complete_playing = False

        self.one_up = pygame.mixer.Sound("assets/audio/1_up.wav")
        self.small_j = pygame.mixer.Sound("assets/audio/small_jump.wav")
        self.big_j = pygame.mixer.Sound("assets/audio/big_jump.wav")
        self.stomp = pygame.mixer.Sound("assets/audio/stomp.wav")
        self.bbreak = pygame.mixer.Sound("assets/audio/brick_break.wav")
        self.bbump = pygame.mixer.Sound("assets/audio/brick_bump.wav")
        self.coin = pygame.mixer.Sound("assets/audio/coin.wav")
        self.fb = pygame.mixer.Sound("assets/audio/fireball.wav")
        self.pup = pygame.mixer.Sound("assets/audio/power_up.wav")
        self.pup_spawn = pygame.mixer.Sound("assets/audio/power_up_appears.wav")

    def change_bg_music(self):
        if self.normal is True and not self.normal_playing:
            pygame.mixer.music.load("assets/audio/bg_music_1.wav")
            pygame.mixer.music.play(-1)
            self.normal_playing = True

            self.underg = False
            self.underg_playing = False
            self.speedup_normal = False
            self.speedup_normal_playing = False
            self.speedup_underg = False
            self.speedup_underg_playing = False
            self.star = False
            self.star_playing = False
            self.pipe = False
            self.pipe_playing = False
            self.flagpole = False
            self.flagpole_playing = False
            self.dies = False
            self.dies_playing = False
            self.game_over = False
            self.game_over_playing = False
            self.level_complete = False
            self.level_complete_playing = False
        elif self.speedup_normal is True and not self.speedup_normal_playing:
            pygame.mixer.music.load("assets/audio/speedup_bg_music_1.wav")
            pygame.mixer.music.play(-1)
            self.speedup_normal_playing = True

            self.underg = False
            self.underg_playing = False
            self.normal = False
            self.normal_playing = False
            self.speedup_underg = False
            self.speedup_underg_playing = False
            self.star = False
            self.star_playing = False
            self.pipe = False
            self.pipe_playing = False
            self.flagpole = False
            self.flagpole_playing = False
            self.dies = False
            self.dies_playing = False
            self.game_over = False
            self.game_over_playing = False
            self.level_complete = False
            self.level_complete_playing = False
        elif self.underg is True and not self.underg_playing:
            pygame.mixer.music.load("assets/audio/bg_music_2.wav")
            pygame.mixer.music.play(-1)
            self.underg_playing = True

            self.normal = False
            self.normal_playing = False
            self.speedup_normal = False
            self.speedup_normal_playing = False
            self.speedup_underg = False
            self.speedup_underg_playing = False
            self.star = False
            self.star_playing = False
            self.pipe = False
            self.pipe_playing = False
            self.flagpole = False
            self.flagpole_playing = False
            self.dies = False
            self.dies_playing = False
            self.game_over = False
            self.game_over_playing = False
            self.level_complete = False
            self.level_complete_playing = False
        elif self.speedup_underg is True and not self.speedup_underg_playing:
            pygame.mixer.music.load("assets/audio/speedup_bg_music_2.wav")
            pygame.mixer.music.play(-1)
            self.speedup_underg_playing = True

            self.underg = False
            self.underg_playing = False
            self.speedup_normal = False
            self.speedup_normal_playing = False
            self.normal = False
            self.normal_playing = False
            self.star = False
            self.star_playing = False
            self.pipe = False
            self.pipe_playing = False
            self.flagpole = False
            self.flagpole_playing = False
            self.dies = False
            self.dies_playing = False
            self.game_over = False
            self.game_over_playing = False
            self.level_complete = False
            self.level_complete_playing = False
        elif self.star is True and not self.star_playing:
            pygame.mixer.music.load("assets/audio/star.wav")
            pygame.mixer.music.play()
            self.star_playing = True

            self.underg = False
            self.underg_playing = False
            self.speedup_normal = False
            self.speedup_normal_playing = False
            self.speedup_underg = False
            self.speedup_underg_playing = False
            self.normal = False
            self.normal_playing = False
            self.pipe = False
            self.pipe_playing = False
            self.flagpole = False
            self.flagpole_playing = False
            self.dies = False
            self.dies_playing = False
            self.game_over = False
            self.game_over_playing = False
            self.level_complete = False
            self.level_complete_playing = False
        elif self.pipe is True and not self.pipe_playing:
            pygame.mixer.music.load("assets/audio/pipe.wav")
            pygame.mixer.music.play()
            self.pipe_playing = True

            self.underg = False
            self.underg_playing = False
            self.speedup_normal = False
            self.speedup_normal_playing = False
            self.speedup_underg = False
            self.speedup_underg_playing = False
            self.star = False
            self.star_playing = False
            self.normal = False
            self.normal_playing = False
            self.flagpole = False
            self.flagpole_playing = False
            self.dies = False
            self.dies_playing = False
            self.game_over = False
            self.game_over_playing = False
            self.level_complete = False
            self.level_complete_playing = False
        elif self.flagpole is True and not self.flagpole_playing:
            pygame.mixer.music.load("assets/audio/flagpole.wav")
            pygame.mixer.music.play()
            self.flagpole_playing = True

            self.underg = False
            self.underg_playing = False
            self.speedup_normal = False
            self.speedup_normal_playing = False
            self.speedup_underg = False
            self.speedup_underg_playing = False
            self.star = False
            self.star_playing = False
            self.pipe = False
            self.pipe_playing = False
            self.normal = False
            self.normal_playing = False
            self.dies = False
            self.dies_playing = False
            self.game_over = False
            self.game_over_playing = False
            self.level_complete = False
            self.level_complete_playing = False
        elif self.dies is True and not self.dies_playing:
            pygame.mixer.music.load("assets/audio/dies.wav")
            pygame.mixer.music.play()
            self.dies_playing = True

            self.underg = False
            self.underg_playing = False
            self.speedup_normal = False
            self.speedup_normal_playing = False
            self.speedup_underg = False
            self.speedup_underg_playing = False
            self.star = False
            self.star_playing = False
            self.pipe = False
            self.pipe_playing = False
            self.flagpole = False
            self.flagpole_playing = False
            self.normal = False
            self.normal_playing = False
            self.game_over = False
            self.game_over_playing = False
            self.level_complete = False
            self.level_complete_playing = False
        elif self.game_over is True and not self.game_over_playing:
            pygame.mixer.music.load("assets/audio/game_over.wav")
            pygame.mixer.music.play()
            self.game_over_playing = True

            self.underg = False
            self.underg_playing = False
            self.speedup_normal = False
            self.speedup_normal_playing = False
            self.speedup_underg = False
            self.speedup_underg_playing = False
            self.star = False
            self.star_playing = False
            self.pipe = False
            self.pipe_playing = False
            self.flagpole = False
            self.flagpole_playing = False
            self.dies = False
            self.dies_playing = False
            self.normal = False
            self.normal_playing = False
            self.level_complete = False
            self.level_complete_playing = False
        elif self.level_complete is True and not self.level_complete_playing:
            pygame.mixer.music.load("assets/audio/level_complete1.wav")
            pygame.mixer.music.play()
            self.level_complete_playing = True

            self.underg = False
            self.underg_playing = False
            self.speedup_normal = False
            self.speedup_normal_playing = False
            self.speedup_underg = False
            self.speedup_underg_playing = False
            self.star = False
            self.star_playing = False
            self.pipe = False
            self.pipe_playing = False
            self.flagpole = False
            self.flagpole_playing = False
            self.dies = False
            self.dies_playing = False
            self.game_over = False
            self.game_over_playing = False
            self.normal = False
            self.normal_playing = False

    def check_speedup(self):
        if self.normal is True:
            self.normal = False
            self.speedup_normal = True
        elif self.underg is True:
            self.underg = False
            self.speedup_underg = True
