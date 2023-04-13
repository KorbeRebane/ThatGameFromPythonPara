import pygame as pg

from lib.constants import SCALE, HEALTH_POINT_FILENAME, HEALTH_POINT_POSITION_X, HEALTH_POINT_POSITION_Y, \
    HEALTH_POINT_SIZE
from lib.utilities import scale_image


class GameScreen:
    def __init__(self):
        self.health_points_image = pg.image.load(HEALTH_POINT_FILENAME)
        self.health_points_image = scale_image(self.health_points_image, SCALE)

    def draw_health_points(self, surface, health_points_count):
        for i in range(health_points_count):
            surface.blit(self.health_points_image, [HEALTH_POINT_POSITION_X + 2*i*HEALTH_POINT_SIZE,
                                                    HEALTH_POINT_POSITION_Y])