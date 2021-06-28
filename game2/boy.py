import pygame


class Boy():
    """Класс для инициализации мальчика-ловца"""
    
    def __init__(self, bc_settings, screen):
        """Инициализация изображения мальчика и его начальной позиции"""
        self.screen = screen
        self.bc_settings = bc_settings
        
        # Инициализация изображения мальчика-ловца
        self.image = pygame.image.load('images/boy_screen_fill_big.bmp')
        self.rect = self.image.get_rect()
        
        # Инициализация его начальной позиции
        self.screen_rect = screen.get_rect()
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        self.x = float(self.rect.centerx)
        
        # Флаги для перемещения мальчика
        self.moving_right = False
        self.moving_left = False
        
    
    def update(self):
        """Функция для реалиции движения мальчика влево и вправо"""
        if (self.moving_right and 
            self.rect.right < self.screen_rect.right):
            self.x += self.bc_settings.boy_speed_factor                
        if (self.moving_left and self.rect.left > 0):
            self.x -= self.bc_settings.boy_speed_factor
        self.rect.centerx = self.x                        
 
    
    def blitme(self):
        """Функция для отображения мальчика-ловца"""
        self.screen.blit(self.image, self.rect)
        
    
    def center_boy(self):
        """Размещает мальчика-ловца в середине экрана."""
        self.x = self.screen_rect.centerx

