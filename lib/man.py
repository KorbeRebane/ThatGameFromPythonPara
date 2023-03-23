import pygame as pg

from lib.constants import SCREEN_HEIGHT, DELTA_T, G, SPEED_OF_JUMPING, SPEED_OF_WALKING, SPEED_OF_FALLING, SCREEN_WIDTH


class Man:
    def __init__(self, position, speed):
        self.position = list(position)
        self.speed = list(speed)
        self.jump_reserve = 1

        self.image = pg.image.load('source/images/black_man.png')

    def move(self, jump, walking_right, walking_left, falling):
        if jump:

            if self.jump_reserve >= 0:
                self.speed[1] = -SPEED_OF_JUMPING
                self.jump_reserve -= 1

        if walking_right and not walking_left:
            self.speed[0] = SPEED_OF_WALKING
        elif walking_left and not walking_right:
            self.speed[0] = -SPEED_OF_WALKING
        else:
            self.speed[0] = 0



        if falling:
            self.speed[1] = SPEED_OF_FALLING

        self.position[1] += self.speed[1] * DELTA_T # Пишем "1", т.к делаем это для y
        self.position[0] += self.speed[0] * DELTA_T
        if self.position[1] >= SCREEN_HEIGHT * 0.8:
            self.speed[1] = 0
            self.position[1] = SCREEN_HEIGHT * 0.8
        else:
            self.speed[1] += G * DELTA_T

        if self.position[0] >= SCREEN_WIDTH * 0.984:
            self.speed[0] = 0
            self.position[0] = SCREEN_WIDTH * 0.984

        elif self.position[0] <= 0:
            self.speed[0] = 0
            self.position[0] = 0
        else:
            self.speed[0] += G * DELTA_T


        if self.position[1] == SCREEN_HEIGHT * 0.8:
            self.jump_reserve = 1
