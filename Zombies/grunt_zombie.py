import pygame
from zombie import Zombie

class GruntZombie(Zombie, pygame.sprite.Sprite):
    image_path = 'PlantsVsZombies\GamePNGS\Zombie.png'

    def __init__(self, position) -> None:
        Zombie(self).__init__(200, position, 10)
        pygame.sprite.Sprite(self).__init__(self)
        self.image = pygame.image.load(self.image_path)
        self.rect = self.image.get_rect(midbottom = self._position)
    
    def draw(self, display: pygame.display):
        pass
