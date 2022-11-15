import pygame
from plant import Plant
import schedule

class Sunflower(Plant, pygame.sprite.Sprite):
    path = 'PlantsVsZombies\GamePNGS\Sunflower.png'
    cost = 50
    sun_container = []
    
    def __init__(self, position) -> None:
        super().__init__(200, position)
        self._event_scheduler = schedule
        self._event_scheduler.every(20).seconds().do(self.produce_sun())
        self._surf = pygame.image.load(Sunflower.path).convert_alpha()
        self._rect = pygame.rect(self.surf, self._position)

    def produce_sun(self):
        print('making sun')
    
    def draw(self, screen: pygame.display):
        screen.blitz(self.rect)
    




