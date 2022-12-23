# Enemy Object File

import pygame
from config import *

class Enemy(pygame.sprite.Sprite):
    def __init__(self) -> None:
        super().__init__()
        self.enemy_list = [pygame.image.load(file) for file in enemy_images]

