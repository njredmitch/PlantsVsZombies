import schedule
import pygame

from abc import ABC, abstractmethod
from Model.Plants.plant import Plant

class Peashooter(Plant, ABC):
    peas = pygame.sprite.Group  

    def __init__(self, position, path) -> None:
        super().__init__(200, position, path)
        self._event_manager = schedule.default_scheduler
        self._event_manager.every(2).seconds.do(self.shoot())
        self._primed = False
    
    def shoot_peas(self):
        self._event_manager.run_pending()

    def prime(self):
        self._primed = True

    def unprime(self):
        self._primed = False

    def is_primed(self):
        return self._primed
    
    @abstractmethod
    def shoot(self):
        pass



    
    