import schedule

from abc import ABC, abstractmethod
from plant import Plant

class Peashooter(Plant, ABC):
    peas = {}

    def __init__(self, position, path) -> None:
        super().__init__(200, position, path)
        self._event_manager = schedule
    
    def shoot_peas(self):
        self._event_manager.every(20).seconds.do(self.shoot())

    def stop_shooting(self):
        self._event_manager.clear()
        
    @abstractmethod
    def shoot(self):
        pass


    
    
    