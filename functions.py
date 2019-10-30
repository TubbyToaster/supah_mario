import sys
import pygame
from blocks import Blocks
from enemy import Enemy
from items import Items


def check_keyup_events(ai_settings, screen, event, mario, g_blocks, bg_blocks, items):
    if event.key == pygame.K_RIGHT:
        mario.mov_right = False
        mario.change_x = 0
    elif event.key == pygame.K_LEFT:
        mario.mov_left = False
        mario.change_x = 0
    if event.key == pygame.K_UP:
        mario.jumping_press = False
    if event.key == pygame.K_DOWN:
        mario.crouch = False
        if mario.state == "super" or mario.state == "fire":
            mario.grow_up('assets/mario/Rsmario_stand.bmp')
    if event.key == pygame.K_SPACE and mario.state == "fire":
        mario.fireball()
        if mario.dir_face == "left":
            create_item(ai_settings, screen, g_blocks, bg_blocks, mario, items, "fireball", float(mario.rect.x)+5,
                        mario.rect.bottom-30,
                        float(mario.rect.x+10), True, False)

        if mario.dir_face == "right":
            create_item(ai_settings, screen, g_blocks, bg_blocks, mario, items, "fireball", float(mario.rect.x)+50,
                        mario.rect.bottom-30,
                        float(mario.rect.x+40), False, True)


def check_keydown_events(event, mario):
    if event.key == pygame.K_RIGHT and not mario.died:
        mario.mov_right = True
    elif event.key == pygame.K_LEFT and not mario.died:
        mario.mov_left = True
        mario.go_left()
    elif event.key == pygame.K_DOWN and not mario.died:
        mario.crouch = True

    if event.key == pygame.K_UP and mario.landed == True and not mario.died:
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


def create_enemy(ai_settings, screen, g_blocks, bg_blocks, mario, enemies, type, rcenter, bottom, center, items):
    enemy = Enemy(ai_settings, screen, g_blocks, bg_blocks, mario, type, rcenter, bottom, center, items)
    enemies.add(enemy)


def create_item(ai_settings, screen, g_blocks, bg_blocks, mario, items, type, rcenter, bottom, center, mov_left,
                mov_right):
    item = Items(ai_settings, screen, g_blocks, bg_blocks, mario, type, rcenter, bottom, center, mov_left, mov_right)
    items.add(item)

def check_time(ai_settings, scores):
    ai_settings.update_time()
    scores.prep_time()

def check_events(ai_settings, screen, mario, g_blocks, bg_blocks, monitor, items):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, mario)
        elif event.type == pygame.KEYUP:
            check_keyup_events(ai_settings, screen, event, mario, g_blocks, bg_blocks, items)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()

def new_level(ai_settings, screen, mario, g_blocks, bg_blocks, enemies, monitor, chunks, items, scores):
    mario.rect.centerx = mario.screen_rect.centerx - 200
    mario.rect.bottom = mario.screen_rect.bottom - 200
    mario.center = float(mario.rect.centerx)
    mario.flag = False
    for el in bg_blocks:
        bg_blocks.remove(el)
    for el in g_blocks:
        g_blocks.remove(el)
    for el in enemies:
        enemies.remove(el)
    for el in chunks:
        chunks.remove(el)



def update_screen(ai_settings, screen, mario, g_blocks, bg_blocks, enemies, monitor, chunks, items, scores):
    screen.fill(ai_settings.bg_color)


    if mario.state == "next!" and monitor.cur == 2:
        new_level(ai_settings, screen, mario, g_blocks, bg_blocks, enemies, monitor, chunks, items, scores)
        monitor.cur = 3

    if mario.death == True and mario.rect.bottom > 1300:
        for el in items:
            items.remove(el)
        mario.grow_up('assets/mario/Rmario_stand.bmp')
        monitor.cur = 1
        mario.death = False
        mario.died = False
        mario.death_blow = False
        new_level(ai_settings, screen, mario, g_blocks, bg_blocks, enemies, monitor, chunks, items, scores)
        mario.state = "reg"

    monitor.update(monitor.level_list)


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
        if el.image_index > 3:
            g_blocks.remove(el)

    for chunk in chunks:
        if chunk.check_edge < 1:
            chunks.remove(chunk)

    for enemy in enemies:
        enemy.blitme()
        enemy.update()

    for item in items:
        item.blitme()
        item.update()

    mario.blitme()

    scores.show_score()

    pygame.display.flip()
