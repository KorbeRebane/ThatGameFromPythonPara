import pygame as pg
from pygame import Rect

from lib.constants import PLATFORM_FILENAME, SCALE, FLOOR_HEIGHT, LEVEL_WIDTH, PLATFORM_HEIGHT, PLATFORM_WIDTH
from lib.utilities import scale_image


class Platform:
    def __init__(self, position, size, texture):
        self.platform_image = pg.image.load(texture)
        self.platform_size = size
        self.platform_image = pg.transform.scale(self.platform_image, self.platform_size)

        self.platform_position = position

    def draw(self, surface, camera_position):
        new_x = self.platform_position[0] - camera_position[0]
        new_y = self.platform_position[1] - camera_position[1]
        surface.blit(self.platform_image, [new_x, new_y])

    @property
    def rect(self):
        x = self.platform_position[0]
        y = self.platform_position[1]
        # width = self.platform_image.get_width()
        # height = self.platform_image.get_height()
        width = self.platform_size[0]
        height = self.platform_size[1]
        return Rect(x, y, width, height)
