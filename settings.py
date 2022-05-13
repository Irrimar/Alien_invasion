"""Создание класса Settings."""


class Settings:
    """Класс для хранения всех настроек игры Alien Invasion."""

    def __init__(self) -> None:
        """Инициализирует настройки игры."""
        # Параметры экрана.
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        # Настройка корабля.
        self.ship_speed = 0.5
        self.ship_limit = 3

        # Параметры снаряда
        self.bullet_speed = 0.5
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 3

        # Настройки пришельцев.
        self.alien_speed = 0.05
        self.fleet_drop_speed = 200
        # fleet.directio = 1 обозначает движение вправо; а -1 - влево.
        self.fleet_direction = 1
