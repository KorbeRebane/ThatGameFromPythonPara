import sys

import pygame as pg

from lib.constants import BUTTON_NEW_GAME_SIZE_WIDTH, SCALE, BUTTON_NEW_GAME_SIZE_HEIGHT, BUTTON_NEW_GAME_POSITION_Y, \
    BUTTON_NEW_GAME_POSITION_X, BUTTON_EXIT_SIZE_WIDTH, BUTTON_EXIT_POSITION_X, BUTTON_EXIT_POSITION_Y, \
    BUTTON_EXIT_SIZE_HEIGHT
from menu.button import Button


class MenuManager:

    def __init__(self):
        self.level_list = False #Мы сейчас на списке уровней?

        # Список нажатых кнопок
        self.buttons = []

        # Кнопка новой игры
        button_new_game = Button(size=(BUTTON_NEW_GAME_SIZE_WIDTH * SCALE, BUTTON_NEW_GAME_SIZE_HEIGHT * SCALE),
                                 position=(BUTTON_NEW_GAME_POSITION_X * SCALE, BUTTON_NEW_GAME_POSITION_Y * SCALE),
                                 text="Играть",
                                 color="white",
                                 on_click=self.to_level_list)
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

        if self.level_list:
            self.level_list = False
            return "level_list", -1

        return "menu", -1

    def draw(self, surface):
        surface.fill((0, 0, 0))
        for button in self.buttons:
            button.draw(surface)

    def to_level_list(self):
        self.level_list = True

    def exit(self):
        pg.quit()
        sys.exit()

class LevelListManager:

    def __init__(self):
        self.start_level = -1 # Мы начали уровень?
        self.return_to_menu = False

        # Список нажатых кнопок
        self.buttons = []

        # Кнопка 0 уровня
        button_zero_level = Button(size=(BUTTON_NEW_GAME_SIZE_WIDTH * 2 * SCALE, BUTTON_NEW_GAME_SIZE_HEIGHT * SCALE),
                                 position=((BUTTON_NEW_GAME_POSITION_X-300) * SCALE, (BUTTON_NEW_GAME_POSITION_Y-200) * SCALE),
                                 text="Тестовый уровень",
                                 color="white",
                                 on_click=lambda : self.startt_level(1))
        self.buttons.append(button_zero_level)

        # Кнопка 1 уровня
        button_first_level = Button(size=(BUTTON_NEW_GAME_SIZE_WIDTH * 2 * SCALE, BUTTON_NEW_GAME_SIZE_HEIGHT * SCALE),
                                   position=((BUTTON_NEW_GAME_POSITION_X - 300) * SCALE,
                                             (BUTTON_NEW_GAME_POSITION_Y - 100) * SCALE),
                                   text="Первый уровень",
                                   color="white",
                                   on_click=lambda : self.startt_level(2))
        self.buttons.append(button_first_level)

        # Кнопка 2 уровня
        button_second_level = Button(size=(BUTTON_NEW_GAME_SIZE_WIDTH * 2 * SCALE, BUTTON_NEW_GAME_SIZE_HEIGHT * SCALE),
                                   position=((BUTTON_NEW_GAME_POSITION_X - 300) * SCALE,
                                             (BUTTON_NEW_GAME_POSITION_Y - 0) * SCALE),
                                   text="Второй уровень",
                                   color="white",
                                   on_click=lambda : self.startt_level(3))
        self.buttons.append(button_second_level)

        # Кнопка 3 уровня
        button_third_level = Button(size=(BUTTON_NEW_GAME_SIZE_WIDTH * 2 * SCALE, BUTTON_NEW_GAME_SIZE_HEIGHT * SCALE),
                                   position=((BUTTON_NEW_GAME_POSITION_X - 300) * SCALE,
                                             (BUTTON_NEW_GAME_POSITION_Y + 100) * SCALE),
                                   text="Третий уровень",
                                   color="white",
                                   on_click=lambda : self.startt_level(4))
        self.buttons.append(button_third_level)

        # Кнопка возврата в меню
        to_menu_button = Button(size=(BUTTON_EXIT_SIZE_WIDTH * 2 * SCALE, BUTTON_EXIT_SIZE_HEIGHT * SCALE),
                             position=((BUTTON_EXIT_POSITION_X - 300) * SCALE, (BUTTON_EXIT_POSITION_Y + 100) * SCALE),
                             text="В меню",
                             color="white",
                             on_click=self.to_menu)
        self.buttons.append(to_menu_button)

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

        if self.start_level > 0: # Идём на уровень
            return "game", self.start_level

        if self.return_to_menu and self.start_level < 0: # Идём в меню
            self.return_to_menu = False
            return "menu", -1

        return "level_list", -1

    def draw(self, surface):
        surface.fill((0, 0, 0))
        for button in self.buttons:
            button.draw(surface)

    def startt_level(self, n):
        self.start_level = n

    def to_menu(self):
        self.return_to_menu = True
