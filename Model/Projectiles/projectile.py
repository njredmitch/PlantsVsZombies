from abc import ABC
import pygame

class ProjectileMeta(type(ABC), type(pygame.sprite.Sprite)): pass

class Projectile(ABC, pygame.sprite.Sprite):
    __metaclass__=ProjectileMeta
    def __init__(self, position, dmg, path) -> None:
        ABC.__init__(self)
        pygame.sprite.Sprite.__init__(self)
        self._dmg = dmg
        self._position = position
        self.image = pygame.image.load(path)
        self.rect = self.image.get_rect(midleft = self._position)
    
    def get_pos(self):
        return self._position

    def update_xpos(self, x):
        self._position = (self._position[0] + x, self._position[1])
    
    def update_ypos(self):
        pass

    def get_dmg(self):
        return self._dmg
    
    def get_rect(self):
        return self.rect

    def convert_image(self):
        self.image.convert_alpha()