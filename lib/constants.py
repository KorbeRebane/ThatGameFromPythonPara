# Масштаб
SCALE = 1

# Цвета
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)

# Параметры экрана и пола
SCREEN_WIDTH = 1200 * SCALE
SCREEN_HEIGHT = 800 * SCALE
FLOOR_HEIGHT = SCREEN_HEIGHT - 110 * SCALE
HEALTH_POINT_POSITION_X = 45 * SCALE
HEALTH_POINT_POSITION_Y = 45 * SCALE
HEALTH_POINT_SIZE = 25 * SCALE

# Player parameters
PLAYER_HEIGHT = 142 * SCALE
PLAYER_WIDTH = 90 * SCALE
VIEW_RADIUS = 200
START_POSITION_X = 150
START_POSITION_Y = FLOOR_HEIGHT - PLAYER_HEIGHT
PLAYER_SPEED = 500 * SCALE
GENERAL_MOVEMENT_SPEED = PLAYER_SPEED
JUMP_SPEED = 650 * SCALE
PLAYER_SPEED_LIST = [0, 0]
HEALTH_POINTS = 7
TIME_OF_ATTACK = 15
PLAYER_DAMAGE = 1
FALLING_SPEED = 1500

# Enemy parameters
ENEMY_HEIGHT = 150 * SCALE
ENEMY_WIDTH = 90 * SCALE
ENEMY_SPEED = 10 * SCALE
HEALTH_POINTS_ENEMY = 3
ENEMY_DAMAGE = 1
RADIUS_OF_ATTACK_BACK = 50
RADIUS_OF_ATTACK_FORWARD = 100
TIME_BETWEEN_ATTACK_ENEMY = 50
STANDART_SIZE = [90 * SCALE, 150 * SCALE]

# Platform parameters
PLATFORM_HEIGHT = 90 * SCALE
PLATFORM_WIDTH = 350 * SCALE
PLATFORM_POSITION_Y = FLOOR_HEIGHT - PLATFORM_HEIGHT
FLOOR_DEPTH = 110 * SCALE
DEFAULT_PLATFORM_SIZE = [PLATFORM_WIDTH, PLATFORM_HEIGHT]

# First level parameters
# Позиции пола и стен всегда первые в списке
FLOOR_POSITION = [-500, FLOOR_HEIGHT]
FLOOR_SIZE = [16*SCREEN_WIDTH, 2.5*FLOOR_DEPTH]
LEFT_WALL_SIZE = [1000, SCREEN_HEIGHT * 2]
LEFT_WALL_POSITION = [FLOOR_POSITION[0] - LEFT_WALL_SIZE[0], PLATFORM_POSITION_Y + PLATFORM_HEIGHT - LEFT_WALL_SIZE[1]]
FLOOR_sp_POSITION = [LEFT_WALL_POSITION[0], FLOOR_HEIGHT]
FLOOR_sp_SIZE = [LEFT_WALL_SIZE[0], 2.5*FLOOR_DEPTH]

# Позиция выигрывшыной платформы
WIN_0_POSITION = [5150 * 0.4, PLATFORM_POSITION_Y]
WIN_1_POSITION = [5150 * 1, PLATFORM_POSITION_Y]
WIN_2_POSITION = [11300 + 1.7 * PLATFORM_WIDTH, -13 * PLATFORM_HEIGHT]
WIN_3_POSITION = [5150 * 2, -3540 * SCALE + PLAYER_HEIGHT - PLATFORM_HEIGHT]

WIN_0_SIZE = [PLATFORM_WIDTH*0.3, PLATFORM_HEIGHT]
WIN_1_SIZE = [PLATFORM_WIDTH*0.3, PLATFORM_HEIGHT]
WIN_2_SIZE = [PLATFORM_WIDTH*0.3, PLATFORM_HEIGHT]
WIN_3_SIZE = [PLATFORM_WIDTH*0.3, PLATFORM_HEIGHT]

# Позиции платформ на уровне
FIRST_ZERO_LEVEL_PLATFORM_POSITION = [900, PLATFORM_POSITION_Y]
SECOND_ZERO_LEVEL_PLATFORM_POSITION = [100 + PLATFORM_WIDTH, PLATFORM_POSITION_Y - 4 * PLATFORM_HEIGHT]
THIRD_ZERO_LEVEL_PLATFORM_POSITION = [-100, PLATFORM_POSITION_Y - PLATFORM_HEIGHT]
FOURTH_ZERO_LEVEL_PLATFORM_POSITION = [100, PLATFORM_POSITION_Y - 4 * PLATFORM_HEIGHT]

FIRST_FIRST_LEVEL_PLATFORM_POSITION = [300, PLATFORM_POSITION_Y]
SECOND_FIRST_LEVEL_PLATFORM_POSITION = [900, PLATFORM_POSITION_Y]
THIRD_FIRST_LEVEL_PLATFORM_POSITION = [900, PLATFORM_POSITION_Y - PLATFORM_HEIGHT]
FOURTH_FIRST_LEVEL_PLATFORM_POSITION = [2100, PLATFORM_POSITION_Y- PLATFORM_HEIGHT]
FIFTH_FIRST_LEVEL_PLATFORM_POSITION = [3000, PLATFORM_POSITION_Y - PLATFORM_HEIGHT]
SIX_FIRST_LEVEL_PLATFORM_POSITION = [4050, PLATFORM_POSITION_Y]
SEVEN_FIRST_LEVEL_PLATFORM_POSITION = [4800, PLATFORM_POSITION_Y - PLATFORM_HEIGHT*5]

FIRST_SECOND_LEVEL_PLATFORM_POSITION = [8075, PLATFORM_POSITION_Y - PLATFORM_HEIGHT * 9]
SECOND_SECOND_LEVEL_PLATFORM_POSITION = [8600, PLATFORM_POSITION_Y - PLATFORM_HEIGHT * 6 + 50]
THIRD_SECOND_LEVEL_PLATFORM_POSITION = [400, PLATFORM_POSITION_Y]
FOURTH_SECOND_LEVEL_PLATFORM_POSITION = [400 + (PLATFORM_WIDTH * 0.5), PLATFORM_POSITION_Y - PLATFORM_HEIGHT]
FIFTH_SECOND_LEVEL_PLATFORM_POSITION = [1800, PLATFORM_POSITION_Y - PLATFORM_HEIGHT]
SIX_SECOND_LEVEL_PLATFORM_POSITION = [4050, PLATFORM_POSITION_Y]
SEVEN_SECOND_LEVEL_PLATFORM_POSITION = [4800, PLATFORM_POSITION_Y - PLATFORM_HEIGHT*5]
EIGHT_SECOND_LEVEL_PLATFORM_POSITION = [4200, PLATFORM_POSITION_Y - PLATFORM_HEIGHT*5]
NINE_SECOND_LEVEL_PLATFORM_POSITION = [3600, PLATFORM_POSITION_Y - PLATFORM_HEIGHT*5]
TEN_SECOND_LEVEL_PLATFORM_POSITION = [3000, PLATFORM_POSITION_Y - PLATFORM_HEIGHT*5]
ELEVEN_SECOND_LEVEL_PLATFORM_POSITION = [2350, PLATFORM_POSITION_Y - PLATFORM_HEIGHT*5]
TWELVE_SECOND_LEVEL_PLATFORM_POSITION = [1500, PLATFORM_POSITION_Y - PLATFORM_HEIGHT - 250]
THIRTEEN_SECOND_LEVEL_PLATFORM_POSITION = [5000, PLATFORM_POSITION_Y - 0.25*PLATFORM_HEIGHT]
FOURTEEN_SECOND_LEVEL_PLATFORM_POSITION = [5300, PLATFORM_POSITION_Y - PLATFORM_HEIGHT * 3]
FIFTEEN_SECOND_LEVEL_PLATFORM_POSITION = [5600, PLATFORM_POSITION_Y - PLATFORM_HEIGHT * 6]
SIXTEEN_SECOND_LEVEL_PLATFORM_POSITION = [5900, PLATFORM_POSITION_Y - PLATFORM_HEIGHT * 9]
SEVENTEEN_SECOND_LEVEL_PLATFORM_POSITION = [6200, PLATFORM_POSITION_Y - PLATFORM_HEIGHT * 12]
EIGHTEEN_SECOND_LEVEL_PLATFORM_POSITION = [6800, PLATFORM_POSITION_Y - PLATFORM_HEIGHT * 8]
NINETEEN_SECOND_LEVEL_PLATFORM_POSITION = [7600, PLATFORM_POSITION_Y - PLATFORM_HEIGHT * 10]
TWENTY_SECOND_LEVEL_PLATFORM_POSITION = [9200, PLATFORM_POSITION_Y - PLATFORM_HEIGHT * 8]
TWENTYONE_SECOND_LEVEL_PLATFORM_POSITION = [8000, PLATFORM_POSITION_Y - PLATFORM_HEIGHT * 4]
TWENTYTWO_SECOND_LEVEL_PLATFORM_POSITION = [8600, PLATFORM_POSITION_Y - PLATFORM_HEIGHT * 2.5]
TWENTYTHREE_SECOND_LEVEL_PLATFORM_POSITION = [9200 + 3.98 * PLATFORM_WIDTH, PLATFORM_POSITION_Y - PLATFORM_HEIGHT * 13]
TWENTYFOUR_SECOND_LEVEL_PLATFORM_POSITION = [11000, PLATFORM_POSITION_Y - PLATFORM_HEIGHT * 2.5]
TWENTYFIVE_SECOND_LEVEL_PLATFORM_POSITION = [11500, -12 * PLATFORM_HEIGHT]
TWENTYSIX_SECOND_LEVEL_PLATFORM_POSITION = [11250, PLATFORM_POSITION_Y - PLATFORM_HEIGHT * 3 - ENEMY_HEIGHT]
TWENTYSEVEN_SECOND_LEVEL_PLATFORM_POSITION = [11250, PLATFORM_POSITION_Y - PLATFORM_HEIGHT * 4 - ENEMY_HEIGHT * 2]
TWENTYEIGHT_SECOND_LEVEL_PLATFORM_POSITION = [11250, PLATFORM_POSITION_Y - PLATFORM_HEIGHT * 5 - ENEMY_HEIGHT * 3]
TWENTYNINE_SECOND_LEVEL_PLATFORM_POSITION = [11250, PLATFORM_POSITION_Y - PLATFORM_HEIGHT * 6 - ENEMY_HEIGHT * 4]
THIRTY_SECOND_LEVEL_PLATFORM_POSITION = [11250, PLATFORM_POSITION_Y - PLATFORM_HEIGHT * 7 - ENEMY_HEIGHT * 5]
THIRTYONE_SECOND_LEVEL_PLATFORM_POSITION = [11250, PLATFORM_POSITION_Y - PLATFORM_HEIGHT * 8 - ENEMY_HEIGHT * 6]

FIRST_SECOND_LEVEL_INVISIBLE_PLATFORM_ENEMY_POSITION = [3000, PLATFORM_POSITION_Y - PLATFORM_HEIGHT * 8]
SECOND_SECOND_LEVEL_INVISIBLE_PLATFORM_ENEMY_POSITION = [3000 + PLATFORM_WIDTH*1, PLATFORM_POSITION_Y - PLATFORM_HEIGHT * 10]
THIRD_SECOND_LEVEL_INVISIBLE_PLATFORM_ENEMY_POSITION = [9200, PLATFORM_POSITION_Y - PLATFORM_HEIGHT * 10]
FOURTH_SECOND_LEVEL_INVISIBLE_PLATFORM_ENEMY_POSITION = [9200 + 4 * PLATFORM_WIDTH, PLATFORM_POSITION_Y - PLATFORM_HEIGHT * 10]

FIRST_SECOND_LEVEL_TRIGGER_POSITION = [FIFTH_SECOND_LEVEL_PLATFORM_POSITION[0] + 0, FIFTH_SECOND_LEVEL_PLATFORM_POSITION[1] - 0.1*PLATFORM_HEIGHT]
SECOND_SECOND_LEVEL_TRIGGER_POSITION = [SEVENTEEN_SECOND_LEVEL_PLATFORM_POSITION[0] + 100, SEVENTEEN_SECOND_LEVEL_PLATFORM_POSITION[1] - 0.1*PLATFORM_HEIGHT]
THIRD_SECOND_LEVEL_TRIGGER_POSITION = [TWENTYFIVE_SECOND_LEVEL_PLATFORM_POSITION[0] + 50, TWENTYFIVE_SECOND_LEVEL_PLATFORM_POSITION[1] - 0.2*PLATFORM_HEIGHT]

FIRST_THIRD_LEVEL_PLATFORM_POSITION = [1000, PLATFORM_POSITION_Y - 4.6 * PLAYER_HEIGHT]
SECOND_THIRD_LEVEL_PLATFORM_POSITION = [-500, PLATFORM_POSITION_Y - 4.6 * PLAYER_HEIGHT]
THIRD_THIRD_LEVEL_PLATFORM_POSITION = [1000 - 0.5 * PLATFORM_WIDTH, PLATFORM_POSITION_Y - 0.7 * PLAYER_HEIGHT]
FOURTH_THIRD_LEVEL_PLATFORM_POSITION = [1000 - 0.5 * PLATFORM_WIDTH, PLATFORM_POSITION_Y - 2.0 * PLAYER_HEIGHT]
FIFTH_THIRD_LEVEL_PLATFORM_POSITION = [1000 - 0.5 * PLATFORM_WIDTH, PLATFORM_POSITION_Y - 3.3 * PLAYER_HEIGHT]
SIX_THIRD_LEVEL_PLATFORM_POSITION = [4000, PLATFORM_POSITION_Y - 4.6 * PLAYER_HEIGHT - 22 * PLAYER_HEIGHT]
SEVEN_THIRD_LEVEL_PLATFORM_POSITION = [4000 - 0.5 * PLATFORM_WIDTH, PLATFORM_POSITION_Y - 5.9 * PLAYER_HEIGHT]
EIGHT_THIRD_LEVEL_PLATFORM_POSITION = [4000 - 1 * PLATFORM_WIDTH, PLATFORM_POSITION_Y - 8 * PLAYER_HEIGHT]
NINE_THIRD_LEVEL_PLATFORM_POSITION = [4000 - 1.5 * PLATFORM_WIDTH, PLATFORM_POSITION_Y - 10.1 * PLAYER_HEIGHT]
TEN_THIRD_LEVEL_PLATFORM_POSITION = [4000 - 2 * PLATFORM_WIDTH, PLATFORM_POSITION_Y - 12.2 * PLAYER_HEIGHT]
ELEVEN_THIRD_LEVEL_PLATFORM_POSITION = [4000 - 2.5 * PLATFORM_WIDTH, PLATFORM_POSITION_Y - 14.3 * PLAYER_HEIGHT]
TWELVE_THIRD_LEVEL_PLATFORM_POSITION = [2000, PLATFORM_POSITION_Y - 6 * PLAYER_HEIGHT]
THIRTEEN_THIRD_LEVEL_PLATFORM_POSITION = [4000 - 3 * PLATFORM_WIDTH, PLATFORM_POSITION_Y - 16.4 * PLAYER_HEIGHT]
FOURTEEN_THIRD_LEVEL_PLATFORM_POSITION = [4000 - 4 * PLATFORM_WIDTH, PLATFORM_POSITION_Y - 18.5 * PLAYER_HEIGHT]
FIFTEEN_THIRD_LEVEL_PLATFORM_POSITION = [4000 - 5 * PLATFORM_WIDTH, PLATFORM_POSITION_Y - 20.6 * PLAYER_HEIGHT]
SIXTEEN_THIRD_LEVEL_PLATFORM_POSITION = [4000 - 5 * PLATFORM_WIDTH, PLATFORM_POSITION_Y - 22.7 * PLAYER_HEIGHT]
SEVENTEEN_THIRD_LEVEL_PLATFORM_POSITION = [4000 - 2 * PLATFORM_WIDTH, PLATFORM_POSITION_Y - 22.7 * PLAYER_HEIGHT]
EIGHTEEN_THIRD_LEVEL_PLATFORM_POSITION = [4000 - 1 * PLATFORM_WIDTH, PLATFORM_POSITION_Y - 25 * PLAYER_HEIGHT]
NINETEEN_THIRD_LEVEL_PLATFORM_POSITION = [4000 + 2 * PLATFORM_WIDTH, PLATFORM_POSITION_Y - 28 * PLAYER_HEIGHT]
TWENTY_THIRD_LEVEL_PLATFORM_POSITION = [4000 + 2.1 * PLATFORM_WIDTH, PLATFORM_POSITION_Y - 29.5 * PLAYER_HEIGHT]
TWENTYONE_THIRD_LEVEL_PLATFORM_POSITION = [4000 + 2.2 * PLATFORM_WIDTH, PLATFORM_POSITION_Y - 31 * PLAYER_HEIGHT]
TWENTYTWO_THIRD_LEVEL_PLATFORM_POSITION = [4000 + 2.3 * PLATFORM_WIDTH, PLATFORM_POSITION_Y - 32.5 * PLAYER_HEIGHT]
TWENTYTHREE_THIRD_LEVEL_PLATFORM_POSITION = [4000 + 2.4 * PLATFORM_WIDTH, PLATFORM_POSITION_Y - 34 * PLAYER_HEIGHT]

FIRST_THIRD_LEVEL_INVISIBLE_PLATFORM_ENEMY_POSITION = [1000, PLATFORM_POSITION_Y - 8.6 * PLAYER_HEIGHT]
SECOND_THIRD_LEVEL_INVISIBLE_PLATFORM_ENEMY_POSITION = [4000 - 1.5 * PLATFORM_WIDTH, PLATFORM_POSITION_Y - 12.2 * PLAYER_HEIGHT]
THIRD_THIRD_LEVEL_INVISIBLE_PLATFORM_ENEMY_POSITION = [4000 - 2 * PLATFORM_WIDTH, PLATFORM_POSITION_Y - 14.3 * PLAYER_HEIGHT]
FOURTH_THIRD_LEVEL_INVISIBLE_PLATFORM_ENEMY_POSITION = [4000 - 3 * PLATFORM_WIDTH, PLATFORM_POSITION_Y - 18.5 * PLAYER_HEIGHT]
FIFTH_THIRD_LEVEL_INVISIBLE_PLATFORM_ENEMY_POSITION = [4000 - 4 * PLATFORM_WIDTH, PLATFORM_POSITION_Y - 20.6 * PLAYER_HEIGHT]
SIXTH_THIRD_LEVEL_INVISIBLE_PLATFORM_ENEMY_POSITION = [4000 - 4 * PLATFORM_WIDTH + 3.5 * PLATFORM_WIDTH, PLATFORM_POSITION_Y - 20.6 * PLAYER_HEIGHT]
SEVENTH_THIRD_LEVEL_INVISIBLE_PLATFORM_ENEMY_POSITION = [4000 - 2 * PLATFORM_WIDTH, PLATFORM_POSITION_Y - 24.8 * PLAYER_HEIGHT]
EIGHTH_THIRD_LEVEL_INVISIBLE_PLATFORM_ENEMY_POSITION = [4000 - 5 * PLATFORM_WIDTH, PLATFORM_POSITION_Y - 22.7 * PLAYER_HEIGHT]
NINETH_THIRD_LEVEL_INVISIBLE_PLATFORM_ENEMY_POSITION = [4000 - 1 * PLATFORM_WIDTH, PLATFORM_POSITION_Y - 22.7 * PLAYER_HEIGHT]

FIRST_THIRD_LEVEL_TRIGGER_POSITION = [ELEVEN_THIRD_LEVEL_PLATFORM_POSITION[0], ELEVEN_THIRD_LEVEL_PLATFORM_POSITION[1] - 0.1*PLATFORM_HEIGHT]
SECOND_THIRD_LEVEL_TRIGGER_POSITION = [SEVENTEEN_SECOND_LEVEL_PLATFORM_POSITION[0] + 100, SEVENTEEN_SECOND_LEVEL_PLATFORM_POSITION[1] - 0.1*PLATFORM_HEIGHT]
THIRD_THIRD_LEVEL_TRIGGER_POSITION = [SIX_THIRD_LEVEL_PLATFORM_POSITION[0] + 100, SIX_THIRD_LEVEL_PLATFORM_POSITION[1] - 0.1*PLATFORM_HEIGHT]

# Размеры платформ
FIRST_ZERO_LEVEL_PLATFORM_SIZE = DEFAULT_PLATFORM_SIZE
SECOND_ZERO_LEVEL_PLATFORM_SIZE = DEFAULT_PLATFORM_SIZE
THIRD_ZERO_LEVEL_PLATFORM_SIZE = DEFAULT_PLATFORM_SIZE
FOURTH_ZERO_LEVEL_PLATFORM_SIZE = DEFAULT_PLATFORM_SIZE

FIRST_FIRST_LEVEL_PLATFORM_SIZE = DEFAULT_PLATFORM_SIZE
SECOND_FIRST_LEVEL_PLATFORM_SIZE = DEFAULT_PLATFORM_SIZE
THIRD_FIRST_LEVEL_PLATFORM_SIZE = DEFAULT_PLATFORM_SIZE
FOURTH_FIRST_LEVEL_PLATFORM_SIZE = [PLATFORM_WIDTH*2, PLATFORM_HEIGHT*2]
FIFTH_FIRST_LEVEL_PLATFORM_SIZE = [PLATFORM_WIDTH * 3, PLATFORM_HEIGHT * 2]
SIX_FIRST_LEVEL_PLATFORM_SIZE = [PLATFORM_WIDTH*0.7, PLATFORM_HEIGHT]
SEVEN_FIRST_LEVEL_PLATFORM_SIZE = [PLATFORM_WIDTH*0.7, PLATFORM_HEIGHT]

FIRST_SECOND_LEVEL_PLATFORM_SIZE = [PLATFORM_WIDTH*2, PLATFORM_HEIGHT * 0.2]
SECOND_SECOND_LEVEL_PLATFORM_SIZE = [PLATFORM_WIDTH*1.5, PLATFORM_HEIGHT * 0.2]
THIRD_SECOND_LEVEL_PLATFORM_SIZE = DEFAULT_PLATFORM_SIZE
FOURTH_SECOND_LEVEL_PLATFORM_SIZE = [PLATFORM_WIDTH*0.5, PLATFORM_HEIGHT]
FIFTH_SECOND_LEVEL_PLATFORM_SIZE = [PLATFORM_WIDTH * 0.25, PLATFORM_HEIGHT * 2]
SIX_SECOND_LEVEL_PLATFORM_SIZE = [PLATFORM_WIDTH*0.7, PLATFORM_HEIGHT]
SEVEN_SECOND_LEVEL_PLATFORM_SIZE = [PLATFORM_WIDTH*0.7, PLATFORM_HEIGHT*0.2]
EIGHT_SECOND_LEVEL_PLATFORM_SIZE = [PLATFORM_WIDTH*1, PLATFORM_HEIGHT*0.2]
NINE_SECOND_LEVEL_PLATFORM_SIZE = [PLATFORM_WIDTH*1, PLATFORM_HEIGHT*0.2]
TEN_SECOND_LEVEL_PLATFORM_SIZE = [PLATFORM_WIDTH*1, PLATFORM_HEIGHT*0.2]
ELEVEN_SECOND_LEVEL_PLATFORM_SIZE = [PLATFORM_WIDTH*1.2, PLATFORM_HEIGHT*0.2]
TWELVE_SECOND_LEVEL_PLATFORM_SIZE = [PLATFORM_WIDTH*0.25, PLATFORM_HEIGHT*0.25]
THIRTEEN_SECOND_LEVEL_PLATFORM_SIZE = [300 * SCALE, PLATFORM_HEIGHT * 1.25]
FOURTEEN_SECOND_LEVEL_PLATFORM_SIZE = [300 * SCALE, 4 * PLATFORM_HEIGHT]
FIFTEEN_SECOND_LEVEL_PLATFORM_SIZE = [300 * SCALE, 7 * PLATFORM_HEIGHT]
SIXTEEN_SECOND_LEVEL_PLATFORM_SIZE = [300 * SCALE, 10 * PLATFORM_HEIGHT]
SEVENTEEN_SECOND_LEVEL_PLATFORM_SIZE = [300 * SCALE, 13 * PLATFORM_HEIGHT]
EIGHTEEN_SECOND_LEVEL_PLATFORM_SIZE = [1 * PLATFORM_WIDTH, 9 * PLATFORM_HEIGHT]
NINETEEN_SECOND_LEVEL_PLATFORM_SIZE = [0.25 * PLATFORM_WIDTH, 11 * PLATFORM_HEIGHT]
TWENTY_SECOND_LEVEL_PLATFORM_SIZE = [4 * PLATFORM_WIDTH, 0.2 * PLATFORM_HEIGHT]
TWENTYONE_SECOND_LEVEL_PLATFORM_SIZE = [1.2 * PLATFORM_WIDTH, 0.2 * PLATFORM_HEIGHT]
TWENTYTWO_SECOND_LEVEL_PLATFORM_SIZE = [6 * PLATFORM_WIDTH, 0.2 * PLATFORM_HEIGHT]
TWENTYTHREE_SECOND_LEVEL_PLATFORM_SIZE = [0.02 * PLATFORM_WIDTH, 5 * PLATFORM_HEIGHT]
TWENTYFOUR_SECOND_LEVEL_PLATFORM_SIZE = [2 * PLATFORM_WIDTH, 0.2 * PLATFORM_HEIGHT]
TWENTYFIVE_SECOND_LEVEL_PLATFORM_SIZE = [5 * PLATFORM_WIDTH, 20 * PLATFORM_HEIGHT]
TWENTYSIX_SECOND_LEVEL_PLATFORM_SIZE = [0.5 * PLATFORM_WIDTH, 0.2 * PLATFORM_HEIGHT]
TWENTYSEVEN_SECOND_LEVEL_PLATFORM_SIZE = [0.5 * PLATFORM_WIDTH, 0.2 * PLATFORM_HEIGHT]
TWENTYEIGHT_SECOND_LEVEL_PLATFORM_SIZE = [0.5 * PLATFORM_WIDTH, 0.2 * PLATFORM_HEIGHT]
TWENTYNINE_SECOND_LEVEL_PLATFORM_SIZE = [0.5 * PLATFORM_WIDTH, 0.2 * PLATFORM_HEIGHT]
THIRTY_SECOND_LEVEL_PLATFORM_SIZE = [0.5 * PLATFORM_WIDTH, 0.2 * PLATFORM_HEIGHT]
THIRTYONE_SECOND_LEVEL_PLATFORM_SIZE = [0.5 * PLATFORM_WIDTH, 0.2 * PLATFORM_HEIGHT]

FIRST_SECOND_LEVEL_INVISIBLE_PLATFORM_ENEMY_SIZE = [PLATFORM_WIDTH * 0.01, PLATFORM_HEIGHT * 3]
SECOND_SECOND_LEVEL_INVISIBLE_PLATFORM_ENEMY_SIZE = [PLATFORM_WIDTH * 0.01, PLATFORM_HEIGHT * 3]
THIRD_SECOND_LEVEL_INVISIBLE_PLATFORM_ENEMY_SIZE = [PLATFORM_WIDTH * 0.01, PLATFORM_HEIGHT * 3]
FOURTH_SECOND_LEVEL_INVISIBLE_PLATFORM_ENEMY_SIZE = [PLATFORM_WIDTH * 0.01, PLATFORM_HEIGHT * 3]

FIRST_SECOND_LEVEL_TRIGGER_SIZE = FIFTH_SECOND_LEVEL_PLATFORM_SIZE

FIRST_THIRD_LEVEL_PLATFORM_SIZE = [PLATFORM_WIDTH * 30, PLATFORM_HEIGHT + PLAYER_HEIGHT * 4.6]
SECOND_THIRD_LEVEL_PLATFORM_SIZE = [1500 * SCALE, PLATFORM_HEIGHT * 0.3]
THIRD_THIRD_LEVEL_PLATFORM_SIZE = [PLATFORM_WIDTH * 0.5, PLATFORM_HEIGHT * 0.18]
FOURTH_THIRD_LEVEL_PLATFORM_SIZE = [PLATFORM_WIDTH * 0.5, PLATFORM_HEIGHT * 0.18]
FIFTH_THIRD_LEVEL_PLATFORM_SIZE = [PLATFORM_WIDTH * 0.5, PLATFORM_HEIGHT * 0.18]
SIX_THIRD_LEVEL_PLATFORM_SIZE = [PLATFORM_WIDTH * 30 - 4000, PLAYER_HEIGHT * 22]
SEVEN_THIRD_LEVEL_PLATFORM_SIZE = [PLATFORM_WIDTH * 0.5, PLATFORM_HEIGHT * 0.18]
EIGHT_THIRD_LEVEL_PLATFORM_SIZE = [PLATFORM_WIDTH * 1, PLATFORM_HEIGHT * 0.18]
NINE_THIRD_LEVEL_PLATFORM_SIZE = [PLATFORM_WIDTH * 1.5, PLATFORM_HEIGHT * 0.18]
TEN_THIRD_LEVEL_PLATFORM_SIZE = [PLATFORM_WIDTH * 2, PLATFORM_HEIGHT * 0.18]
ELEVEN_THIRD_LEVEL_PLATFORM_SIZE = [PLATFORM_WIDTH * 2.5, PLATFORM_HEIGHT * 0.18]
TWELVE_THIRD_LEVEL_PLATFORM_SIZE = [PLATFORM_WIDTH, PLATFORM_HEIGHT * 0.3]
THIRTEEN_THIRD_LEVEL_PLATFORM_SIZE = [PLATFORM_WIDTH * 3, PLATFORM_HEIGHT * 0.18]
FOURTEEN_THIRD_LEVEL_PLATFORM_SIZE = [PLATFORM_WIDTH * 3.5, PLATFORM_HEIGHT * 0.18]
FIFTEEN_THIRD_LEVEL_PLATFORM_SIZE = [PLATFORM_WIDTH * 4, PLATFORM_HEIGHT * 0.18]
SIXTEEN_THIRD_LEVEL_PLATFORM_SIZE = [PLATFORM_WIDTH * 2, PLATFORM_HEIGHT * 0.18]
SEVENTEEN_THIRD_LEVEL_PLATFORM_SIZE = [PLATFORM_WIDTH * 2, PLATFORM_HEIGHT * 0.18]
EIGHTEEN_THIRD_LEVEL_PLATFORM_SIZE = [PLATFORM_WIDTH * 1, PLATFORM_HEIGHT * 0.18]
NINETEEN_THIRD_LEVEL_PLATFORM_SIZE = [PLATFORM_WIDTH * 2, PLATFORM_HEIGHT * 0.18]
TWENTY_THIRD_LEVEL_PLATFORM_SIZE = [PLATFORM_WIDTH * 2, PLATFORM_HEIGHT * 0.18]
TWENTYONE_THIRD_LEVEL_PLATFORM_SIZE = [PLATFORM_WIDTH * 2, PLATFORM_HEIGHT * 0.18]
TWENTYTWO_THIRD_LEVEL_PLATFORM_SIZE = [PLATFORM_WIDTH * 2, PLATFORM_HEIGHT * 0.18]
TWENTYTHREE_THIRD_LEVEL_PLATFORM_SIZE = [PLATFORM_WIDTH * 2, PLATFORM_HEIGHT * 0.18]

FIRST_THIRD_LEVEL_INVISIBLE_PLATFORM_ENEMY_SIZE = [PLATFORM_WIDTH * 0.01, PLAYER_HEIGHT * 4]
SECOND_THIRD_LEVEL_INVISIBLE_PLATFORM_ENEMY_SIZE = [PLATFORM_WIDTH * 0.01, PLAYER_HEIGHT * 2.1]
THIRD_THIRD_LEVEL_INVISIBLE_PLATFORM_ENEMY_SIZE = [PLATFORM_WIDTH * 0.01, PLAYER_HEIGHT * 2.1]
FOURTH_THIRD_LEVEL_INVISIBLE_PLATFORM_ENEMY_SIZE = [PLATFORM_WIDTH * 0.01, PLAYER_HEIGHT * 2.1]
FIFTH_THIRD_LEVEL_INVISIBLE_PLATFORM_ENEMY_SIZE = [PLATFORM_WIDTH * 0.01, PLAYER_HEIGHT * 2.1]
SIXTH_THIRD_LEVEL_INVISIBLE_PLATFORM_ENEMY_SIZE = [PLATFORM_WIDTH * 0.01, PLAYER_HEIGHT * 2.1]
SEVENTH_THIRD_LEVEL_INVISIBLE_PLATFORM_ENEMY_SIZE = [PLATFORM_WIDTH * 0.01, PLAYER_HEIGHT * 2.1]
EIGHTH_THIRD_LEVEL_INVISIBLE_PLATFORM_ENEMY_SIZE = [PLATFORM_WIDTH * 0.01, PLAYER_HEIGHT * 2.1]
NINETH_THIRD_LEVEL_INVISIBLE_PLATFORM_ENEMY_SIZE = [PLATFORM_WIDTH * 0.01, PLAYER_HEIGHT * 2.1]

FIRST_THIRD_LEVEL_TRIGGER_SIZE = ELEVEN_THIRD_LEVEL_PLATFORM_SIZE
THIRD_THIRD_LEVEL_TRIGGER_SIZE = SIX_THIRD_LEVEL_PLATFORM_SIZE

# Camera parameters
CAMERA_X = 0 * SCALE
CAMERA_Y = 0 * SCALE
MAX_PLAYER_CENTER_DISTANCE_X = 100 * SCALE
BORDER_XL = (SCREEN_WIDTH / 2) - MAX_PLAYER_CENTER_DISTANCE_X
BORDER_XR = (SCREEN_WIDTH / 2) + MAX_PLAYER_CENTER_DISTANCE_X
BORDER_YH = FLOOR_DEPTH + PLATFORM_HEIGHT
BORDER_YD = FLOOR_HEIGHT - 2 * PLAYER_HEIGHT

# Enemy positions
FIRST_FIRST_LEVEL_ENEMY_POSITION = [1500, PLATFORM_POSITION_Y]
SECOND_FIRST_LEVEL_ENEMY_POSITION = [3500, PLATFORM_POSITION_Y - 2*PLATFORM_HEIGHT]

FIRST_SECOND_LEVEL_ENEMY_POSITION = [1500, PLATFORM_POSITION_Y - PLATFORM_HEIGHT]
SECOND_SECOND_LEVEL_ENEMY_POSITION = [2000, PLATFORM_POSITION_Y - PLATFORM_HEIGHT]
THIRD_SECOND_LEVEL_ENEMY_POSITION = [2500, PLATFORM_POSITION_Y - PLATFORM_HEIGHT]
FOURTH_SECOND_LEVEL_ENEMY_POSITION = [2600 + ENEMY_WIDTH, PLATFORM_POSITION_Y - PLATFORM_HEIGHT]
FIFTH_SECOND_LEVEL_ENEMY_POSITION = [3000 + ENEMY_WIDTH, PLATFORM_POSITION_Y - PLATFORM_HEIGHT*5 - ENEMY_HEIGHT]
SIXTH_SECOND_LEVEL_ENEMY_POSITION = [3600 + ENEMY_WIDTH, PLATFORM_POSITION_Y - PLATFORM_HEIGHT*5 - ENEMY_HEIGHT]
SEVENTH_SECOND_LEVEL_ENEMY_POSITION = [6500, PLATFORM_POSITION_Y - ENEMY_HEIGHT]
EIGHTH_SECOND_LEVEL_ENEMY_POSITION = [7100, PLATFORM_POSITION_Y - ENEMY_HEIGHT]
NINTH_SECOND_LEVEL_ENEMY_POSITION = [7700+ 2 * ENEMY_WIDTH, PLATFORM_POSITION_Y - ENEMY_HEIGHT]
TENTH_SECOND_LEVEL_ENEMY_POSITION = [8300 + ENEMY_WIDTH, PLATFORM_POSITION_Y - PLATFORM_HEIGHT*5 - ENEMY_HEIGHT]
ELEVENTH_SECOND_LEVEL_ENEMY_POSITION = [9250, PLATFORM_POSITION_Y - PLATFORM_HEIGHT * 8 - ENEMY_HEIGHT]
TWELFTH_SECOND_LEVEL_ENEMY_POSITION = [9350, PLATFORM_POSITION_Y - PLATFORM_HEIGHT * 8 - ENEMY_HEIGHT]
THIRTEENTH_SECOND_LEVEL_ENEMY_POSITION = [9450, PLATFORM_POSITION_Y - ENEMY_HEIGHT]
FOURTEENTH_SECOND_LEVEL_ENEMY_POSITION = [9550, PLATFORM_POSITION_Y - ENEMY_HEIGHT]
FIFTEENTH_SECOND_LEVEL_ENEMY_POSITION = [9650, PLATFORM_POSITION_Y - ENEMY_HEIGHT]
SIXTEENTH_SECOND_LEVEL_ENEMY_POSITION = [9750, PLATFORM_POSITION_Y - PLATFORM_HEIGHT]
SEVENTEENTH_SECOND_LEVEL_ENEMY_POSITION = [9850, PLATFORM_POSITION_Y - PLATFORM_HEIGHT]
EIGHTEENTH_SECOND_LEVEL_ENEMY_POSITION = [9950, PLATFORM_POSITION_Y - PLATFORM_HEIGHT]

FIRST_THIRD_LEVEL_ENEMY_POSITION = [800, PLATFORM_POSITION_Y - 5.7 * PLAYER_HEIGHT]
SECOND_THIRD_LEVEL_ENEMY_POSITION = [1100, PLATFORM_POSITION_Y - 5.7 * PLAYER_HEIGHT]
THIRD_THIRD_LEVEL_ENEMY_POSITION = [1500, PLATFORM_POSITION_Y - 5.7 * PLAYER_HEIGHT]
FOURTH_THIRD_LEVEL_ENEMY_POSITION = [1900, PLATFORM_POSITION_Y - 5.7 * PLAYER_HEIGHT]
FIFTH_THIRD_LEVEL_ENEMY_POSITION = [4000 - 0.5 * PLATFORM_WIDTH, PLATFORM_POSITION_Y - 12.1 * PLAYER_HEIGHT]
SIXTH_THIRD_LEVEL_ENEMY_POSITION = [4000 - 0.5 * PLATFORM_WIDTH, PLATFORM_POSITION_Y - 14.2 * PLAYER_HEIGHT]
SEVENTH_THIRD_LEVEL_ENEMY_POSITION = [4000 - 0.5 * PLATFORM_WIDTH, PLATFORM_POSITION_Y - 18.4 * PLAYER_HEIGHT]
EIGHTH_THIRD_LEVEL_ENEMY_POSITION = [4000 - 0.75 * PLATFORM_WIDTH, PLATFORM_POSITION_Y - 18.4 * PLAYER_HEIGHT]
NINTH_THIRD_LEVEL_ENEMY_POSITION = [4000 - 1 * PLATFORM_WIDTH, PLATFORM_POSITION_Y - 18.4 * PLAYER_HEIGHT]
TENTH_THIRD_LEVEL_ENEMY_POSITION = [4000 - 1.5 * PLATFORM_WIDTH, PLATFORM_POSITION_Y - 20.5 * PLAYER_HEIGHT]
ELEVENTH_THIRD_LEVEL_ENEMY_POSITION = [4000 - 2 * PLATFORM_WIDTH, PLATFORM_POSITION_Y - 20.5 * PLAYER_HEIGHT]
TWELFTH_THIRD_LEVEL_ENEMY_POSITION = [4000 - 2.5 * PLATFORM_WIDTH, PLATFORM_POSITION_Y - 20.5 * PLAYER_HEIGHT]
THIRTEENTH_THIRD_LEVEL_ENEMY_POSITION = [4000 - 2 * PLATFORM_WIDTH, PLATFORM_POSITION_Y - 24.8 * PLAYER_HEIGHT]
FOURTEENTH_THIRD_LEVEL_ENEMY_POSITION = [4000 - 1 * PLATFORM_WIDTH, PLATFORM_POSITION_Y - 24.8 * PLAYER_HEIGHT]
FIFTEENTH_THIRD_LEVEL_ENEMY_POSITION = [4000 - 0.5 * PLATFORM_WIDTH, PLATFORM_POSITION_Y - 24.8 * PLAYER_HEIGHT]
SIXTEENTH_THIRD_LEVEL_ENEMY_POSITION = [4000 - 1.5 * PLATFORM_WIDTH, PLATFORM_POSITION_Y - 24.8 * PLAYER_HEIGHT]

# Ось и циферки
FONT_SIZE = int(30 * SCALE)

# Физические константы
FPS = 60
G = 1500 * SCALE
DELTA_T = 1/FPS

# Картинки
IMAGES_DIRECTORY = "source/images/"
BACKGROUND_FILENAME = IMAGES_DIRECTORY + "wallpaper_cut.jpg"
FLOOR_FILENAME = IMAGES_DIRECTORY + "floor.png"
PLAYER_FILENAME = IMAGES_DIRECTORY + "player.png"
PLAYER_ATTACK_FILENAME = IMAGES_DIRECTORY + "player_attack.png"
ENEMY_FILENAME = IMAGES_DIRECTORY + "enemy.png"
ENEMY_ATTACK_FILENAME = IMAGES_DIRECTORY + "enemy_attack.png"
PLATFORM_FILENAME = IMAGES_DIRECTORY + "platform.png"
HEALTH_POINT_FILENAME = IMAGES_DIRECTORY + "healt_point.png"
TEXT_SURFACE_FILENAME = IMAGES_DIRECTORY + "text_surface.png"

# Звуки
SOUND_DIRECTORY = "source/sounds/"
BACK_MUSIC_1 = SOUND_DIRECTORY + "Back_music_1.mp3"
BUM_1 = SOUND_DIRECTORY + "Bym_1.mp3"

# Параметры кнопок
BUTTON_NEW_GAME_SIZE_WIDTH = 200
BUTTON_NEW_GAME_SIZE_HEIGHT = 50
BUTTON_EXIT_SIZE_WIDTH = 200
BUTTON_EXIT_SIZE_HEIGHT = 50
BUTTON_EXIT_POSITION_X = 500
BUTTON_EXIT_POSITION_Y = 500
BUTTON_NEW_GAME_POSITION_X = 500
BUTTON_NEW_GAME_POSITION_Y = 350
