import sys

import pygame


def check_keyup_events(event, rocket):
    """Реагирует на отпускание клавиши."""
    if event.key == pygame.K_RIGHT:
        rocket.moving_right = False 
    elif event.key == pygame.K_LEFT:
        rocket.moving_left = False  
    elif event.key == pygame.K_UP:
        rocket.moving_up = False  
    elif event.key == pygame.K_DOWN:
        rocket.moving_down = False


def check_keydown_events(event, rocket):
    """Реагирует на нажатие клавиши."""
    if event.key == pygame.K_RIGHT:
        rocket.moving_right = True 
    elif event.key == pygame.K_LEFT:
        rocket.moving_left = True  
    elif event.key == pygame.K_UP:
        rocket.moving_up = True  
    elif event.key == pygame.K_DOWN:
        rocket.moving_down = True
    elif event.key == pygame.K_q:
        sys.exit()


def check_events(rocket):
    """Обрабатывает нажатия клавиш и события мыши."""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, rocket)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, rocket)


def update_screen(mfg_settings, screen, rocket):
    """Обновляет изображение на экране и отображает новый экран."""
    screen.fill((mfg_settings.bg_color))
    
    rocket.print_rocket()
    rocket.switch_image()
    
    # Отображение последнего прорисованного экрана.
    pygame.display.flip()
