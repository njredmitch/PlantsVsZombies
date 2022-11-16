import pygame
from peashooter import Peashooter

class GreenPeashooter(Peashooter, pygame.sprite.Sprite):
    image_path = 'PlantsVsZombies\GamePNGS\Peashooter.png'
    COST = 100

    def __init__(self, position) -> None:
        Peashooter.__init__(self,position)
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(GreenPeashooter.image_path)
        self.rect = self.image.get_rect(self._position)

    @staticmethod
    def get_cost():
        return GreenPeashooter.COST

    def shoot():
        pass

    def draw(self):
        pass

        