import sys
import pygame
from blocks import Blocks
from enemy import Enemy
import random


def check_keyup_events(event, mario, g_blocks, bg_blocks):
    if event.key == pygame.K_RIGHT:
        mario.mov_right = False
        mario.change_x = 0
    elif event.key == pygame.K_LEFT:
        mario.mov_left = False
        mario.change_x = 0
    if event.key == pygame.K_UP:
        mario.jumping_press = False


def check_keydown_events(event, mario):
    if event.key == pygame.K_RIGHT:
        mario.mov_right = True
        mario.go_right()
    elif event.key == pygame.K_LEFT:
        mario.mov_left = True
        mario.go_left()

    if event.key == pygame.K_UP and mario.landed == True:
        mario.landed = False
        if not mario.jumping:
            mario.jumping = True
        if not mario.inair:
            mario.inair = True
        mario.jumping_press = True


def create_g_blocks(ai_settings, screen, image, g_blocks, rx, ry, xx, type_):
    block = Blocks(ai_settings, screen, image, rx, ry, 0, type_)
    block.rect.y = ry
    block.rect.x = rx
    block.x = xx
    g_blocks.add(block)



def create_bg_blocks(ai_settings, screen, image, bg_blocks, rx, ry, xx, type_):
    block = Blocks(ai_settings, screen, image, rx, ry, 0, type_)
    block.rect.y = ry
    block.rect.x = rx
    block.x = xx
    bg_blocks.add(block)


def create_enemy(ai_settings, screen, g_blocks, bg_blocks, mario, enemies, type, rcenter, bottom, center, ):
    enemy = Enemy(ai_settings, screen, g_blocks, bg_blocks, mario, type, rcenter, bottom, center)
    enemies.add(enemy)


def check_events(ai_settings, screen, mario, g_blocks, bg_blocks, monitor):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, mario)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, mario, g_blocks, bg_blocks)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()


def update_screen(ai_settings, screen, mario, g_blocks, bg_blocks, enemies, monitor, chunks):
    screen.fill(ai_settings.bg_color)

    monitor.update()

    for el in bg_blocks:
        el.blitme()
        el.update_frame()
        if el.rect.x < -60:
            bg_blocks.remove(el)
            monitor.pos += 1
        if el.image_index > 3:
            bg_blocks.remove(el)

    for el in g_blocks:
        el.blitme()
        el.update_frame()
        if el.rect.x < -60:
            g_blocks.remove(el)
            monitor.pos += 1
            print(monitor.pos)
        if el.image_index > 3:
            g_blocks.remove(el)

    for chunk in chunks:
        if chunk.check_edge < 1:
            chunks.remove(chunk)


    for enemy in enemies:
        enemy.blitme()
        enemy.update()
    mario.blitme()

    pygame.display.flip()

