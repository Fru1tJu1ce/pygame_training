import pygame
from pygame.sprite import Sprite


class Ball(Sprite):
    """Класс для инициализации мяча"""
    
    def __init__(self, bc_settings, screen):
        """
        Инициализация изображения мяча 
        и его перемещение в координату (0, 0).
        """
        super().__init__()
        self.bc_settings = bc_settings
        self.screen = screen
        
        # Инициализициа изображения
        self.image = pygame.image.load('images/ball.bmp')
        self.rect = self.image.get_rect()
        
        # Перемещение в координату (0, -размер мяча)
        self.rect.x = 0
        self.rect.y = -self.rect.height
        
        # Позиция по y хранится в вещественном формате        
        self.y = float(self.rect.y)

        
        
    def update(self):
        """Обновляет позицию мяча с учётом его скорости."""
        self.y += self.bc_settings.ball_speed_factor
        self.rect.y = self.y
            
        
    def blitme(self):
        """Функция для тестового вывода изобрадения мяча"""
        self.screen.blit(self.image, self.rect)
