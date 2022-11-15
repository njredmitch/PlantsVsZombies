import pygame
from plant import Plant
import schedule

class Sunflower(Plant, pygame.sprite.Sprite):
    image_path = 'PlantsVsZombies\GamePNGS\Sunflower.png'
    cost = 50
    sun_container = []
    
    def __init__(self, position) -> None:
        Plant.__init__(200, position)
        pygame.sprite.Sprite.__init__()
        self._event_scheduler = schedule
        self._event_scheduler.every(20).seconds.do(self.produce_sun())
        self._surf = pygame.image.load(Sunflower.image_path).convert_alpha()
        self._rect = self.image.get_rect(self._position)

    def produce_sun(self):
        print('making sun')
    
    def draw(self, screen: pygame.display):
        screen.blitz(self.rect)
    




