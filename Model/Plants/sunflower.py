import pygame
import schedule

from Model.Plants.plant import Plant
from Model.GameObjects.sun import Sun


class Sunflower(Plant, pygame.sprite.Sprite):
    image_path = 'PlantsVsZombies\GamePNGS\Sunflower.png'
    sun_group = pygame.sprite.Group
    
    def __init__(self, position) -> None:
        Plant.__init__(self, 200, position, self.image_path)
        pygame.sprite.Sprite.__init__(self)
        self._event_scheduler = schedule.default_scheduler
        self._event_scheduler.every(20).seconds.do(self.produce_sun())

    def produce_sun(self):
        Sunflower.sun_group.add(Sun(self._position))
    
    def run_event(self):
        self._event_scheduler.run_pending()