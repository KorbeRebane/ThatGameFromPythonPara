from lib.constants import CAMERA_X, CAMERA_Y, BORDER_YH, BORDER_YD, BORDER_XL, BORDER_XR


class Camera:
    def __init__(self):
        self.position = [CAMERA_X, CAMERA_Y]

    def camera_movement(self, player):
        if self.position[0] <= player.position[0] - BORDER_XR:
            self.position[0] = player.position[0] - BORDER_XR
        if self.position[0] >= player.position[0] - BORDER_XL:
            self.position[0] = player.position[0] - BORDER_XL

        if self.position[1] <= player.position[1] - BORDER_YD:
            self.position[1] = player.position[1] - BORDER_YD
        elif self.position[1] >= player.position[1] - BORDER_YH:
            self.position[1] = player.position[1] - BORDER_YH