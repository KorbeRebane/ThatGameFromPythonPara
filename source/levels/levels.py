from copy import copy

from lib.constants import *
from lib.enemy import Enemy
from lib.platform import Platform, WinPlatform, Trigger

# Уровень 0
test_level_platfroms_list = [Platform(FLOOR_POSITION, FLOOR_SIZE, FLOOR_FILENAME),
                             Platform(FIRST_ZERO_LEVEL_PLATFORM_POSITION, FIRST_ZERO_LEVEL_PLATFORM_SIZE,
                                      PLATFORM_FILENAME),
                             Platform(SECOND_ZERO_LEVEL_PLATFORM_POSITION, SECOND_ZERO_LEVEL_PLATFORM_SIZE,
                                      PLATFORM_FILENAME),
                             Platform(THIRD_ZERO_LEVEL_PLATFORM_POSITION, THIRD_ZERO_LEVEL_PLATFORM_SIZE,
                                      PLATFORM_FILENAME),
                             Platform(FOURTH_ZERO_LEVEL_PLATFORM_POSITION, FOURTH_ZERO_LEVEL_PLATFORM_SIZE,
                                      PLATFORM_FILENAME),
                             WinPlatform(WIN_0_POSITION, WIN_0_SIZE, PLATFORM_FILENAME)
                             ]
test_level_enemy_list = [Enemy(copy(FIRST_ENEMY_POSITION))]
test_level_text_dict = {}
test_level_trigger_list = []
# test_level_invisible_platform_enemy_list = []

# Уровень 1
first_level_platfroms_list = [Platform(FLOOR_POSITION, FLOOR_SIZE, FLOOR_FILENAME),
                              Platform(LEFT_WALL_POSITION, LEFT_WALL_SIZE, FLOOR_FILENAME),
                              Platform(FLOOR_sp_POSITION, FLOOR_sp_SIZE, FLOOR_FILENAME),

                              Platform(FIRST_FIRST_LEVEL_PLATFORM_POSITION, FIRST_FIRST_LEVEL_PLATFORM_SIZE,
                                       PLATFORM_FILENAME),
                              Platform(SECOND_FIRST_LEVEL_PLATFORM_POSITION, SECOND_FIRST_LEVEL_PLATFORM_SIZE,
                                       PLATFORM_FILENAME),
                              Platform(THIRD_FIRST_LEVEL_PLATFORM_POSITION, THIRD_FIRST_LEVEL_PLATFORM_SIZE,
                                       PLATFORM_FILENAME),
                              Platform(FOURTH_FIRST_LEVEL_PLATFORM_POSITION, FOURTH_FIRST_LEVEL_PLATFORM_SIZE,
                                       PLATFORM_FILENAME),
                              Platform(FIFTH_FIRST_LEVEL_PLATFORM_POSITION, FIFTH_FIRST_LEVEL_PLATFORM_SIZE,
                                       PLATFORM_FILENAME),
                              Platform(SIX_FIRST_LEVEL_PLATFORM_POSITION, SIX_FIRST_LEVEL_PLATFORM_SIZE,
                                       PLATFORM_FILENAME),
                              Platform(SEVEN_FIRST_LEVEL_PLATFORM_POSITION, SEVEN_FIRST_LEVEL_PLATFORM_SIZE,
                                       PLATFORM_FILENAME),

                              WinPlatform(WIN_1_POSITION, WIN_1_SIZE, PLATFORM_FILENAME)
                              ]
first_level_enemy_list = []
first_level_text_dict = {0: 'Автор: Первая строчка', 1: 'Автор: Хм-м, что это'}
first_level_trigger_list = [Trigger([START_POSITION_X, START_POSITION_Y], (100, 100), PLATFORM_FILENAME, 0),
                            Trigger([5000, START_POSITION_Y], (100, 100), PLATFORM_FILENAME, 1),
                            Trigger([324, 4343], (2, 3), PLATFORM_FILENAME)
                            ]
# first_level_invisible_platform_enemy_list = []

# Уровень 2
second_level_platfroms_list = [Platform(FLOOR_POSITION, FLOOR_SIZE, FLOOR_FILENAME),
                               Platform(LEFT_WALL_POSITION, LEFT_WALL_SIZE, FLOOR_FILENAME),
                               Platform(FLOOR_sp_POSITION, FLOOR_sp_SIZE, FLOOR_FILENAME),

                               Platform(FIRST_SECOND_LEVEL_PLATFORM_POSITION, FIRST_SECOND_LEVEL_PLATFORM_SIZE,
                                        PLATFORM_FILENAME),
                               Platform(SECOND_SECOND_LEVEL_PLATFORM_POSITION, SECOND_SECOND_LEVEL_PLATFORM_SIZE,
                                        PLATFORM_FILENAME),
                               Platform(THIRD_SECOND_LEVEL_PLATFORM_POSITION, THIRD_SECOND_LEVEL_PLATFORM_SIZE,
                                        PLATFORM_FILENAME),
                               Platform(FOURTH_SECOND_LEVEL_PLATFORM_POSITION, FOURTH_SECOND_LEVEL_PLATFORM_SIZE,
                                        PLATFORM_FILENAME),
                               Platform(FIFTH_SECOND_LEVEL_PLATFORM_POSITION, FIFTH_SECOND_LEVEL_PLATFORM_SIZE,
                                        PLATFORM_FILENAME),
                               Platform(SIX_SECOND_LEVEL_PLATFORM_POSITION, SIX_SECOND_LEVEL_PLATFORM_SIZE,
                                        PLATFORM_FILENAME),
                               Platform(SEVEN_SECOND_LEVEL_PLATFORM_POSITION, SEVEN_SECOND_LEVEL_PLATFORM_SIZE,
                                        PLATFORM_FILENAME),
                               Platform(EIGHT_SECOND_LEVEL_PLATFORM_POSITION, EIGHT_SECOND_LEVEL_PLATFORM_SIZE,
                                        PLATFORM_FILENAME),
                               Platform(NINE_SECOND_LEVEL_PLATFORM_POSITION, NINE_SECOND_LEVEL_PLATFORM_SIZE,
                                        PLATFORM_FILENAME),
                               Platform(TEN_SECOND_LEVEL_PLATFORM_POSITION, TEN_SECOND_LEVEL_PLATFORM_SIZE,
                                        PLATFORM_FILENAME),
                               Platform(ELEVEN_SECOND_LEVEL_PLATFORM_POSITION, ELEVEN_SECOND_LEVEL_PLATFORM_SIZE,
                                        PLATFORM_FILENAME),
                               Platform(TWELVE_SECOND_LEVEL_PLATFORM_POSITION, TWELVE_SECOND_LEVEL_PLATFORM_SIZE,
                                        PLATFORM_FILENAME),
                               Platform(THIRTEEN_SECOND_LEVEL_PLATFORM_POSITION, THIRTEEN_SECOND_LEVEL_PLATFORM_SIZE,
                                        PLATFORM_FILENAME),
                               Platform(FOURTEEN_SECOND_LEVEL_PLATFORM_POSITION, FOURTEEN_SECOND_LEVEL_PLATFORM_SIZE,
                                        PLATFORM_FILENAME),
                               Platform(FIFTEEN_SECOND_LEVEL_PLATFORM_POSITION, FIFTEEN_SECOND_LEVEL_PLATFORM_SIZE,
                                        PLATFORM_FILENAME),
                               Platform(SIXTEEN_SECOND_LEVEL_PLATFORM_POSITION, SIXTEEN_SECOND_LEVEL_PLATFORM_SIZE,
                                        PLATFORM_FILENAME),
                               Platform(SEVENTEEN_SECOND_LEVEL_PLATFORM_POSITION, SEVENTEEN_SECOND_LEVEL_PLATFORM_SIZE,
                                        PLATFORM_FILENAME),
                               Platform(EIGHTEEN_SECOND_LEVEL_PLATFORM_POSITION, EIGHTEEN_SECOND_LEVEL_PLATFORM_SIZE,
                                        PLATFORM_FILENAME),
                               Platform(NINETEEN_SECOND_LEVEL_PLATFORM_POSITION, NINETEEN_SECOND_LEVEL_PLATFORM_SIZE,
                                        PLATFORM_FILENAME),

                               WinPlatform(WIN_2_POSITION, WIN_2_SIZE, PLATFORM_FILENAME)
                               ]
second_level_enemy_list = [Enemy(copy(FIRST_SECOND_LEVEL_ENEMY_POSITION)),
                           Enemy(copy(SECOND_SECOND_LEVEL_ENEMY_POSITION)),
                           Enemy(copy(THIRD_SECOND_LEVEL_ENEMY_POSITION)),
                           Enemy(copy(FOURTH_SECOND_LEVEL_ENEMY_POSITION)),
                           Enemy(copy(FIFTH_SECOND_LEVEL_ENEMY_POSITION)),
                           Enemy(copy(SIXTH_SECOND_LEVEL_ENEMY_POSITION)),
                           Enemy(copy(SEVENTH_SECOND_LEVEL_ENEMY_POSITION)),
                           Enemy(copy(EIGHTH_SECOND_LEVEL_ENEMY_POSITION)),
                           Enemy(copy(NINTH_SECOND_LEVEL_ENEMY_POSITION)),
                           Enemy(copy(TENTH_SECOND_LEVEL_ENEMY_POSITION))]
second_level_text_dict = {}
second_level_trigger_list = [Trigger(FIRST_SECOND_LEVEL_INVISIBLE_PLATFORM_ENEMY_POSITION,
                                     FIRST_SECOND_LEVEL_INVISIBLE_PLATFORM_ENEMY_SIZE,
                                     PLATFORM_FILENAME),
                             Trigger(SECOND_SECOND_LEVEL_INVISIBLE_PLATFORM_ENEMY_POSITION,
                                     SECOND_SECOND_LEVEL_INVISIBLE_PLATFORM_ENEMY_SIZE,
                                     PLATFORM_FILENAME)]

# second_level_invisible_platform_enemy_list = [Platform(FIRST_SECOND_LEVEL_INVISIBLE_PLATFORM_ENEMY_POSITION,
#                                                        FIRST_SECOND_LEVEL_INVISIBLE_PLATFORM_ENEMY_SIZE,
#                                                        PLATFORM_FILENAME),
#                                               Platform(SECOND_SECOND_LEVEL_INVISIBLE_PLATFORM_ENEMY_POSITION,
#                                                        SECOND_SECOND_LEVEL_INVISIBLE_PLATFORM_ENEMY_SIZE,
#                                                        PLATFORM_FILENAME), ]

# Уровень 3
third_level_platfroms_list = [Platform(FLOOR_POSITION, FLOOR_SIZE, FLOOR_FILENAME),
                              Platform(LEFT_WALL_POSITION, LEFT_WALL_SIZE, FLOOR_FILENAME),
                              Platform(FLOOR_sp_POSITION, FLOOR_sp_SIZE, FLOOR_FILENAME),

                              Platform(FIRST_THIRD_LEVEL_PLATFORM_POSITION, FIRST_THIRD_LEVEL_PLATFORM_SIZE,
                                       PLATFORM_FILENAME),
                              Platform(SECOND_THIRD_LEVEL_PLATFORM_POSITION, SECOND_THIRD_LEVEL_PLATFORM_SIZE,
                                       PLATFORM_FILENAME),
                              Platform(THIRD_THIRD_LEVEL_PLATFORM_POSITION, THIRD_THIRD_LEVEL_PLATFORM_SIZE,
                                       PLATFORM_FILENAME),
                              Platform(FOURTH_THIRD_LEVEL_PLATFORM_POSITION, FOURTH_THIRD_LEVEL_PLATFORM_SIZE,
                                       PLATFORM_FILENAME),
                              Platform(FIFTH_THIRD_LEVEL_PLATFORM_POSITION, FIFTH_THIRD_LEVEL_PLATFORM_SIZE,
                                       PLATFORM_FILENAME),
                              Platform(SIX_THIRD_LEVEL_PLATFORM_POSITION, SIX_THIRD_LEVEL_PLATFORM_SIZE,
                                       PLATFORM_FILENAME),
                              Platform(SEVEN_THIRD_LEVEL_PLATFORM_POSITION, SEVEN_THIRD_LEVEL_PLATFORM_SIZE,
                                       PLATFORM_FILENAME),

                              WinPlatform(WIN_3_POSITION, WIN_3_SIZE, PLATFORM_FILENAME)
                              ]
third_level_enemy_list = []
third_level_text_dict = {}
third_level_trigger_list = []
# third_level_invisible_platform_enemy_list = []

# Все уровни
levels_dict = {'1_platforms': test_level_platfroms_list,
               '1_enemies': test_level_enemy_list,
               '1_text': test_level_text_dict,
               '1_triggers': test_level_trigger_list,
               # '1_invisible_platforms_enemy': test_level_invisible_platform_enemy_list,
               '2_platforms': first_level_platfroms_list,
               '2_enemies': first_level_enemy_list,
               '2_text': first_level_text_dict,
               '2_triggers': first_level_trigger_list,
               # '2_invisible_platforms_enemy': test_level_invisible_platform_enemy_list,
               '3_platforms': second_level_platfroms_list,
               '3_enemies': second_level_enemy_list,
               '3_text': second_level_text_dict,
               '3_triggers': second_level_trigger_list,
               # '3_invisible_platforms_enemy': test_level_invisible_platform_enemy_list,
               '4_platforms': third_level_platfroms_list,
               '4_enemies': third_level_enemy_list,
               '4_text': third_level_text_dict,
               '4_triggers': third_level_trigger_list,
               # '4_invisible_platforms_enemy': test_level_invisible_platform_enemy_list
               }
