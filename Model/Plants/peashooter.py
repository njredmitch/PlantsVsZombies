import schedule
import pygame

from abc import ABC, abstractmethod
from Model.Plants.plant import Plant

class Peashooter(Plant, ABC):
    """Represents a Peashooter plant
    """
    peas = pygame.sprite.Group()

    def __init__(self, position : tuple[int], path : str) -> None:
        """initializes the peashooter

        Args:
            position (tuple[int]): the x,y position the peashooter will be placed at
            path (str): the path to the peashooters image
        """
        super().__init__(120, position, path)
        self._event_manager = schedule.Scheduler()
        self._event_manager.every(2).seconds.do(self.shoot)
        self._primed = False
    
    def shoot_peas(self):
        """runs the event to fire shots stored in the event_manager
        """
        self._event_manager.run_pending()

    def prime(self):
        """primes the peashooter to shoot setting its primed status to True
        """
        self._primed = True

    def unprime(self):
        """unprimes the peashooter setting its primed status to False
        """
        self._primed = False

    def is_primed(self):
        """checks if the peashooter is primed

        Returns:
            bool: True if primed, False otherwise
        """
        return self._primed
    
    @abstractmethod
    def shoot(self):
        """shoots a pea onto the yard
        """
        pass
    
    


    
    