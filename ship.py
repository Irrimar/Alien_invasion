"""Создание класса для управления кораблем."""
import pygame


class Ship():
    """Класс для управления кораблем."""

    def __init__(self, ai_game) -> None:
        """Инициализирует корабль и задает его начальную позицию."""
        self.screen = ai_game
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        # Загружает изображение корабля и получает прямоугольник.
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()

        # Каждый новый корабль появляется у нижнего края экрана.
        self.rect.midbottom = self.screen_rect.midbottom

        # Сохранение вещественной координаты центра корабля.
        self.x = float(self.rect.x)

        # Флаг перемещения.
        self.moving_right = False
        self.moving_left = False

    def update(self) -> None:
        """Обновляет позиции корабля с учетом флагов."""
        # Переместить корабль.
        if self.moving_right:
            self.x += self.settings.ship_speed
        if self.moving_left:
            self.x -= self.settings.ship_speed

        # Обновление статуса rect на соновании self.x.
        self.rect.x = self.x

    def blitme(self) -> None:
        """Рисует корабль в текущей позиции."""
        self.screen.screen.blit(self.image, self.rect)
