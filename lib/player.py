import pygame as pg
from pygame import Rect

from lib.constants import PLAYER_FILENAME, SCALE, START_POSITION_X, PLAYER_SPEED, \
    START_POSITION_Y, HEALTH_POINTS, PLAYER_DAMAGE, WIN_POSITION
from lib.utilities import scale_image


class Player:
    def __init__(self):
        self.player_image = pg.image.load(PLAYER_FILENAME)
        self.player_image = scale_image(self.player_image, SCALE)

        self.player_position = [START_POSITION_X, START_POSITION_Y]
        self.health_points = HEALTH_POINTS
        self.player_damage = PLAYER_DAMAGE

    def draw(self, surface):
        surface.blit(self.player_image, self.player_position)

    def move(self, pressed_keys, upped_keys, contact):
        if pg.K_d in pressed_keys and not contact[1]:
            self.player_position[0] += PLAYER_SPEED
        if pg.K_a in pressed_keys and not contact[0]:
            self.player_position[0] -= PLAYER_SPEED

    def get_damage(self):
        # тут будут условия на получение урона
        self.health_points -= 1

    def give_damage(self):
        # тут будут условия нанесения урона
        return self.player_damage

    def game_states(self):
        if self.health_points != 0:
            if self.player_position[0] == WIN_POSITION[0]:
                self.player_position[0] = START_POSITION_X
                self.health_points = 3
                return "menu"
            else:
                return "game"
        elif self.health_points == 0:
            self.health_points = 3
            return "menu"

    def get_player_position(self):
        return self.player_position

    def get_player_health_points(self):
        return self.health_points
    
    @property
    def rect(self):
        x = self.player_position[0]
        y = self.player_position[1]
        width = self.player_image.get_width()
        height = self.player_image.get_height()
        return Rect(x, y, width, height)
