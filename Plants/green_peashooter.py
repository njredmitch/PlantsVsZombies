import pygame
from peashooter import Peashooter

class GreenPeashooter(Peashooter, pygame.sprite.Sprite):
    image_path = 'PlantsVsZombies\GamePNGS\Peashooter.png'
    _cost = 100

    def __init__(self, position) -> None:
        Peashooter.__init__(position)
        pygame.sprite.Sprite.__init__()
        self.image = pygame.image.load(GreenPeashooter.image_path).convert_alpha()
        self.rect = self.image.get_rect(self._position)

    @staticmethod
    def get_cost(self):
        return GreenPeashooter._cost

    def shoot():
        pass

        