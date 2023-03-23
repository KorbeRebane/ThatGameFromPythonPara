import pygame as pg


class Button:

    def __init__(self, size, position, text, color, on_click):
        self.size = size
        self.position = position
        self.text = text
        self.color = pg.color.Color(color)

        self.font = pg.font.Font(None, 50)
        self.text_image = self.font.render(self.text, True, "black")

        self.image = pg.surface.Surface(self.size)
        self.image.fill(self.color)
        self.image.blit(self.text_image, (0, 0))

        self.on_click_function = on_click

    def draw(self, surface):
        surface.blit(self.image, self.position)

    def clicked(self):
        self.on_click_function()

