from abc import ABC
from projectile import Projectile
import pygame

class Pea(Projectile, ABC, pygame.sprite.Sprite):

    def __init__(self, position, dmg, path) -> None:
        Projectile.__init__(self, position, dmg)
        ABC.__init__(self)
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(path)
        self.rect = self.image.get_rect(midbottom = self._position)

    def draw(self, display: pygame.display):
        display.blitz(self.rect) 
    
    def convert_image(self):
        self.image.convert_alpha()
    

    
    