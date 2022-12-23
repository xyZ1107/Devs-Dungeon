# Class to hold block objects

import pygame
from config import *

class Block(pygame.sprite.Sprite):
    def __init__(self, position: tuple[int, int]) -> None:
        super().__init__()
        self.image_list = [pygame.image.load(file) for file in block_images]
        self.image = self.image_list[0]
        self.rect = self.image.get_rect()
        self.rect.center = position
    
    def update(self):
        self.keypress()

    def keypress(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_UP] and self.rect.topleft[1] > 0:
            self.image = self.image_list[1]
            self.rect.topleft -= pygame.Vector2(0, 10)
        elif keys[pygame.K_DOWN] and self.rect.bottomleft[1] < HEIGHT:
            self.image = self.image_list[0]
            self.rect.topleft += pygame.Vector2(0, 10)
        elif keys[pygame.K_LEFT] and self.rect.topleft[0] > 0:
            self.image = self.image_list[2]
            self.rect.topleft -= pygame.Vector2(10, 0)
        elif keys[pygame.K_RIGHT] and self.rect.topright[0] < WIDTH:
            self.image = self.image_list[3]
            self.rect.topleft += pygame.Vector2(10, 0)

    