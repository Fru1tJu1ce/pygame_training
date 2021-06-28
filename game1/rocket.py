import pygame

import random

images = ['images/rocketBackground.bmp', 'images/rocketBackground2.bmp']


class Rocket():
    """Класс для отображения ракеты."""
    
    def __init__(self, mfg_settings, screen):
        """Инициализация персонажа и присвоение ему начальной позиции"""
        self.screen = screen
        self.mfg_settings = mfg_settings
        self.image = pygame.image.load('images/rocketBackground.bmp')
        # Флаг для картинки
        self.switch = True
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        
        # Начальная позиция
        self.rect.centerx = self.screen_rect.centerx
        self.rect.centery = self.screen_rect.centery
        self.centerx = float(self.rect.centerx)
        self.centery = float(self.rect.centery)
        # Флаги перемещения
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

    def update(self):
        """Обновляет позицию ракеты с учетом флагов."""
        if (self.moving_left and self.rect.left > 0):
            self.centerx -= self.mfg_settings.rocket_speed
        if (self.moving_right and 
            self.rect.right < self.screen_rect.right):
            self.centerx += self.mfg_settings.rocket_speed

        if (self.moving_up and self.rect.top > 0):
            self.centery -= self.mfg_settings.rocket_speed
        if (self.moving_down and 
            self.rect.bottom < self.screen_rect.bottom):
            self.centery += self.mfg_settings.rocket_speed
            
        self.rect.centerx = self.centerx
        self.rect.centery = self.centery

    def print_rocket(self):
        """Выводит изображение ракеты."""
        self.screen.blit(self.image, self.rect)
        
    def switch_image(self):
        """Меняет картинку огня ракеты."""
        if self.switch:
            self.image = pygame.image.load(images[1])
            self.switch = False
        else:
            self.image = pygame.image.load(images[0])
            self.switch = True
