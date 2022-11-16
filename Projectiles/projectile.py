from abc import ABC, abstractmethod

class Projectile(ABC):

    def __init__(self, position, dmg) -> None:
        super().__init__()
        self._dmg = dmg
        self._position = position
    
    def update_xpos(self):
        self._position[0] += 1
    
    def update_ypos(self):
        pass

    def get_dmg(self):
        return self._dmg
    
    @abstractmethod
    def draw(self, display):
        pass