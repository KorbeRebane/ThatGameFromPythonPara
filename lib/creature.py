import pygame as pg
from pygame import Rect

from lib.constants import PLAYER_FILENAME, SCALE, START_POSITION_X, PLAYER_SPEED, \
    START_POSITION_Y, HEALTH_POINTS, PLAYER_DAMAGE, WIN_POSITION, PLAYER_SPEED_LIST, JUMP_SPEED, DELTA_T, G, \
    SCREEN_HEIGHT, PLAYER_HEIGHT
from lib.utilities import scale_image


class Creature:
    def __init__(self, image, position, health_points, damage):
        self.image = pg.image.load(image)
        self.image = scale_image(self.image, SCALE)
        self.image_rect = self.image.get_rect()

        self.position = position
        self.speed = PLAYER_SPEED_LIST
        self.health_points = health_points
        self.damage = damage

        self.walking_left = False
        self.walking_right = False
        self.jumps_count = 1

    def draw(self, surface):
        surface.blit(self.image, self.position)

    def jump(self):
        if self.jumps_count >= 0:
            self.speed[1] = -JUMP_SPEED
            self.jumps_count -= 1

    def move(self, pressed_keys, upped_keys, platform_rects):
        if pg.K_d in pressed_keys:
            self.walking_right = True
        if pg.K_d in upped_keys:
            self.walking_right = False
        if pg.K_a in pressed_keys:
            self.walking_left = True
        if pg.K_a in upped_keys:
            self.walking_left = False

        if self.walking_right and not self.walking_left:
            self.speed[0] = PLAYER_SPEED
        else:
            self.speed[0] = 0
        if self.walking_right and pg.Rect.collidelist(self.rect.move(PLAYER_SPEED * DELTA_T, -1), platform_rects) != -1:
            self.speed[0] = 0

        if self.walking_left and not self.walking_right:
            self.speed[0] = -PLAYER_SPEED
        if self.walking_left and pg.Rect.collidelist(self.rect.move(PLAYER_SPEED * -DELTA_T, -1), platform_rects) != -1:
            self.speed[0] = 0

        if pg.K_SPACE in pressed_keys:
            self.jump()

        self.position[0] += self.speed[0] * DELTA_T
        self.position[1] += self.speed[1] * DELTA_T
        if not pg.Rect.collidelist(self.rect.move(0, 1), platform_rects) == -1:
            self.position[1] -= self.speed[1] * DELTA_T
            self.speed[1] = 0
            self.jumps_count = 1
        else:
            self.speed[1] += G * DELTA_T

    def get_damage(self, damage):
        # тут будут условия на получение урона
        self.health_points -= damage

    def give_damage(self):
        # тут будут условия нанесения урона
        return self.damage

    def get_player_position(self):
        return self.position

    def get_health_points(self):
        return self.health_points

    @property
    def rect(self):
        x = self.position[0]
        y = self.position[1]
        width = self.image.get_width()
        height = self.image.get_height()
        return Rect(x, y, width, height)
