from copy import copy

from pygame import Rect, draw

from lib.background import Background
from lib.camera import Camera
from lib.constants import ENEMY_WIDTH, SCALE, HEALTH_POINTS_ENEMY, RED, BLACK, HEALTH_POINTS, PLAYER_WIDTH, \
    TIME_BETWEEN_ATTACK_ENEMY, PLAYER_DAMAGE, ENEMY_DAMAGE
from lib.interface import GameScreen
from lib.player import Player
from lib.text_engine import TextSurface
from source.levels.levels import levels_dict


class GameManager:

    def __init__(self, sound_manager):
        self.sound_manager = sound_manager
        self.return_to_inital_states('1')

        sound_manager.play_music("back_music")

    def draw(self, surface):
        self.background.draw_game_window(surface)
        for enemy in self.enemies:
            if enemy.health_points > 0:
                enemy.draw(surface, self.camera.position)
                health_pos_x = enemy.position[0] - self.camera.position[0]
                health_pos_y = enemy.position[1] - self.camera.position[1] - 25
                health_width = ENEMY_WIDTH  # Ширина картинки врага
                health_height = 15 * SCALE  # Высота полоски здоровья
                health_ratio = enemy.health_points / HEALTH_POINTS_ENEMY  # Отношение текущего здоровья к максимальному
                health_bar_width = int(health_width * health_ratio)
                health_bar_rect = Rect(health_pos_x, health_pos_y, health_bar_width, health_height)
                draw.rect(surface, RED, health_bar_rect)  # Рисуем полоску здоровья
                draw.rect(surface, BLACK, health_bar_rect, 2)  # Рисуем обводку полоски здоровья

        if self.player.is_alive:
            self.player.draw(surface, self.camera.position)
            health_pos_x = self.player.position[0] - self.camera.position[0]
            health_pos_y = self.player.position[1] - self.camera.position[1] - 25
            health_width = PLAYER_WIDTH  # Ширина картинки игрока
            health_height = 15 * SCALE  # Высота полоски здоровья
            health_ratio = self.player.health_points / HEALTH_POINTS  # Отношение текущего здоровья к максимальному
            health_bar_width = int(health_width * health_ratio)
            health_bar_rect = Rect(health_pos_x, health_pos_y, health_bar_width, health_height)
            draw.rect(surface, RED, health_bar_rect)  # Рисуем полоску здоровья
            draw.rect(surface, BLACK, health_bar_rect, 2)  # Рисуем обводку полоски здоровья

        for platform in self.platforms:
            platform.draw(surface, self.camera.position)
        self.text_surface.draw(surface)

    def update(self, pressed_keys, upped_keys, mouse_pressed, mouse_upped):
        new_state = 'game' # Если ничего не произошло, то мы всё ещё в игре
        self.platforms_rects = [p.rect for p in self.platforms] # Конструктор списка

        self.player.move(pressed_keys, upped_keys, self.platforms_rects + self.enemies_rects, can_we_move=self.text_surface.is_text_open) # can_we_move - открыт ли текст
        self.player.player_attack(mouse_pressed)

        for enemy in self.enemies:
            if enemy.health_points > 0:
                enemy.enemy_attack(enemy.rect_for_fight, self.player.rect)
            if enemy.health_points >= 0:
                self.enemies_rects = [e.rect for e in self.enemies if e.health_points > 0] # Rect врагов исчезает после смерти

                if enemy.attack_timer > 0:
                    enemy.attack_timer -= 1
                    enemy.attack_frame_counter += 1

                    if enemy.attack_frame_counter >= TIME_BETWEEN_ATTACK_ENEMY:
                        enemy.attack_frame_counter = 0

                if self.player.is_attacking:
                    enemy.get_damage_from_player(self.player, damage=PLAYER_DAMAGE)
                enemy.move(self.platforms_rects, self.player, can_we_move=self.text_surface.is_text_open) # can_we_move - открыт ли текст
                if enemy.is_attacking:
                    self.player.get_damage_from_enemy(enemy, enemy.rect_for_fight, damage=ENEMY_DAMAGE)

        # for enemy in self.enemies:
        #     self.enemies_rects = [e.rect for e in self.enemies if e.is_alive]
        #     if self.player.is_attacking:
        #         enemy.get_damage(self.player.rect)
        #     enemy.move(self.platforms_rects, self.player, can_we_move=self.text_surface.is_text_open) # can_we_move - открыт ли текст

        # Тот самый вин\луз в геймманагере
        if self.platforms[len(self.platforms)-1].win(self.player.position): # Пердача последней, победной, платформе позиции игрока
            new_state = 'menu'
        if self.player.health_points == 0: # Если нет хп
            new_state = 'menu'

        for trigger in self.triggers: # если мы контактируем с триггером, то вызывается определённый текст. КОСТЫЛЬ
            if trigger.contact(self.player):
                self.text_surface.put_text(trigger.number)

        if self.text_surface.is_text_open:
            self.text_surface.continue_text(mouse_pressed)

        # Camera movement,
        self.camera.camera_movement(self.player)

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
        self.text_surface = TextSurface(levels_dict[f'{level}_text'])
        self.triggers = levels_dict[f'{level}_triggers']