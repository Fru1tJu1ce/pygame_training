import pygame
from pygame.sprite import Group

from settings import Settings
import game_functions as gf
from boy import Boy
from game_stats import GameStats


def run_game():
    """Функция, инициализирующая запуск игры ball_catcher"""
    pygame.init()
    bc_settings = Settings()
    screen = pygame.display.set_mode(
        (bc_settings.screen_width, bc_settings.screen_height))
    pygame.display.set_caption("Ball Catcher")
    
    # Создает набор статистик
    stats = GameStats(bc_settings)
    # Создает экземпляр мальчика-ловца
    boy = Boy(bc_settings, screen)
    # Создает группу из мяча
    balls = Group()
    # Создание мяча
    gf.create_ball(bc_settings, screen, balls)
    
    while True:
        gf.check_events(boy)
        if stats.game_active:
            boy.update()
            gf.update_ball(stats, bc_settings, screen, boy, balls)
            gf.update_screen(bc_settings, screen, boy, balls)


run_game()
