"""Создание класса кнопки старт."""
from tkinter import font
import pygame.font


class Button:
    """Описание кнопки Button."""

    def __init__(self, ai_game, msg) -> None:
        """Инициализирует атрибуты кнопки."""
        self.screen = ai_game
        self.screen_rect = self.screen.screen.get_rect()

        # Назначение размеров и свойств кнопки.
        self.width, self.height = 200, 50
        self.button_color = (0, 255, 0)
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 48)

        # Построение объекта rect кнопки и выравнивание по центру экрана.
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center

        # Сообщение кнопки создается только один раз.
        self._prep_msg(msg)

    def _prep_msg(self, msg) -> None:
        """Преобразует msg в прямоугольник и выравнивает текст по центру."""
        self.msg_image = self.font.render(msg, True, self.text_color,
                                          self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw_button(self) -> None:
        """Отображение пустой кнопк и вывод сообщения."""
        self.screen.screen.fill(self.button_color, self.rect)
        self.screen.screen.blit(self.msg_image, self.msg_image_rect)
