import pygame
from pygame.sprite import Sprite

class Platform(Sprite):
    def __init__(self, screen):
        #Call Sprite
        Sprite.__init__(self)

        self.width = 100
        self.height = 10
        self.color = (0, 255, 0)

        self.screen = screen

        self.image = pygame.Surface([self.width, self.height])
        self.image.fill(self.color)
        self.rect = self.image.get_rect()
        self.rect.x = 200
        self.rect.y = 200


        #self.platform_rect_list = [self.rect_plat1, self.rect_plat2]


    def blitme(self):
        self.screen.blit(self.image, self.rect)
