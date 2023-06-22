import pygame as pg
from lib.constants import BACK_MUSIC_1, BUM_1


class SoundManager:
    def __init__(self):
        pass
        # Загружаем фоновую музыку
        # back_music_1 = pg.mixer.Sound(BACK_MUSIC_1)
        # self.all_music = {"back_music": back_music_1}
        # Загружаем звуки
        # explosion_1 = pg.mixer.Sound(BUM_1)
        # self.all_sounds = {"explosion": explosion_1}

    def play_sound(self, name):
        pass
        # if name in self.all_sounds:
          #  self.all_sounds[name].play()
        # else:
           # pass    # В будущем надо выдавать ошибку

    def play_music(self, name):
        pass
        # if name in self.all_music:
            # self.all_music[name].play()
        # else:
            # pass    # В будущем надо выдавать ошибку
