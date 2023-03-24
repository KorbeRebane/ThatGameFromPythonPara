import pygame as pg
from pygame import Rect

from lib.constants import ENEMY_FILENAME, SCALE, HEALTH_POINTS_ENEMY, ENEMY_DAMAGE
from lib.utilities import scale_image


class Enemy:
    def __init__(self, enemy_position):
        self.enemy_image = pg.image.load(ENEMY_FILENAME)
        self.enemy_image = scale_image(self.enemy_image, SCALE)
        self.enemy_image_rect = self.enemy_image.get_rect()

        self.health_points = HEALTH_POINTS_ENEMY
        self.position = enemy_position
        self.damage = ENEMY_DAMAGE
        self.is_alive = True

    def draw(self, surface):
        if self.is_alive:
            surface.blit(self.enemy_image, self.position)

    def give_damage(self):
        # тут будут условия на нанесение урона
        return self.damage

    def get_damage(self, player_rect):
        # тут будут условия на получение урона
        if player_rect.colliderect(self.rect):
            self.health_points -= 1
        # dying
        if self.health_points == 0:
            self.is_alive = False

    def dying(self):
        if self.health_points == 0:
            self.is_alive = False

    @property
    def rect(self):
        x = self.position[0]
        y = self.position[1]
        width = self.enemy_image.get_width()
        height = self.enemy_image.get_height()
        return Rect(x, y, width, height)