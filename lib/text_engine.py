import pygame as pg

from lib.constants import TEXT_SURFACE_FILENAME


class TextSurface:

    def __init__(self, text):
        self.is_text_open = False # Game on pause while we're reading a text
        self.surface_image = pg.image.load(TEXT_SURFACE_FILENAME)
        self.font = pg.font.Font(None, 50)
        self.text = text

    def draw(self, surface):
        if self.is_text_open:
            surface.blit(self.surface_image, (100, 100))
        if not self.is_text_open: # После закрытия текста очищает картинку от прошлого текста
            self.surface_image = pg.image.load(TEXT_SURFACE_FILENAME)

    def put_text(self, trigger_number): # Загружает текст, присущий этому триггеру
        self.is_text_open = True
        self.surface_image.blit(self.font.render(self.text[trigger_number], True, "black"), (10, 10))

    def continue_text(self, mouse_pressed): # Перелистывание текста
        if mouse_pressed == 1:
            self.is_text_open = False

