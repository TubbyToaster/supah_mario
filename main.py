import pygame
from pygame.sprite import Group
from mario import Mario
from settings import Settings
from level_gen import Chunk
from level_monitor import Monitor
from enemy import Enemy
from blocks import Blocks
import functions as gf

mainClock = pygame.time.Clock()


def run_game():
    pygame.init()
    pygame.display.set_caption("Mario")
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))

    g_blocks = Group()
    bg_blocks = Group()
    enemies = Group()
    chunks = Group()
    items = Group()

    monitor = Monitor(ai_settings, screen, g_blocks, bg_blocks, chunks)
    mario = Mario(ai_settings, screen, g_blocks, bg_blocks, enemies, monitor, chunks, items)

    #gf.create_enemy(ai_settings, screen, g_blocks, bg_blocks, mario, enemies, "reg", 500, 100, 500)
    #gf.create_enemy(ai_settings, screen, g_blocks, bg_blocks, mario, enemies, "reg", 520, 400, 500)

    gf.create_item(ai_settings, screen, g_blocks, bg_blocks, mario, items, "fireflower", 500, 400, 500, True, False)

    while True:
        gf.check_events(ai_settings, screen, mario, g_blocks, bg_blocks, monitor, items)
        mario.update()

        gf.update_screen(ai_settings, screen, mario, g_blocks, bg_blocks, enemies, monitor, chunks, items)

        mainClock.tick(40)


run_game()
