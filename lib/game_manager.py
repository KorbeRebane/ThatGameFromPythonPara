import pygame as pg

from lib.background import Background
from lib.camera import Camera
from lib.enemy import Enemy
from lib.interface import GameScreen
from lib.player import Player
from lib.platform import Platform


class GameManager:

    def __init__(self, sound_manager):
        self.sound_manager = sound_manager
        self.camera = Camera()
        self.player = Player()
        self.platform = Platform()
        self.background = Background()
        self.interface = GameScreen()
        self.enemy = Enemy()

        sound_manager.play_music("back_music")

    def draw(self, surface):
        self.background.draw_game_window(surface, self.camera.current_scroll)
        self.player.draw(surface)
        self.interface.draw_health_points(surface, health_points_count = self.player.get_player_health_points())
        # self.enemy.draw(surface)
        # self.platform.draw(surface)

    def update(self, pressed_keys, upped_keys):
        player_rect = self.player.rect

        player_position = self.player.get_player_position()
        contact = self.platform.contact_with_player(player_position)
        contact = [0, 0]
        self.player.move(pressed_keys, upped_keys, contact)
        self.enemy.get_damage(player_position)
        new_state = self.player.game_states()
        return new_state
