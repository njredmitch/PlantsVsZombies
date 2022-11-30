import pygame
from pygame.sprite import Sprite

class PlantShop(Sprite):

    def __init__(self, path, pos, cost) -> None:
        super().__init__()
        self.image = pygame.image.load(path)
        self.rect = self.image.get_rect(midbottom = pos)
        self._cost = cost
    
    def get_cost(self):
        return self._cost
    
    
    
