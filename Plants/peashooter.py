import schedule
import pygame

from abc import ABC, abstractmethod
from plant import Plant

class Peashooter(Plant, ABC):
    peas = pygame.sprite.Group  

    def __init__(self, position, path) -> None:
        super().__init__(200, position, path)
        self._event_manager = schedule
        self._primed = False
    
    def shoot_peas(self):
        self._event_manager.every(2).seconds.do(self.shoot())
        self._primed = True

    def stop_shooting(self):
        self._event_manager.clear()
        self._primed = False

    def get_primed(self):
        return self._primed
    
    @abstractmethod
    def shoot(self):
        pass



    
    