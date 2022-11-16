import pygame
from plant import Plant
import schedule

class Sunflower(Plant, pygame.sprite.Sprite):
    image_path = 'PlantsVsZombies\GamePNGS\Sunflower.png'
    COST = 50
    sun_container = []
    
    def __init__(self, position) -> None:
        Plant.__init__(self, 200, position, self.image_path)
        pygame.sprite.Sprite.__init__(self)
        self._event_scheduler = schedule
        self._event_scheduler.every(20).seconds.do(self.produce_sun())

    def produce_sun(self):
        print('making sun')
    
    




