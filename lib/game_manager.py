from lib.background import Background
from lib.constants import FLOOR_POSITION, SECOND_PLATFORM_POSITION, THIRD_PLATFORM_POSITION, FOURTH_PLATFORM_POSITION, \
    FIRST_ENEMY_POSITION, SECOND_ENEMY_POSITION, FLOOR_FILENAME, PLATFORM_FILENAME
from lib.enemy import Enemy
from lib.interface import GameScreen
from lib.player import Player
from lib.platform import Platform


class GameManager:

    def __init__(self, sound_manager):
        self.sound_manager = sound_manager
        self.player = Player()
        self.platforms = [Platform(FLOOR_POSITION, FLOOR_FILENAME), Platform(SECOND_PLATFORM_POSITION, PLATFORM_FILENAME),
                          Platform(THIRD_PLATFORM_POSITION, PLATFORM_FILENAME), Platform(FOURTH_PLATFORM_POSITION, PLATFORM_FILENAME)]
        self.background = Background()
        self.interface = GameScreen()
        self.enemies = [Enemy(FIRST_ENEMY_POSITION)]
        self.platforms_rects = []

        sound_manager.play_music("back_music")

    def draw(self, surface):
        self.background.draw_game_window(surface)
        self.player.draw(surface)
        self.interface.draw_health_points(surface, health_points_count=self.player.get_player_health_points())
        for enemy in self.enemies:
            enemy.draw(surface)
        for platform in self.platforms:
            platform.draw(surface)

    def update(self, pressed_keys, upped_keys):
        for platform in self.platforms:
            self.platforms_rects.append(platform.rect)
        self.player.move(pressed_keys, upped_keys, self.platforms_rects)
        for enemy in self.enemies:
            enemy.get_damage(self.player.rect)
        new_state = self.player.game_states()
        return new_state
