import pygame

import game_func as gf
from settings1 import Settings
from rocket import Rocket

def run_game():
    """Инициализирует pygame, окно экрана."""
    pygame.init()
    mfg_settings = Settings()
    screen = pygame.display.set_mode(
        (mfg_settings.screen_width, mfg_settings.screen_height))
    pygame.display.set_caption("My First Game")
    
    # Создание персонажа
    rocket = Rocket(mfg_settings, screen)
    
    while True:
        gf.check_events(rocket)
        rocket.update()
        gf.update_screen(mfg_settings, screen, rocket)

    
run_game()
