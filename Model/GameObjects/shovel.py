import pygame

class ShovelBlock(pygame.sprite.Sprite):

    def __init__(self, pos) -> None:
        super().__init__()
        self.image = pygame.image.load('PlantsVsZombies\GamePNGS\Shovel_square.png')
        self.rect = self.image.get_rect(midtop = pos)
        self._shovel = Shovel(pos)

    def get_shovel(self):
        return self._shovel.copy()
    
    def get_rect(self):
        return self.rect

class Shovel(pygame.sprite.Sprite):

    def __init__(self, pos) -> None:
        super().__init__()
        self.image = pygame.image.load('PlantsVsZombies\GamePNGS\Shovel.png')
        self.rect = self.image.get_rect(midtop = pos)
        self._pos = pos

    def update_pos(self, pos):
        self._pos = pos
    
    def update_rect(self, pos):
        self.rect.center = pos
    
    def update(self, pos) -> None:
        self.update_pos(pos)
        self.update_rect(pos)
    
    def copy(self):
        return Shovel(self._pos)