import pygame.font


class Scoreboard:
    # a class to report scoring info

    def __init__(self, ai_settings, screen):
        # initialize scorekeeping attributes
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.ai_settings = ai_settings
        self.sliv = (self.ai_settings.screen_width / 5)

        # font settings for scoring info
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 48)

        # prepare the initial score images
        self.score_image = None
        self.score_rect = None
        self.score_title = None
        self.score_title_rect = None
        self.prep_score()

        self.coins_img = None
        self.coins_rect = None
        self.coin_title = None
        self.coin_title_rect = None
        self.prep_coins()

        self.time_img = None
        self.time_rect = None
        self.time_title = None
        self.time_title_rect = None
        self.prep_time()

        self.level_image = None
        self.level_rect = None
        self.level_title = None
        self.level_title_rect = None
        self.prep_level()

        self.lives_img = None
        self.lives_rect = None
        self.lives_title = None
        self.lives_title_rect = None
        self.prep_lives()

    def prep_time(self):
        # turn the high score into a rendered image
        time = self.ai_settings.time
        time_str = str(time)
        self.time_img = self.font.render(time_str, True, self.text_color)
        self.time_title = self.font.render("TIME", True, self.text_color)

        # put time at the top of the screen
        self.time_rect = self.time_img.get_rect()
        self.time_title_rect = self.time_title.get_rect()
        self.time_title_rect.centerx = (self.sliv*2) - 75
        self.time_title_rect.top = 5
        self.time_rect.centerx = (self.sliv*2) - 75
        self.time_rect.top = 40

    def prep_coins(self):
        # turn the high score into a rendered image
        coins = self.ai_settings.coins
        coins_str = str(coins)
        self.coins_img = self.font.render(coins_str, True, self.text_color)
        self.coin_title = self.font.render("COINS", True, self.text_color)

        # put time at the top of the screen
        self.coins_rect = self.coins_img.get_rect()
        self.coin_title_rect = self.coin_title.get_rect()
        self.coin_title_rect.centerx = (self.sliv*4) - 75
        self.coin_title_rect.top = 5
        self.coins_rect.centerx = (self.sliv*4) - 75
        self.coins_rect.top = 40

    def prep_score(self):
        # turn the score into a rendered image
        score = self.ai_settings.high_score
        score_str = str(score)
        self.score_image = self.font.render(score_str, True, self.text_color)
        self.score_title = self.font.render("SCORE", True, self.text_color)

        # display the score on the screen
        self.score_rect = self.score_image.get_rect()
        self.score_title_rect = self.score_title.get_rect()
        self.score_rect.centerx = (self.sliv*1) - 75
        self.score_rect.top = 40
        self.score_title_rect.centerx = (self.sliv*1) - 75
        self.score_title_rect.top = 5

    def show_score(self):
        # draw score and ships to the screen
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.score_title, self.score_title_rect)

        self.screen.blit(self.time_img, self.time_rect)
        self.screen.blit(self.time_title, self.time_title_rect)

        self.screen.blit(self.level_image, self.level_rect)
        self.screen.blit(self.level_title, self.level_title_rect)

        self.screen.blit(self.coins_img, self.coins_rect)
        self.screen.blit(self.coin_title, self.coin_title_rect)

        self.screen.blit(self.lives_img, self.lives_rect)
        self.screen.blit(self.lives_title, self.lives_title_rect)

    def prep_level(self):
        # turn the level into a rendered image
        if self.ai_settings.level == 1:
            self.level_image = self.font.render(str("1-1"), True,
                                                self.text_color)
        self.level_title = self.font.render("WORLD", True, self.text_color)

        # position on screen
        self.level_rect = self.level_image.get_rect()
        self.level_title_rect = self.level_title.get_rect()
        self.level_title_rect.centerx = (self.sliv*3) - 75
        self.level_title_rect.top = 5
        self.level_rect.centerx = (self.sliv*3) - 75
        self.level_rect.top = 40

    def prep_lives(self):
        # turn the high score into a rendered image
        lives = self.ai_settings.mario_lives
        lives_str = str(lives)
        self.lives_img = self.font.render(lives_str, True, self.text_color)
        self.lives_title = self.font.render("LIVES", True, self.text_color)

        # put time at the top of the screen
        self.lives_rect = self.lives_img.get_rect()
        self.lives_title_rect = self.lives_title.get_rect()
        self.lives_title_rect.centerx = (self.sliv*5) - 75
        self.lives_title_rect.top = 5
        self.lives_rect.centerx = (self.sliv*5) - 75
        self.lives_rect.top = 40

