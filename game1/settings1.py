class Settings():
    """Класс для хранения настроек для игры."""
    
    def __init__(self):
        """Инициализирует настройки игры."""
        # Настройки для экрана
        self.screen_width = 1600
        self.screen_height = 900
        self.bg_color = (137, 181, 250)
        # Настройки для ракеты
        self.rocket_speed = 0.5
    
