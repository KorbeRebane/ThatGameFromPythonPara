import sys

import pygame as pg

from lib.constants import BUTTON_NEW_GAME_SIZE_WIDTH, SCALE, BUTTON_NEW_GAME_SIZE_HEIGHT, BUTTON_NEW_GAME_POSITION_Y, \
    BUTTON_NEW_GAME_POSITION_X, BUTTON_EXIT_SIZE_WIDTH, BUTTON_EXIT_POSITION_X, BUTTON_EXIT_POSITION_Y, \
    BUTTON_EXIT_SIZE_HEIGHT
from menu.button import Button


class MenuManager:

    def __init__(self):
        self.game_starts = False

        # Список нажатых кнопок
        self.buttons = []

        # Кнопка новой игры
        button_new_game = Button(size=(BUTTON_NEW_GAME_SIZE_WIDTH * SCALE, BUTTON_NEW_GAME_SIZE_HEIGHT * SCALE),
                                 position=(BUTTON_NEW_GAME_POSITION_X * SCALE, BUTTON_NEW_GAME_POSITION_Y * SCALE),
                                 text="Новая игра",
                                 color="white",
                                 on_click=self.new_game)
        self.buttons.append(button_new_game)

        # Кнопка выхода
        button_exit = Button(size=(BUTTON_EXIT_SIZE_WIDTH * SCALE, BUTTON_EXIT_SIZE_HEIGHT * SCALE),
                             position=(BUTTON_EXIT_POSITION_X * SCALE, BUTTON_EXIT_POSITION_Y * SCALE),
                             text="Выход",
                             color="white",
                             on_click=self.exit)
        self.buttons.append(button_exit)

    def update(self, pressed_keys, upped_keys, mouse_pressed, mouse_upped):
        if pg.mouse.get_pressed()[0]:
            mouse_position = pg.mouse.get_pos()
            mouse_x, mouse_y = mouse_position
            for button in self.buttons:
                if button.position[0] < mouse_x < button.position[0] +\
                     button.size[0] and \
                     button.position[1] < mouse_y < button.position[1] + \
                     button.size[1]:

                    button.clicked()

        if self.game_starts:
            self.game_starts = False
            return "game"

        return "menu"

    def draw(self, surface):
        surface.fill((0, 0, 0))
        for button in self.buttons:
            button.draw(surface)

    def new_game(self):
        self.game_starts = True

    def exit(self):
        pg.quit()
        sys.exit()

