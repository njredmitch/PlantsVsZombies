from peashooter import Peashooter
from Projectiles.flame_pea import FlamePea

class Flameshooter(Peashooter):
    image_path = 'PlantsVsZombies\GamePNGS\Flameshooter.png'
    COST = 200

    def __init__(self, position) -> None:
        Peashooter.__init__(self, position, self.image_path)
        
    @staticmethod
    def get_cost():
        return Flameshooter.COST

    def shoot(self):
        pass

    def pos_to_pea_pos(self):
        pass
