import sys
from time import sleep

import pygame

import random

from ball import Ball


def check_events(boy):
    """Функция для проверки событий нажатия клавиш клавиатуры и мыши."""
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            check_keydown_events(event, boy)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, boy)
        elif event.type == pygame.QUIT:
            sys.exit()
            

def check_keydown_events(event, boy):
    """Реагирует на нажитие клавиш"""
    if event.key == pygame.K_RIGHT:
        boy.moving_right = True
    elif event.key == pygame.K_LEFT:
        boy.moving_left = True
    elif event.key == pygame.K_q:
        sys.exit()
    

def check_keyup_events(event, boy):
    """Реагирует на отжатие клавиш"""
    if event.key == pygame.K_RIGHT:
        boy.moving_right = False
    elif event.key == pygame.K_LEFT:
        boy.moving_left = False
        
        
def create_ball(bc_settings, screen, balls):
    """Функция для создания экземпляра мяча и внесение его в список"""
    ball = Ball(bc_settings, screen)
    ball_width = ball.rect.width
    # Задание случайного местоположения по x
    ball.rect.right = random.randint(ball_width, 
                                     bc_settings.screen_width)
    # Внесение мяча в список
    balls.add(ball)


def check_ball_pos(stats, bc_settings, screen, boy, balls):
    """Проверяет на заход за экран мяча"""
    for ball in balls.sprites():
        if ball.rect.top > bc_settings.screen_height:
            ball_not_caught(stats, bc_settings, screen, boy, balls)
            

def ball_not_caught(stats, bc_settings, screen, boy, balls):
    """Уменьшает количество мячей на 1 и создает новый экземпляр мяча"""
    if stats.boy_lifes_left > 0 :
        # Уменьшает количество мячей на 1
        stats.boy_lifes_left -= 1
        
        # Очистка мячей
        balls.empty()
        
        # Создает новый экземпляр мяча
        create_ball(bc_settings, screen, balls)
        
        # Размещение мальчика в центре экрана
        boy.center_boy()
        
        # Пауза
        sleep(0.5)
    else:
        stats.game_active = False


def update_screen(bc_settings, screen, boy, balls):
    """Обновляет содержимое экрана"""
    screen.fill(bc_settings.bg_color)
    balls.draw(screen)
    boy.blitme()
    # Отображение последнего прорисованного экрана.
    pygame.display.flip()


def update_ball(stats, bc_settings, screen, boy, balls):
    """Обновляет позиции мяча с учетом захода за экран"""
    check_collisions(bc_settings, screen, boy, balls)
    check_ball_pos(stats, bc_settings, screen, boy, balls)
    balls.update()
    
    
def check_collisions(bc_settings, screen, boy, balls):
    """Проверяет коллизию мяча и мальчика-ловца"""
    if pygame.sprite.spritecollideany(boy, balls):
        balls.empty()
        create_ball(bc_settings, screen, balls)
