from Model.Plants.peashooter import Peashooter
from Model.Projectiles.green_pea import GreenPea

class GreenPeashooter(Peashooter):
    image_path = 'PlantsVsZombies\GamePNGS\Peashooter.png'


    def __init__(self, position) -> None:
        Peashooter.__init__(self, position, self.image_path)

    @staticmethod
    def get_cost():
        return GreenPeashooter.COST

    def shoot(self):
        self.peas.add(GreenPea(self.make_pea_pos()))


    def meke_pea_pos(self):
        return (self._position[0] + 30, self._position[1] - 75)
        