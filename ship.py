import pygame
from pygame.sprite import Sprite

class Ship(Sprite):
    """Classes for managing spaceships"""

    def __init__(self, ai_game) -> None:
        """Инициализирует корабль и задает его начальную позицию."""
        super().__init__()
        self.screen = ai_game.screen
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

    def blitme(self) -> None:
        """Рисует корабль в текущей позиции."""
        self.screen.blit(self.image, self.rect)

    def update(self) -> None:
        """Обновляет позиции корабля с учетом флагов."""
        # Переместить корабль.
        # Обновить атрибут х объекта ship, не rect.
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed

        # Обновление статуса rect на соновании self.x.
        self.rect.x = self.x

    def center_ship(self) -> None:
        # Размещает корабль в центре нижней стороны.
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)
