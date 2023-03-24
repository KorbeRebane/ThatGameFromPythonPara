import pygame as pg
from pygame import Rect

from lib.constants import PLATFORM_FILENAME, SCALE
from lib.utilities import scale_image


class Platform:
    def __init__(self, platform_position, texture):
        self.platform_image = pg.image.load(texture)
        self.platform_image = scale_image(self.platform_image, SCALE)

        self.platform_position = platform_position

    def draw(self, surface):
        surface.blit(self.platform_image, self.platform_position)

    @property
    def rect(self):
        x = self.platform_position[0]
        y = self.platform_position[1]
        width = self.platform_image.get_width()
        height = self.platform_image.get_height()
        return Rect(x, y, width, height)
