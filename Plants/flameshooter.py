import pygame
from peashooter import Peashooter

class Flameshooter(Peashooter, pygame.sprite.Sprite):
    image_path = 'PlantsVsZombies\GamePNGS\Flameshooter.png'
    COST = 200

    def __init__(self, position) -> None:
        Peashooter.__init__(self, position)
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(Flameshooter.image_path)
        self.rect = self.image.get_rect(midbottom = self._position)
        
    @staticmethod
    def get_cost():
        return Flameshooter.COST

    def shoot():
        pass

    def draw(self):
        pass

    