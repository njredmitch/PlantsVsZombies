import pygame
from plant import Plant

class Walnut(Plant, pygame.sprite.Sprite):
    _image_path = 'PlantsVsZombies\GamePNGS\Walnut.png'
    _cost = 75

    def __init__(self, health, position) -> None:
        Plant.__init__(400, position)
        pygame.sprite.Sprite.__init__()
        self._image = pygame.image.load(Walnut._image_path).convert_alpha()
        self.rect = self.image.get_rect(self._position)
    
    def draw(self):
        pass