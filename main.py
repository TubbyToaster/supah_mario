import pygame
from pygame.sprite import Group
from mario import Mario
from settings import Settings
from blocks import Blocks
import functions as gf
from level_gen import Chunk

mainClock = pygame.time.Clock()


def run_game():
    pygame.init()
    pygame.display.set_caption("Mario")
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))

    g_blocks = Group()
    bg_blocks = Group()
    mario = Mario(ai_settings, screen, g_blocks)

    #gf.create_blocks(ai_settings, screen, blocks, 500, 368+32, 400)
    #gf.create_blocks(ai_settings, screen, blocks, 500, 280, 400)
    #gf.create_blocks(ai_settings, screen, blocks, 500+32, 280, 400)
    #gf.create_blocks(ai_settings, screen, blocks, 500+64, 280, 400)
    a1 = [
        "000000000000000",
        "000000000000000",
        "000000000000000",
        "000000000000000",
        "000000000000000",
        "000000000000000",
        "000000000000000",
        "000000000000000",
        "000000000000000",
        "000000000000000",
        "000000000000000",
        "000000000000000",
        "000000000000000",
        "111111111111111",
        "111111111111111",

    ]
    test = Chunk(ai_settings, screen, g_blocks, bg_blocks, a1)
    test.gen(0, "g")

    b1 = [
        "bbbbbbbbbbbbbbb",
        "bbbbbbbbbbbbbbb",
        "bbbbbbbbbdbbbbb",
        "bbbbbbbbcefbbbb",
        "bbbbbbbbbbbbbbb",
        "bbbbbbbbbbbbbbb",
        "bbbbbbbbbbbbbbb",
        "bbbbbbbbbbbbbbb",
        "bbbbbbbbbbbbbbb",
        "bbbbbbbbbbbbbbb",
        "bbhbbbbbbbbbbbb",
        "bgkibbbbbbbbbbb",
        "gkjlibbbbbbmnnn",
        "aaaaaaaaaaaaaaa",
        "aaaaaaaaaaaaaaa",

    ]
    test2 = Chunk(ai_settings, screen, g_blocks, bg_blocks, b1)
    test2.gen(0, "bg")
    while True:
        gf.check_events(ai_settings, screen, mario)
        mario.update()

        gf.update_screen(ai_settings, screen, mario, g_blocks, bg_blocks)
        mainClock.tick(40)


run_game()
