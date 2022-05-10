"""Создание класса, представляющее окно игры."""
import sys
import pygame

from settings import Settings
from ship import Ship


class AlienInvasion:
    """Класс управления ресурсами и поведением игры."""

    def __init__(self) -> None:
        """Инициализирует игру и создает игровые ресурсы."""
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Alien Invasion")

        self.ship = Ship(self.screen)

        # Назначение цвета фона.
        self.bg_color = (self.settings.bg_color)

    def run_game(self) -> None:
        """Запуск основного цикла."""
        while True:
            # Отслеживание событий клавиатуры и мыши.
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            # При каждом проходе цикла перерисовывает экран.
            self.screen.fill(self.bg_color)
            self.ship.blitme()

            # Отображение последнего прорисованного экрана.
            pygame.display.flip()


if __name__ == "__main__":
    # Создание экземпляра класса и запуск игры.
    ai = AlienInvasion()
    ai.run_game()
