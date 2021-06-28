class Settings():
    """Класс для хранения настроек ball_catcher"""
    
    def __init__(self):
        """Инициализация настроек игры."""
        # Настройки экрана
        self.screen_width = 1280
        self.screen_height = 720
        self.bg_color = (248, 255, 181)
        # Настройки мальчика
        self.boy_speed_factor = 1.5
        self.boy_lifes = 3
        # Настройки мяча
        self.ball_speed_factor = 0.8
        # Новые настройки
        #self.ball_angle = 
