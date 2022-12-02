from abc import ABC, abstractmethod
import pygame
from pygame.sprite import Sprite

class Projectile(ABC, Sprite):

    def __init__(self, position, dmg, path) -> None:
        ABC.__init__(self)
        Sprite.__init__(self)
        self._dmg = dmg
        self._position = position
        self.image = pygame.image.load(path)
        self.rect = self.image.get_rect(midleft = self._position)
    
    def update_xpos(self):
        self._position[0] += 1
    
    def update_ypos(self):
        pass

    def get_dmg(self):
        return self._dmg
    
    def convert_image(self):
        self.image.convert_alpha()