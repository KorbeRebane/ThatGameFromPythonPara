import pygame as pg

from lib.constants import SCREEN_WIDTH, SCREEN_HEIGHT, FPS
from lib.game_manager import GameManager
from lib.sound import SoundManager
from lib.utilities import get_all_pressed_keys
from menu.menu import MenuManager

pg.init()

screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pg.time.Clock()
sound_manager = SoundManager()
game_manager = GameManager(sound_manager=sound_manager)
menu_manager = MenuManager()

state = "menu"
managers = {
    "menu": menu_manager,
    "game": game_manager
}

while True:
    keys, keys_up = get_all_pressed_keys()

    manager = managers[state]
    state = manager.update(pressed_keys=keys, upped_keys=keys_up)
    manager.draw(surface=screen)

    pg.display.update()
    clock.tick(FPS)

















