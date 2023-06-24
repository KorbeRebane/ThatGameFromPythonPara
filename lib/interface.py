import pygame as pg

from lib.constants import SCALE, HEALTH_POINT_FILENAME, \
    HEALTH_POINT_SIZE, HEALTH_POINT_POSITION_X_PLAYER, PLAYER_FILENAME, GREEN, RED, BLACK
from lib.utilities import scale_image
import pygame as pg
from pygame import Rect, draw


class GameScreen:
    def __init__(self):
        self.health_points_image = pg.image.load(HEALTH_POINT_FILENAME)
        self.health_points_image = scale_image(self.health_points_image, SCALE)
        self.image = pg.image.load(PLAYER_FILENAME)


