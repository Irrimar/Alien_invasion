"""Класс статистики."""


class GameStats:
    """Отслеживание статистики для игры Alien Invasion."""

    def __init__(self, ai_game) -> None:
        """Инициализирует статистику."""
        self.settings = ai_game.settings
        self.reset_stats()

        # Игра Alien Invasion запускается в активном состоянии.
        self.game_active = True

    def reset_stats(self) -> None:
        """Инициализирует статистику, изменяющуюся в ходе игры."""
        self.ships_left = self.settings.ship_limit
