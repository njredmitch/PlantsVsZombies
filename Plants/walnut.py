import pygame
from plant import Plant

class Walnut(Plant, pygame.sprite.Sprite):
    image_path = 'PlantsVsZombies\GamePNGS\Walnut.png'
    COST = 75

    def __init__(self, position) -> None:
        Plant.__init__(self, 800, position, self.image_path)
    