import pygame
from zombie import Zombie

class ConeZombie(Zombie, pygame.sprite.Sprite):
    image_path = 'PlantsVsZombies\GamePNGS\Conehead.png'
    
    def __init__(self, position) -> None:
        Zombie(self).__init__(self, 400, position, 10)
        pygame.sprite.Sprite(self).__init__(self)
        self.image = pygame.image.load(self.image_path)
        self.rect = self.image.get_rect(midbottom = self._position)
    
    def draw(self, display: pygame.display):
        display.blitz
