from copy import copy

from lib.background import Background
from lib.camera import Camera
from lib.constants import BORDER_XL, BORDER_XR, BORDER_YH, BORDER_YD
from lib.interface import GameScreen
from lib.player import Player
from source.levels.levels import levels_dict


class GameManager:

    def __init__(self, sound_manager):
        self.sound_manager = sound_manager
        self.return_to_inital_states('1')

        sound_manager.play_music("back_music")

    def draw(self, surface):
        self.background.draw_game_window(surface)
        self.player.draw(surface, self.camera.position)
        self.interface.draw_health_points(surface, health_points_count=self.player.get_health_points)
        for enemy in self.enemies:
            enemy.draw(surface, self.camera.position)
        for platform in self.platforms:
            platform.draw(surface, self.camera.position)

    def update(self, pressed_keys, upped_keys, mouse_pressed, mouse_upped):
        new_state = 'game' # Если ничего не произошло, то мы всё ещё в игре
        self.platforms_rects = [p.rect for p in self.platforms] # Конструктор списка
        self.player.move(pressed_keys, upped_keys, self.platforms_rects + self.enemies_rects)
        self.player.attack(mouse_pressed)
        for enemy in self.enemies:
            self.enemies_rects = [e.rect for e in self.enemies if e.is_alive]
            if self.player.is_attacking:
                enemy.get_damage(self.player.rect)
            enemy.move(self.platforms_rects, self.player)
        # Тот самый вин\луз в геймманагере
        if self.platforms[len(self.platforms)-1].win(self.player.position): # Пердача последней, победной, платформе позиции игрока
            new_state = 'menu'
        if self.player.health_points == 0: # Если нет хп
            new_state = 'menu'
        # Camera movement
        if self.camera.position[0] <= self.player.position[0] - BORDER_XR:
            self.camera.position[0] = self.player.position[0] - BORDER_XR
        if self.camera.position[0] >= self.player.position[0] - BORDER_XL:
            self.camera.position[0] = self.player.position[0] - BORDER_XL

        if self.camera.position[1] <= self.player.position[1] - BORDER_YD:
            self.camera.position[1] = self.player.position[1] - BORDER_YD
        elif self.camera.position[1] >= self.player.position[1] - BORDER_YH:
            self.camera.position[1] = self.player.position[1] - BORDER_YH

        # if new_state == 'menu':
        #     self.return_to_inital_states('1')

        return new_state, -1

    def return_to_inital_states(self, level): # возвращает в начальное состояние
        self.player = Player()
        self.platforms = levels_dict[f'{level}_platforms']
        self.background = Background()
        self.interface = GameScreen()
        self.enemies = copy(levels_dict[f'{level}_enemies'])
        self.platforms_rects = []
        self.enemies_rects = []
        self.camera = Camera()