import pygame
import schedule

from abc import ABC, abstractmethod
from plant import Plant

class Peashooter(Plant, ABC):
    peas = {}

    def __init__(self, position) -> None:
        super().__init__(200, position)
        self._event_manager = schedule
        self._shoot_state = False
        
    def set_shoot_state(self, state):
        self._shoot_state = state
    
    def get_shoot_state(self):
        return self._shoot_state
    
    def shoot_peas(self):
        self._event_manager.every(20).seconds.do(self.shoot())

    @abstractmethod
    def shoot(self):
        pass

    
    
    