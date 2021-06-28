class GameStats():
    """Класс для отслеживания статистики Ball Catcher"""
    
    def __init__(self, bc_settings):
        self.bc_settings = bc_settings
        self.reset_stats()
        # Игра запускается в активном состоянии
        self.game_active = True

    def reset_stats(self):
        """Инициализирует статистику, изменяющуюся в ходе игры."""
        self.boy_lifes_left = self.bc_settings.boy_lifes
