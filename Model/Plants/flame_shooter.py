from Model.Plants.peashooter import Peashooter
from Model.Projectiles.flame_pea import FlamePea
import copy

class Flameshooter(Peashooter):
    image_path = 'PlantsVsZombies\GamePNGS\Flameshooter.png'

    def __init__(self, position) -> None:
        Peashooter.__init__(self, position, self.image_path)
        
    @staticmethod
    def get_cost():
        return Flameshooter.COST

    def shoot(self):
        self.peas.add(FlamePea(self.make_pea_pos()))

    def make_pea_pos(self):
        return (self._position[0] + 20, self._position[1] - 75)
    
    def deepcopy(self):
        return Flameshooter(copy.copy(self._position))