import pygame as pg

from lib.constants import ENEMY_FILENAME, SCALE, HEALTH_POINTS_ENEMY, ENEMY_POSITION_X, ENEMY_POSITION_Y, ENEMY_DAMAGE, \
    PLAYER_WIDTH
from lib.utilities import scale_image


class Enemy:
    def __init__(self):
        self.enemy_image = pg.image.load(ENEMY_FILENAME)
        self.enemy_image = scale_image(self.enemy_image, SCALE)

        self.health_points = HEALTH_POINTS_ENEMY
        self.enemy_position = (ENEMY_POSITION_X, ENEMY_POSITION_Y)
        self.enemy_damage = ENEMY_DAMAGE
        self.is_alive = True

    def draw(self, surface):
        if self.is_alive:
            surface.blit(self.enemy_image, self.enemy_position)

    def give_damage(self):
        # тут будут условия на нанесение урона
        return self.enemy_damage

    def get_damage(self, player_position):
        # тут будут условия на получение урона
        if player_position[0] + PLAYER_WIDTH == self.enemy_position[0]:
            self.health_points -= 1
        # dying
        if self.health_points == 0:
            self.is_alive = False

    def dying(self):
        if self.health_points == 0:
            self.is_alive = False

class EnemySpawner:
    pass