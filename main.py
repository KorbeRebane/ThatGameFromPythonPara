import sys

import pygame as pg

from lib.constants import speed_y, FPS, SCREEN_WIDTH, SCREEN_HEIGHT
from lib.man import Man

pg.init()

screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pg.time.Clock()

background_image = pg.image.load('source/images/wallpaper_cut.jpg')
floor_image = pg.image.load('source/images/floor.png')

man_x = 230
man_y = 560
speed_y = 100
man = Man(position=(man_x, man_y),
          speed=(0, speed_y))


walking_right = False
walking_left = False


while True:
    screen.blit(background_image, (0,0))
    screen.blit(floor_image, (0,600))
    screen.blit(man.image, man.position)

    jump = False
    falling = False


    pg.display.update() # Обновляет пиксели. Без нее будет у себя обновлять, но на экран выводить не будет :)
    clock.tick(FPS) # Колчичество FPS

    events = pg.event.get()

    for event in events:
        need_to_exit = False

        if event.type == pg.KEYDOWN:
            if event.key == pg.K_ESCAPE:
                need_to_exit = True
            if event.key in [pg.K_SPACE, pg.K_w, pg.K_UP]:
                jump = True
            if event.key in [pg.K_d, pg.K_RIGHT]:
                walking_right = True
            if event.key in [pg.K_a, pg.K_LEFT]:
                walking_left = True
            if event.key in [pg.K_s, pg.K_DOWN]:
                falling = True

        if event.type == pg.KEYUP:
            if event.key in [pg.K_a, pg.K_LEFT]:
                walking_left = False
            if event.key in [pg.K_d, pg.K_RIGHT]:
                walking_right = False

        if event.type == pg.QUIT:
            need_to_exit = True

        if need_to_exit:
            pg.quit()
            sys.exit()

    man.move(jump, walking_right, walking_left, falling)