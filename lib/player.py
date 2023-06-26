import pygame as pg
from pygame import Rect

from lib.constants import PLAYER_FILENAME, START_POSITION_X, PLAYER_SPEED, \
    START_POSITION_Y, HEALTH_POINTS, PLAYER_DAMAGE, PLAYER_SPEED_LIST, PLAYER_ATTACK_FILENAME, \
    TIME_OF_ATTACK, VIEW_RADIUS, PLAYER_HEIGHT, PLAYER_WIDTH, DELTA_T, FALLING_SPEED
from lib.creature import Creature

class Player(Creature):
    MOVEMENT_SPEED = PLAYER_SPEED

    def __init__(self):
        super().__init__(PLAYER_FILENAME, PLAYER_ATTACK_FILENAME, [START_POSITION_X, START_POSITION_Y], HEALTH_POINTS, PLAYER_DAMAGE)

    def move(self, pressed_keys, upped_keys, platform_rects, can_we_move): # can_we_move - открыт ли текст
        if pg.K_d in pressed_keys or pg.K_RIGHT in pressed_keys:
            self.walking_right = True
        if pg.K_d in upped_keys or pg.K_RIGHT in upped_keys:
            self.walking_right = False
        if pg.K_a in pressed_keys or pg.K_LEFT in pressed_keys:
            self.walking_left = True
        if pg.K_a in upped_keys or pg.K_LEFT in upped_keys:
            self.walking_left = False
        if pg.K_s in pressed_keys or pg.K_DOWN in pressed_keys:
            if pg.Rect.collidelist(self.under_zone.move(PLAYER_SPEED * -1 * DELTA_T, -1), platform_rects) != -1:
                self.position[1] = self.position[1] + 50 + PLAYER_HEIGHT
            else:
                self.speed[1] = FALLING_SPEED
        if pg.K_SPACE in pressed_keys or pg.K_w in pressed_keys or pg.K_UP in pressed_keys:
            self.in_jump = True
        else:
            self.in_jump = False


        self.move_physically(platform_rects, can_we_move)

    def attack(self, mouse_pressed):
        if mouse_pressed == 1:
            self.image = self.attack_image
            self.not_idle_counter = TIME_OF_ATTACK
            self.is_attacking = True

    # def on_start_conditions(self): # Возвращает игрока в изначальное состояние
    #     self.position[0] = START_POSITION_X
    #     self.position[1] = START_POSITION_Y
    #     self.walking_left = False
    #     self.walking_right = False
    #     self.health_points = HEALTH_POINTS
    #     self.in_jump = False
    def player_attack(self, mouse_pressed):
        if mouse_pressed == 1:
            self.image = self.attack_image
            self.is_attacking = True
            self.not_idle_counter = TIME_OF_ATTACK

    def get_damage_from_enemy(self, enemy, rect_for_enemy, damage):
        if enemy.is_attacking and not self.is_attacking and self.rect.colliderect(rect_for_enemy):
            self.health_points -= damage

    def hp_regen(self):
        if self.health_points < HEALTH_POINTS:
            self.health_points += 1

    @property
    def under_zone(self):
        x = self.position[0]
        y = self.position[1] + self.image.get_height()
        width = self.image.get_width() / 2
        height = 50
        return Rect(x, y, width, height)
