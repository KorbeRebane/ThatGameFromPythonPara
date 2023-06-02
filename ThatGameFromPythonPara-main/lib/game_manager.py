from lib.background import Background
from lib.constants import FLOOR_POSITION, SECOND_PLATFORM_POSITION, THIRD_PLATFORM_POSITION, FOURTH_PLATFORM_POSITION, \
    FIRST_ENEMY_POSITION, SECOND_ENEMY_POSITION, FLOOR_FILENAME, PLATFORM_FILENAME, CAMERA_X, CAMERA_Y, BORDER_XL, \
    BORDER_XR, BORDER_YH, BORDER_YD
from lib.enemy import Enemy
from lib.interface import GameScreen
from lib.player import Player
from lib.platform import Platform
from lib.camera import Camera

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
        self.camera = Camera()

        sound_manager.play_music("back_music")

    def draw(self, surface):
        self.background.draw_game_window(surface)
        self.player.draw(surface, self.camera.position)
        self.interface.draw_health_points(surface, health_points_count=self.player.get_player_health_points())
        for enemy in self.enemies:
            enemy.draw(surface, self.camera.position)
        for platform in self.platforms:
            platform.draw(surface, self.camera.position)

    def update(self, pressed_keys, upped_keys):
        for platform in self.platforms:
            self.platforms_rects.append(platform.rect)
        self.player.move(pressed_keys, upped_keys, self.platforms_rects)
        for enemy in self.enemies:
            enemy.get_damage(self.player.rect)
        new_state = self.player.game_states()
        # Camera movement
        if self.camera.position[0] <= self.player.position[0] - BORDER_XR:
            self.camera.position[0] = self.player.position[0] - BORDER_XR
        elif self.camera.position[0] >= self.player.position[0] - BORDER_XL:
            self.camera.position[0] = self.player.position[0] - BORDER_XL

        if self.camera.position[1] <= self.player.position[1] - BORDER_YD:
            self.camera.position[1] = self.player.position[1] - BORDER_YD
        elif self.camera.position[1] >= self.player.position[1] - BORDER_YH:
            self.camera.position[1] = self.player.position[1] - BORDER_YH

        return new_state