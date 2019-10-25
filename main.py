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
        "111111111111111"
    ]

    a2 = [
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
        "000000000000023",
        "000000000000054",
        "111111111111111",
        "111111111111111"
    ]
    g1_1_1 = Chunk(ai_settings, screen, g_blocks, bg_blocks, a1)
    g1_1_2 = Chunk(ai_settings, screen, g_blocks, bg_blocks, a2)
    g1_1_1.gen(0, "g")
    g1_1_2.gen(720, "g")

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
        "aaaaaaaaaaaaaaa"
    ]

    b2 = [
        "bbbbbbbbbbbbbbb",
        "bbbbbbbbbbbbbbb",
        "bbbbpqrbbbbbbbb",
        "bbbbstubbbbbpqq",
        "bbbbbbbbbbbbstt",
        "bbbbbbbbbbbbbbb",
        "bbbbbbbbbbbbbbb",
        "bbbbbbbbbbbbbbb",
        "bbbbbbbbbbbbbbb",
        "bbbbbbbbbbbbbbb",
        "bbbbbbbbbbbbbbb",
        "bbhbbbbbbbbbbbb",
        "ogkibbbbmnobbbb",
        "aaaaaaaaaaaaaaa",
        "aaaaaaaaaaaaaaa"
    ]
    bg1_1_1 = Chunk(ai_settings, screen, g_blocks, bg_blocks, b1)
    bg1_1_2 = Chunk(ai_settings, screen, g_blocks, bg_blocks, b2)
    bg1_1_1.gen(0, "bg")
    bg1_1_2.gen(720, "bg")
    while True:
        gf.check_events(ai_settings, screen, mario)
        mario.update(g_blocks, bg_blocks)

        gf.update_screen(ai_settings, screen, mario, g_blocks, bg_blocks)
        mainClock.tick(40)


run_game()
