import pygame
import copy
from Model.Plants.plant import Plant

class Walnut(Plant, pygame.sprite.Sprite):
    image_path = 'PlantsVsZombies\GamePNGS\Walnut.png'

    def __init__(self, position) -> None:
        Plant.__init__(self, 1440, position, self.image_path)
    
    def set_image(self, path):
        self.image = pygame.image.load(path)
        self.rect = self.image.get_rect(midbottom = self._position)

    def deepcopy(self):
        return Walnut(copy.copy(self._position))