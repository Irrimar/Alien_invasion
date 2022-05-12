"""Создание класса, представляющее окно игры."""
from cmath import rect
import sys
import pygame

from settings import Settings
from ship import Ship
from bullet import Bullet
from alien import Alien


class AlienInvasion:
    """Класс управления ресурсами и поведением игры."""

    def __init__(self) -> None:
        """Инициализирует игру и создает игровые ресурсы."""
        pygame.init()
        self.settings = Settings()

        # Оконны режим
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))

        # Полноэкранный режим
        # self.screen = pygame.display.set_mode((0, 0) , pygame.FULLSCREEN)
        # self.settings.screen_width = self.screen.get_rect().width
        # self.settings.screen_height = self.screen.get_rect().height

        pygame.display.set_caption("Alien Invasion")

        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()

        self._create_fleet()

        # Назначение цвета фона.
        self.bg_color = (self.settings.bg_color)

    def run_game(self) -> None:
        """Запуск основного цикла."""
        while True:
            # Отслеживание событий клавиатуры и мыши.
            self._check_events()
            # Обновляет позиции корабля.
            self.ship.update()
            # Обновление позиции снарядов и уничтожает старые снаряды.
            self._update_bullets()
            # Обновление позиции пришельцев.
            self._update_aliens()
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
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()

    def _check_keyup_events(self, event) -> None:
        """Реагирует на отпускание клавишь."""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False

    def _fire_bullet(self) -> None:
        """Создание нового снаряда и включение его в группу Bullets."""
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _update_bullets(self) -> None:
        # Обновление позиции снарядов и уничтожает старые снаряды.
        self.bullets.update()
        # Удаление снарядов, вышедших за край экрана.
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)

    def _update_aliens(self) -> None:
        """Обновление позиции всех пришельцев во флоте."""
        self._check_fleet_edges()
        self.aliens.update()

    def _create_fleet(self) -> None:
        """Создание флота вторжения."""
        # Создание пришельца.
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        avaliable_space_x = self.settings.screen_width - (2 * alien_width)
        number_alien_x = avaliable_space_x // (2 * alien_width)

        # Определяем количество рядов, помещающихся на экране.
        ship_height = self.ship.rect.height
        avaliable_space_y = (self.settings.screen_height -
                                (3 * alien_height) - ship_height)
        number_rows = avaliable_space_y // (2 * alien_height)

        # Создание первого ряда пришельцев.
        for row_number in range(number_rows):
            for alien_number in range(number_alien_x):
            # Создание пришельца и размещение его вряду.
                self._create_alien(alien_number, row_number)

    def _create_alien(self, alien_number: int, row_number: int) -> None:
        """Создание пришельца и рзмещение его вряду."""
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        alien.x = alien_width + 2 * alien_width * alien_number
        alien.rect.x = alien.x
        alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
        self.aliens.add(alien)

    def _check_fleet_edges(self) -> None:
        """Реагирует на достижение пришельцем края экрана."""
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break

    def _change_fleet_direction(self) -> None:
        """Опускает весь флот и меняет направление флота."""
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1

    def _update_screen(self) -> None:
        """Обновляет изображение на экране и отображает новый экран."""
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()

        self.aliens.draw(self.screen)

        # Отображение последнего прорисованного экрана.
        pygame.display.flip()


if __name__ == "__main__":
    # Создание экземпляра класса и запуск игры.
    ai = AlienInvasion()
    ai.run_game()
