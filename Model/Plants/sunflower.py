import pygame
import schedule
import copy

from Model.Plants.plant import Plant
from Model.GameObjects.sun import Sun


class Sunflower(Plant):
    """represents a sunflower
    """
    image_path = 'PlantsVsZombies\GamePNGS\Sunflower.png'
    sun_group = pygame.sprite.Group()
    
    def __init__(self, position : tuple[int]) -> None:
        """initializes the sunflower

        Args:
            position (tuple[int]): the x,y position it will be placed at
        """
        super().__init__(120, position, Sunflower.image_path)
        self._event_scheduler = schedule.Scheduler()
        self._event_scheduler.every(24).seconds.do(self.produce_sun)

    def produce_sun(self):
        """adds sun to the yard
        """
        Sunflower.sun_group.add(Sun(self._position))
    
    def run_event(self):
        """runs the produce_sun method stored in its event_scheduler
        """
        self._event_scheduler.run_pending()
    
    def deepcopy(self):
        """creates a deep copy of the object

        Returns:
            Sunflower: the copy
        """
        return Sunflower(copy.copy(self._position))