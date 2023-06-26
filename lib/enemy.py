import time

import pygame as pg
import random

from .constants import ENEMY_FILENAME, HEALTH_POINTS_ENEMY, ENEMY_DAMAGE, HEALTH_POINTS, PLAYER_SPEED, \
    DELTA_T, PLATFORM_HEIGHT, PLAYER_DAMAGE
from .creature import Creature


class Enemy(Creature):
    MOVEMENT_SPEED = PLAYER_SPEED*0.5
    NUMBER_OF_JUMPS = 0

    def __init__(self, position):
        super().__init__(ENEMY_FILENAME, ENEMY_FILENAME, position, HEALTH_POINTS_ENEMY, ENEMY_DAMAGE)

    def get_damage(self, player_rect):
        # тут будут условия на получение урона
        if player_rect.colliderect(self.rect):
            self.health_points -= PLAYER_DAMAGE
        # dying
        if self.health_points == 0:
            self.is_alive = False

    def move(self, platform_rects, player, can_we_move):  # can_we_move - открыт ли текст
        if player.view_zone.colliderect(self.rect):
            if self.position[0] >= player.position[0]:
                self.walking_left = True
                self.walking_right = False
            elif self.position[0] <= player.position[0]:
                self.walking_right = True
                self.walking_left = False
            elif int(self.position[0]) == int(player.position[0]):
                random_index = random.choice([1, 2])
                if random_index == 1:
                    self.walking_left = True
                    self.walking_right = False
                elif random_index == 2:
                    self.walking_right = True
                    self.walking_left = False

        if not player.view_zone.colliderect(self.rect):

            if self.speed[0] == 0:
                random_index = random.choice([1, 2])
                if random_index == 1:
                    self.walking_left = True
                    self.walking_right = False
                elif random_index == 2:
                    self.walking_right = True
                    self.walking_left = False

        if player.view_zone.colliderect(self.rect) and pg.Rect.collidelist(self.view_zone.move(PLAYER_SPEED * -DELTA_T, -1), platform_rects) != -1 \
        and ((player.position[1] + PLATFORM_HEIGHT) > self.position[1] > player.position[1]): # если игрок в поле зрения И
            # И спустя 20 тиков предположительно враг врезался бы в платформу И игрок в определённом диапазоне высоты
            self.jump()

        self.move_physically(platform_rects + [player.rect], can_we_move)
