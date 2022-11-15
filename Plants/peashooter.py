import pygame
import schedule

from abc import ABC, abstractmethod
from plant import Plant

class Peashooter(Plant, ABC):
    peas = {}

    def __init__(self, position) -> None:
        super().__init__(200, position)
        self._event_manager = schedule
        self._event_manager.every(10).second.do(self.shoot())
    
    @abstractmethod
    def shoot(self):
        pass
    
    