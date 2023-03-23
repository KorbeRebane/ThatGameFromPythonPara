import sys

import pygame as pg

from menu.button import Button


class MenuManager:

    def __init__(self):
        self.game_starts = False

        self.buttons = []
        button_new_game = Button(size=(200, 50),
                                 position=(200, 400),
                                 text="Новая игра",
                                 color="white",
                                 on_click=self.new_game)
        self.buttons.append(button_new_game)
        button_exit = Button(size=(200, 50),
                             position=(200, 600),
                             text="Выход",
                             color="white",
                             on_click=self.exit)
        self.buttons.append(button_exit)

    def update(self, pressed_keys, upped_keys):
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
        surface.fill((100, 0, 0))
        for button in self.buttons:
            button.draw(surface)

    def new_game(self):
        self.game_starts = True

    def exit(self):
        pg.quit()
        sys.exit()

