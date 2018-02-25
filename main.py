import pygame
from time import sleep
import game_functions as gf
from settings import Settings
from player import Player
from platforms import Platform
from pygame.sprite import Group


def run_game():
    clock = pygame.time.Clock()
    pygame.init()
    settings = Settings()
    screen = pygame.display.set_mode((settings.screen_width, settings.screen_height))
    pygame.display.set_caption("Cube Bro")

    platform = Platform(screen)
    player = Player(settings, screen, platform)
    player.place_player()

    while True:
        clock.tick(60)
        gf.check_events(settings, player, platform)
        player.update(settings, screen, platform)
        gf.update_screen(screen, settings, player, platform)


run_game()
