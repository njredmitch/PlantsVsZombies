import pygame

class PlantShop(pygame.sprite.Sprite):

    def __init__(self, path, pos, cost, plant):
        super().__init__()
        self.image = pygame.image.load(path)
        self.rect = self.image.get_rect(midleft=pos)
        self._cost = cost
        self._plant = plant
    
    def get_rect(self):
        return self.rect

    def get_cost(self):
        return self._cost
    
    def get_plant(self):
        return self._plant
    
    def __str__(self) -> str:
        return f'{self._cost}'