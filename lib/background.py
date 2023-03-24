import pygame as pg

from lib.constants import FLOOR_HEIGHT, SCALE, BACKGROUND_FILENAME, FLOOR_FILENAME, FONT_SIZE
from lib.utilities import scale_image


class Background:
    def __init__(self):
        self.fon_image = pg.image.load(BACKGROUND_FILENAME)
        self.fon_image = scale_image(self.fon_image, SCALE)
        self.floor_image = pg.image.load(FLOOR_FILENAME)
        self.floor_image = scale_image(self.floor_image, SCALE)

        self.axis_font = pg.font.Font(None, FONT_SIZE)

    def draw_game_window(self, surface):
        surface.blit(self.fon_image, (0, 0))
        # self.draw_floor(surface)

    def draw_floor(self, surface):
        surface.blit(self.floor_image, (0, FLOOR_HEIGHT))







