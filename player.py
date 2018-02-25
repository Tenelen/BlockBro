import pygame
from time import sleep

class Player():
    def __init__(self, settings, screen, platform):
        self.player_speed = settings.player_speed
        self.velocity = settings.velocity

        self.settings = settings

        self.screen = screen
        self.player_width = settings.player_width
        self.player_height = settings.player_height
        self.player_color = settings.player_color


        self.direction = 1
        self.move_left = False
        self.move_right = False
        self.jumping = False
        self.onGround = False
        #self.jumptime = 0

        self.image = pygame.Surface([self.player_width, self.player_height])
        self.image.fill(self.player_color)
        self.rect = self.image.get_rect()

        self.centerx = float(self.rect.centerx)
        self.bottom = int(self.rect.bottom)

        self.platform = platform
        #self.platform1 = platform.rect_plat1
        #self.platform2 = platform.rect_plat2


    def place_player(self):
        self.centerx = 200
        self.bottom = 100

    def blitme(self):
        self.screen.blit(self.image, self.rect)

    def check_player(self, settings, screen):
        if self.rect.bottom >= settings.screen_height:
            self.onGround = True

    def collision(self, settings, screen, platform):
        if pygame.Rect.colliderect(self.rect, self.platform):
        #or pygame.Rect.colliderect(self.rect, self.platform2):
            self.onGround = True
            self.jumping = False
        elif self.bottom >= self.settings.screen_height:
            self.onGround = True
        else:
            self.onGround = False

    def jump(self, settings):
        if self.onGround and self.jumping == False:
            self.jumping = True
            self.bottom -= 150
            self.centerx += (self.direction * 5)
            self.jumping = False
        else:
            self.velocity = self.settings.velocity

    def gravity(self, settings):
        if self.onGround == True:
            self.velocity = 0
        elif self.jumping:
            self.velocity = 0
        else:
            self.velocity = self.settings.velocity

    def check_position(self, settings):
        if self.move_right == True and self.rect.right <= self.settings.screen_width - 1:
            self.centerx += 3
        elif self.move_left == True and self.rect.left > 0:
            self.centerx -= 3
        self.bottom += self.velocity
        self.rect.centerx = self.centerx
        self.rect.bottom = self.bottom

    def update(self, settings, screen, platform):
        self.check_player(settings, screen)
        self.collision(settings, screen, platform)
        self.gravity(settings)
        self.check_position(settings)
