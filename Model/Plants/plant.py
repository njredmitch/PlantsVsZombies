from abc import ABC
import pygame

class PlantMeta(type(ABC), type(pygame.sprite.Sprite)): pass

class Plant(ABC, pygame.sprite.Sprite):
    __metaclass__=PlantMeta
    def __init__(self, health, position, path) -> None:
        ABC.__init__(self)
        pygame.sprite.Sprite.__init__(self)
        self._health = health
        self._life_state = True
        self._position = position
        self.image = pygame.image.load(path)
        self.rect = self.image.get_rect(topleft = self._position)
    
    def lose_health(self, dmg):
        self.set_health(self._health - dmg)
    
    def convert_image(self):
        self.image.convert_alpha()
    
    def set_health(self, health):
        self._health = health
    
    def set_life_state(self, state):
        self._life_state = state

    def set_position(self, position):
        self._position = position
    
    def get_health(self):
        return self._health
    
    def get_life_state(self):
        return self._life_state
    
    def get_position(self):
        return self._position