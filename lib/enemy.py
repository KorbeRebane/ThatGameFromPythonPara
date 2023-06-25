import pygame as pg
import random

from lib.constants import ENEMY_FILENAME, HEALTH_POINTS_ENEMY, ENEMY_DAMAGE, HEALTH_POINTS, PLAYER_SPEED, \
    DELTA_T, PLATFORM_HEIGHT, PLAYER_DAMAGE, TIME_OF_ATTACK, ENEMY_ATTACK_FILENAME, SPEED_OF_ATTACK_ENEMY
from lib.creature import Creature



class Enemy(Creature):
    MOVEMENT_SPEED = PLAYER_SPEED*0.5
    NUMBER_OF_JUMPS = 0

    def __init__(self, position):
        super().__init__(ENEMY_FILENAME, ENEMY_ATTACK_FILENAME, position, HEALTH_POINTS_ENEMY, ENEMY_DAMAGE)
        self.attack_timer = 0
        self.attack_frame_counter = 0


    def move(self, platform_rects, player, can_we_move): # can_we_move - открыт ли текст
        if player.view_zone.colliderect(self.rect):
            if self.position[0] >= player.position[0]:
                self.walking_left = True
                self.walking_right = False
            elif self.position[0] <= player.position[0]:
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


    def enemy_attack(self, enemy_rect_in_attack, rect_player_in_idle):
        if enemy_rect_in_attack.colliderect(rect_player_in_idle):
            if self.attack_timer == 0:
                self.image = self.attack_image
                self.is_attacking = True
                self.attack_timer = SPEED_OF_ATTACK_ENEMY  # Устанавливаем таймер на заданное количество кадров
                self.attack_frame_counter = 0  # Сбрасываем счетчик кадров
            else:
                self.is_attacking = False


    def get_damage_from_player(self, player, damage): #self = enemy
        if player.is_attacking and player.rect_for_fight.colliderect(self.rect):
            self.health_points -= damage




