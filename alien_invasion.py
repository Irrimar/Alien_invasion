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

        self.ship = Ship(self)

        # Назначение цвета фона.
        self.bg_color = (self.settings.bg_color)

    def run_game(self) -> None:
        """Запуск основного цикла."""
        while True:
            # Отслеживание событий клавиатуры и мыши.
            self._check_events()
            # Обновляет позиции корабля.
            self.ship.update()
            # При каждом проходе цикла перерисовывает экран.
            self._update_screen()

    def _check_events(self) -> None:
        """Обрабатывает нажатие клавиш и события мыши."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _check_keydown_events(self, event) -> None:
        """Реагирует на нажатие клавиш."""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_q:
            sys.exit()

    def _check_keyup_events(self, event) -> None:
        """Реагирует на отпускание клавишь."""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False

    def _update_screen(self) -> None:
        """Обновляет изображение на экране и отображает новый экран."""
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()

        # Отображение последнего прорисованного экрана.
        pygame.display.flip()


if __name__ == "__main__":
    # Создание экземпляра класса и запуск игры.
    ai = AlienInvasion()
    ai.run_game()
