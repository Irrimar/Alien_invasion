"""Создание класса Settings."""


class Settings:
    """Класс для хранения всех настроек игры Alien Invasion."""

    def __init__(self) -> None:
        """Инициализирует статические настройки игры."""
        # Параметры экрана.
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        # Настройка корабля.
        self.ship_speed_start = 0.5
        self.ship_limit = 3

        # Параметры снаряда
        self.bullet_speed_start = 0.5
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 3

        # Настройки пришельцев.
        self.alien_speed_start = 0.05
        self.fleet_drop_speed = 10

        # Подсчет очков.
        self.alien_points_start = 50

        # Темп ускорения игры
        self.speedup_scale = 1.5

        # Темп роста стоимости пришельцев.
        self.score_scale = 1.5

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self) -> None:
        """Инициализирует настройки изменяющиеся в ходе игры."""
        self.ship_speed += 0.2 #self.ship_speed_start
        self.bullet_speed = self.bullet_speed_start
        self.alien_speed = self.alien_speed_start
        self.alien_points = self.alien_points_start

        # fleet.directio = 1 обозначает движение вправо; а -1 - влево.
        self.fleet_direction = 1

    def increase_speed(self) -> None:
        """Увеличение настройки скорости."""
        self.ship_speed += self.speedup_scale
        self.bullet_speed = self.speedup_scale
        self.alien_speed *= self.speedup_scale
        self.alien_points = int(self.alien_points * self.score_scale)
