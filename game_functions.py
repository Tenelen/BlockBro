import pygame
from time import sleep
import sys

def update_screen(screen, settings, player, platform):
    screen.fill(settings.bg_color)
    platform.blitme()
    player.blitme()
    pygame.display.flip()

def check_keyup_events(event, settings, player, platform):
    if event.key == pygame.K_LEFT:
        player.move_left = False
    elif event.key == pygame.K_RIGHT:
        player.move_right = False


def check_keydown_events(event, settings, player, platform):
    if event.key == pygame.K_SPACE:
        player.jump(settings)
    elif event.key == pygame.K_RIGHT:
        player.direction = 1
        player.move_right = True
    elif event.key == pygame.K_LEFT:
        player.direction = -1
        player.move_left = True
    elif event.key == pygame.K_b:
        player.player_height += 5
    elif event.key == pygame.K_q:
        pygame.quit()
        sys.exit()

def check_events(settings, player, platform):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, settings, player, platform)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, settings, player, platform)
