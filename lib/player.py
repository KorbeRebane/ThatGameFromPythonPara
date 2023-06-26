import pygame as pg

from lib.constants import PLAYER_FILENAME, START_POSITION_X, PLAYER_SPEED, \
    START_POSITION_Y, HEALTH_POINTS, PLAYER_DAMAGE, WIN_POSITION, PLAYER_SPEED_LIST, PLAYER_ATTACK_FILENAME, \
    TIME_OF_ATTACK, FALLING_SPEED
from lib.creature import Creature


class Player(Creature):
    MOVEMENT_SPEED = PLAYER_SPEED

    def __init__(self):
        super().__init__(PLAYER_FILENAME, PLAYER_ATTACK_FILENAME, [START_POSITION_X, START_POSITION_Y], HEALTH_POINTS,
                         PLAYER_DAMAGE)

    def game_states(self):
        if self.health_points != 0:
            if self.position[0] >= WIN_POSITION[0]:
                pass
            else:
                return "game"
        elif self.health_points == 0:
            self.health_points = 3
            return "menu"

    def move(self, pressed_keys, upped_keys, platform_rects, can_we_move):  # can_we_move - открыт ли текст
        if pg.K_d in pressed_keys or pg.K_RIGHT in pressed_keys:
            self.walking_right = True
        if pg.K_d in upped_keys or pg.K_RIGHT in upped_keys:
            self.walking_right = False
        if pg.K_a in pressed_keys or pg.K_LEFT in pressed_keys:
            self.walking_left = True
        if pg.K_a in upped_keys or pg.K_LEFT in upped_keys:
            self.walking_left = False
        if pg.K_s in pressed_keys or pg.K_DOWN in pressed_keys:
            self.speed[1] = FALLING_SPEED
        if pg.K_SPACE in pressed_keys or pg.K_w in pressed_keys or pg.K_UP in pressed_keys:
            self.in_jump = True

        else:
            self.in_jump = False

        self.move_physically(platform_rects, can_we_move)

    def player_attack(self, mouse_pressed):
        if mouse_pressed == 1:
            self.image = self.attack_image
            self.is_attacking = True
            self.not_idle_counter = TIME_OF_ATTACK


    def get_damage_from_enemy(self, enemy, rect_for_enemy, damage):
        if enemy.is_attacking and not self.is_attacking and (
        self.rect.colliderect(rect_for_enemy)):
            self.health_points -= damage




