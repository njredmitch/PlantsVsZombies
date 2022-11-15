import pygame
from peashooter import Peashooter

class Flameshooter(Peashooter, pygame.sprite.Sprite):
    image_path = 'PlantsVsZombies\GamePNGS\Flameshooter.png'
    _cost = 200

    def __init__(self, position) -> None:
        Peashooter.__init__(position)
        pygame.sprite.Sprite.__init__()
        self.image = pygame.image.load(Flameshooter.image_path).convert_alpha()
        self.rect = self.image.get_rect(self._position)
        
    @staticmethod
    def get_cost():
        return Flameshooter._cost

    def shoot():
        pass

    def draw(self):
        pass