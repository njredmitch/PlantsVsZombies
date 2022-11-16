import pygame
from peashooter import Peashooter

class Iceshooter(Peashooter, pygame.sprite.Sprite):
    image_path = 'PlantsVsZombies\GamePNGS\Icehooter.png'
    COST = 175

    def __init__(self, position) -> None:
        Peashooter.__init__(position)
        pygame.sprite.Sprite.__init__()
        self.image = pygame.image.load(Iceshooter.image_path)
        self.rect = self.image.get_rect(self._position)
        
    @staticmethod
    def get_cost():
        return Iceshooter.COST
    
    def shoot():
        pass

    def draw(self):
        pass