from abc import ABC, abstractmethod

class Plant(ABC):
    
    def __init__(self, health, position, path = '') -> None:
        super().__init__()
        self._health = health
        self._life_state = True
        self._position = position
    
    def lose_health(self, dmg):
        self.set_health(self._health - dmg)
    
    def set_health(self, health):
        self._health = health
    
    def set_life_state(self, state):
        self._life_state = state
    
    def set_position(self, position):
        self._position = position
    
    def get_health(self):
        return self._health
    
    def get_life_state(self):
        return self._life_state
    
    def get_position(self):
        return self._position
    
    @abstractmethod
    def draw(self):
        pass

    
    

    
