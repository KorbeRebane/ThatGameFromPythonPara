from copy import copy

import pygame as pg
from pygame import Rect, draw


from lib.constants import SCALE, PLAYER_SPEED, PLAYER_SPEED_LIST, JUMP_SPEED, DELTA_T, G, \
    GENERAL_MOVEMENT_SPEED, VIEW_RADIUS, PLAYER_HEIGHT, NUMBER_OF_JUMPS, \
    RADIUS_OF_ATTACK_FORWARD, RADIUS_OF_ATTACK_BACK

from lib.utilities import scale_image



class Creature:
    MOVEMENT_SPEED = GENERAL_MOVEMENT_SPEED
    number_of_jumps = NUMBER_OF_JUMPS - 1

    def __init__(self, image, attack_image, position, health_points, damage):
        self.attack_image = pg.image.load(attack_image)
        self.attack_image = scale_image(self.attack_image, SCALE)
        self.idle_image = pg.image.load(image)
        self.idle_image = scale_image(self.idle_image, SCALE)
        self.image = self.idle_image
        self.image_rect = self.image.get_rect()

        self.position = copy(position)
        self.speed = copy(PLAYER_SPEED_LIST)
        self.health_points = health_points
        self.damage = damage

        self.walking_left = False
        self.walking_right = False
        self.looking_left = False
        self.in_jump = False
        self.jumps_count = 1

        self.not_idle_counter = 0
        self.is_alive = True
        self.is_attacking = False
        # self.camera = Camera()

    def draw(self, surface, camera_position):
        new_x = self.position[0] - camera_position[0]
        new_y = self.position[1] - camera_position[1]
        if self.is_alive:
            if not self.looking_left:
                surface.blit(self.image, [new_x, new_y])
            else:
                image = pg.transform.flip(self.image, True, False)
                surface.blit(image, [new_x, new_y])
        self.return_to_idle()


    def return_to_idle(self):
        if self.not_idle_counter != 0:
            self.not_idle_counter -= 1
        if self.not_idle_counter == 0:
            self.image = self.idle_image
        self.is_attacking = False

    def jump(self):
        if self.jumps_count >= 0:
            self.speed[1] = -JUMP_SPEED
            self.jumps_count -= 1

    def move_physically(self, platform_rects, can_we_move): # can_we_move - открыт ли текст
        if not can_we_move:
            if self.in_jump:
                self.jump()

            if self.walking_right and not self.walking_left:
                self.speed[0] = self.MOVEMENT_SPEED
                self.looking_left = False
            else:
                self.speed[0] = 0
            if self.walking_right and pg.Rect.collidelist(self.rect.move(PLAYER_SPEED * DELTA_T, -1), platform_rects) != -1:
                self.speed[0] = 0

            if self.walking_left and not self.walking_right:
                self.speed[0] = -self.MOVEMENT_SPEED
                self.looking_left = True
            if self.walking_left and pg.Rect.collidelist(self.rect.move(PLAYER_SPEED * -DELTA_T, -1), platform_rects) != -1:
                self.speed[0] = 0

            self.position[0] += self.speed[0] * DELTA_T
            self.position[1] += self.speed[1] * DELTA_T
            if pg.Rect.collidelist(self.rect.move(0, 1), platform_rects) != -1:
                self.position[1] = platform_rects[pg.Rect.collidelist(self.rect.move(0, 1), platform_rects)][1] - PLAYER_HEIGHT
                self.speed[1] = 0
                self.jumps_count = self.number_of_jumps
            else:
                self.speed[1] += G * DELTA_T



    def give_damage(self):
        # тут будут условия нанесения урона
        return self.damage

    def intersection(self, object):
        return object.colliderect(self.rect_for_enemy)



    @property
    def get_health_points(self):
        return self.health_points

    @property
    def rect(self):
        x = self.position[0]
        y = self.position[1]
        width = self.image.get_width()
        height = self.image.get_height()
        return Rect(x, y, width, height)

    @property
    def rect_for_fight(self): # Радиус, когда враг начинает на носить урон
        x = self.position[0] - RADIUS_OF_ATTACK_BACK
        # x = self.position[0]
        y = self.position[1]
        width = self.image.get_width() + RADIUS_OF_ATTACK_FORWARD
        # width = self.image.get_width()
        height = self.image.get_height()
        return Rect(x, y, width, height)

    @property
    def view_zone(self):
        x = self.position[0] - VIEW_RADIUS # На плюс ВИЕВ_РАДИУС от нашей позиции видим
        y = self.position[1] - VIEW_RADIUS
        width = self.image.get_width() + 2*VIEW_RADIUS # один ВИЕВ_РАДИУС в одну сторону и один в другую
        height = self.image.get_height() + VIEW_RADIUS
        return Rect(x, y, width, height)
