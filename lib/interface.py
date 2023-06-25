import pygame as pg

from lib.constants import SCALE, \
     PLAYER_FILENAME, GREEN, RED, BLACK
from lib.utilities import scale_image
import pygame as pg



class GameScreen:
    def __init__(self):
        self.image = pg.image.load(PLAYER_FILENAME)


