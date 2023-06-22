import pygame as pg
from pygame import Rect
# from enemy import Enemy

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


class Trigger(Platform):
    def __init__(self, position, size, texture, number=None):
        super().__init__(position, size, texture)
        self.is_activated = False
        self.number = number

    def contact(self, player):
        if pg.Rect.colliderect(self.rect, player.rect) and not self.is_activated and self.number is not None: # Если мы встаём на триггер то он активируется
            self.is_activated = True
            return True

    def contact_enemy(self, enemy):
        if pg.Rect.colliderect(self.rect, enemy.rect):
            enemy.walking_left, enemy.walking_right = enemy.walking_right, enemy.walking_left

    @property
    def ret_number(self):
        return self.number


class WinPlatform(Platform):
    def __init__(self, position, size, texture):
        super().__init__(position, size, texture)

    def win(self, player_position):
        if player_position[0] >= self.position[0]: # Если игрок дальше иксовой позиции финиша, то сработает
            return True

