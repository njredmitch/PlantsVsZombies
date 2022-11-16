import pygame
from plant import Plant

class Walnut(Plant, pygame.sprite.Sprite):
    image_path = 'PlantsVsZombies\GamePNGS\Walnut.png'
    COST = 75

    def __init__(self, position) -> None:
        Plant.__init__(self, 800, position)
        pygame.sprite.Sprite.__init__(self)
        self._image = pygame.image.load(Walnut._image_path)
        self.rect = self.image.get_rect(self._position)
    
    def draw(self):
        pass