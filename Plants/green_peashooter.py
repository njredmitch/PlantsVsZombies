from peashooter import Peashooter
from Projectiles.green_pea import GreenPea

class GreenPeashooter(Peashooter):
    image_path = 'PlantsVsZombies\GamePNGS\Peashooter.png'
    COST = 100

    def __init__(self, position) -> None:
        Peashooter.__init__(self, position, self.image_path)

    @staticmethod
    def get_cost():
        return GreenPeashooter.COST

    def shoot():
        pass

    def pos_to_pea_pos(self):
        pass
        