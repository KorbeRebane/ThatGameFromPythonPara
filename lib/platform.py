import pygame as pg
from pygame import Rect

class Platform:
    def __init__(self, position, size, texture):
        self.image = pg.image.load(texture)
        self.size = size
        self.image = pg.transform.scale(self.image, self.size)

        self.position = position

    def draw(self, surface, camera_position):
        new_x = self.position[0] - camera_position[0]
        new_y = self.position[1] - camera_position[1]
        surface.blit(self.image, [new_x, new_y])

    @property
    def rect(self):
        x = self.position[0]
        y = self.position[1]
        width = self.image.get_width()
        height = self.image.get_height()
        return Rect(x, y, width, height)

class WinPlatform(Platform):
    def __int__(self, position, size, texture):
        super.__init__(position, size, texture)

    def win(self, player_position):
        if player_position[0] >= self.position[0]: # Если игрок дальше иксовой позиции финиша, то сработает
            return True