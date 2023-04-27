import pygame as pg
from pygame import Rect

from lib.constants import PLATFORM_FILENAME, SCALE
from lib.utilities import scale_image


class Platform:
    def __init__(self, position, texture):
        self.platform_image = pg.image.load(texture)
        self.platform_image = scale_image(self.platform_image, SCALE)

        self.platform_position = position

    def draw(self, surface, camera_position):
        new_x = self.platform_position[0] - camera_position[0]
        new_y = self.platform_position[1] - camera_position[1]
        surface.blit(self.platform_image, [new_x, new_y])

    @property
    def rect(self):
        x = self.platform_position[0]
        y = self.platform_position[1]
        width = self.platform_image.get_width()
        height = self.platform_image.get_height()
        return Rect(x, y, width, height)
