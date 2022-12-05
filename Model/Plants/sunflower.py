import pygame
import schedule
import copy

from Model.Plants.plant import Plant
from Model.GameObjects.sun import Sun


class Sunflower(Plant):
    image_path = 'PlantsVsZombies\GamePNGS\Sunflower.png'
    sun_group = pygame.sprite.Group()
    
    def __init__(self, position) -> None:
        super().__init__(120, position, Sunflower.image_path)
        self._event_scheduler = schedule.Scheduler()
        self._event_scheduler.every(24).seconds.do(self.produce_sun)

    def produce_sun(self):
        Sunflower.sun_group.add(Sun(self._position))
    
    def run_event(self):
        self._event_scheduler.run_pending()
    
    def deepcopy(self):
        return Sunflower(copy.copy(self._position))