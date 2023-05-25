from copy import copy

from lib.constants import *
from lib.enemy import Enemy
from lib.platform import Platform, WinPlatform

# Уровень 0
test_level_platfroms_list = [Platform(FLOOR_POSITION, FLOOR_SIZE, FLOOR_FILENAME),
                          Platform(SECOND_PLATFORM_POSITION, SECOND_PLATFORM_SIZE, PLATFORM_FILENAME),
                          WinPlatform(WIN_POSITION, WIN_SIZE, PLATFORM_FILENAME)
                          ]
test_level_enemy_list = [Enemy(copy(FIRST_ENEMY_POSITION))]

# Уровень 1
first_level_platfroms_list = [Platform(FLOOR_POSITION, FLOOR_SIZE, FLOOR_FILENAME),
                              Platform(LEFT_WALL_POSITION, LEFT_WALL_SIZE, FLOOR_FILENAME),

                              Platform(FIRST_PLATFORM_POSITION, FIRST_PLATFORM_SIZE, PLATFORM_FILENAME),
                              Platform(SECOND_PLATFORM_POSITION, SECOND_PLATFORM_SIZE, PLATFORM_FILENAME),
                              Platform(THIRD_PLATFORM_POSITION, THIRD_PLATFORM_SIZE, PLATFORM_FILENAME),
                              Platform(FOURTH_PLATFORM_POSITION, FOURTH_PLATFORM_SIZE, PLATFORM_FILENAME),
                              Platform(FIVTH_PLATFORM_POSITION, FIVTH_PLATFORM_SIZE, PLATFORM_FILENAME),
                              Platform(SIX_PLATFORM_POSITION, SIX_PLATFORM_SIZE, PLATFORM_FILENAME),
                              Platform(SEVEN_PLATFORM_POSITION, SEVEN_PLATFORM_SIZE, PLATFORM_FILENAME),

                              WinPlatform(WIN_POSITION, WIN_SIZE, PLATFORM_FILENAME)
                              ]
first_level_enemy_list = []

# Все уровни
levels_dict = {'1_platforms': test_level_platfroms_list,
               '1_enemies': test_level_enemy_list,
               '2_platforms': first_level_platfroms_list,
               '2_enemies': first_level_enemy_list
               }