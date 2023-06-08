import pygame as pg

from lib.constants import SCREEN_WIDTH, SCREEN_HEIGHT, FPS
from lib.game_manager import GameManager
from lib.sound import SoundManager
from lib.utilities import get_all_pressed_keys
from menu.menu import MenuManager, LevelListManager

pg.init()

screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pg.time.Clock()
sound_manager = SoundManager()
game_manager = GameManager(sound_manager=sound_manager)
menu_manager = MenuManager()
level_manager = LevelListManager()

state = "menu"
parameters = -1
managers = {
    "menu": menu_manager,
    "game": game_manager,
    "level_list": level_manager
}

while True:
    keys, keys_up, mouse, mouse_up = get_all_pressed_keys()

    manager = managers[state]
    if parameters != -1:
        manager.return_to_inital_states(parameters)
        level_manager.start_level = -1
    state, parameters = manager.update(pressed_keys=keys, upped_keys=keys_up, mouse_pressed=mouse, mouse_upped=mouse_up)
    manager.draw(surface=screen)

    pg.display.update()
    clock.tick(FPS)

















