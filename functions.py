   import sys
import pygame
from blocks import Blocks
import random


def check_keyup_events(event, mario):
    if event.key == pygame.K_RIGHT:
        mario.moving_right = False
    elif event.key == pygame.K_LEFT:
        mario.moving_left = False
    if event.key == pygame.K_UP:
        mario.jumping_press = False


def check_keydown_events(event, mario):
    if event.key == pygame.K_RIGHT:
        mario.moving_right = True
    elif event.key == pygame.K_LEFT:
        mario.moving_left = True

    if event.key == pygame.K_UP:
        if not mario.jumping:
            mario.jumping = True
        if not mario.inair:
            mario.inair = True
        mario.jumping_press = True


def create_g_blocks(ai_settings, screen, image, g_blocks, rx, ry, xx):
    block = Blocks(ai_settings, screen, image, rx, ry)
    block.rect.y = ry
    block.rect.x = rx
    block.x = xx
    g_blocks.add(block)


def create_bg_blocks(ai_settings, screen, image, bg_blocks, rx, ry, xx):
    block = Blocks(ai_settings, screen, image, rx, ry)
    block.rect.y = ry
    block.rect.x = rx
    block.x = xx
    bg_blocks.add(block)


def check_events(ai_settings, screen, mario):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, mario)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, mario)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()


def update_screen(ai_settings, screen, mario, g_blocks, bg_blocks):
    screen.fill(ai_settings.bg_color)

    for el in g_blocks:
        el.blitme()
        el.update_frame()
        if el.image_index > 3:
            g_blocks.remove(el)

    for el in bg_blocks:
        el.blitme()
        el.update_frame()
        if el.image_index > 3:
            g_blocks.remove(el)

    mario.blitme()

    pygame.display.flip()
