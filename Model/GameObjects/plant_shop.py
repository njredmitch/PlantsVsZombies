import pygame
from pygame.sprite import Sprite

class PlantShop(Sprite):

    def __init__(self, path, pos, cost, plant) -> None:
        super().__init__()
        self.image = pygame.image.load(path)
        self.rect = self.image.get_rect(midbottom = pos)
        self._cost = cost
        self._plant = plant
    
    def get_cost(self):
        return self._cost
    
    def get_plant(self):
        return self._plant