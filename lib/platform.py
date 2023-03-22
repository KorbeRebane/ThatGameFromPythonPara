import pygame as pg
from lib.constants import PLATFORM_HEIGHT, PLATFORM_WIDTH, FLOOR_HEIGHT, PLAYER_WIDTH, \
    PLATFORM_FILENAME, SCALE, PLATFORM_POSITION_Y, PLATFORM_POSITION_X
from lib.utilities import scale_image


class Platform:
    def __init__(self):
        self.platform_image = pg.image.load(PLATFORM_FILENAME)
        self.platform_image = scale_image(self.platform_image, SCALE)

        self.platform_position = [PLATFORM_POSITION_X, PLATFORM_POSITION_Y]
        self.is_player_contact_left = False
        self.is_player_contact_right = False

    def draw(self, surface):
        surface.blit(self.platform_image, self.platform_position)

    def contact_with_player(self, player_position):
        if player_position[0] == self.platform_position[0] - PLAYER_WIDTH:
            self.is_player_contact_right = True
        elif player_position[0] == self.platform_position[0] + PLATFORM_WIDTH:
            self.is_player_contact_left = True
        else:
            self.is_player_contact_right = False
            self.is_player_contact_left = False
        return self.is_player_contact_left, self.is_player_contact_right

class PlatformBuilder:
    def __init__(self):
        pass
