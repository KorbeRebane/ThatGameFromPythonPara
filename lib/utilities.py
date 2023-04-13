import sys
import pygame as pg


def get_all_pressed_keys():
    pressed_keys = []
    upped_keys = []

    events = pg.event.get()
    for event in events:
        # Проверка на выход из игры
        need_to_exit = False
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_ESCAPE:
                need_to_exit = True
            else:
                pressed_keys.append(event.key)
        if event.type == pg.KEYUP:
            upped_keys.append(event.key)
        if event.type == pg.QUIT:
            need_to_exit = True
        if need_to_exit:
            pg.quit()
            sys.exit()

    return pressed_keys, upped_keys


def scale_image(image, scale):
    width = image.get_width()
    height = image.get_height()
    new_size = (width * scale, height * scale)
    return pg.transform.scale(image, new_size)

