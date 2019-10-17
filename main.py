import pygame
from pygame.sprite import Group
from mario import Mario
from settings import Settings
from blocks import Blocks
import functions as gf


def run_game():
    pygame.init()
    pygame.display.set_caption("Mario")
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))

    blocks = Group()
    mario = Mario(ai_settings, screen, blocks)

    gf.create_blocks(ai_settings, screen, blocks, 500, 368+32, 400)
    gf.create_blocks(ai_settings, screen, blocks, 500, 280, 400)
    gf.create_blocks(ai_settings, screen, blocks, 500+32, 280, 400)
    gf.create_blocks(ai_settings, screen, blocks, 500+64, 280, 400)
    while True:
        gf.check_events(ai_settings, screen, mario)
        mario.update()

        gf.update_screen(ai_settings, screen, mario, blocks)


run_game()
