from Model.Plants.peashooter import Peashooter
from Model.Projectiles.ice_pea import IcePea

class Iceshooter(Peashooter):
    image_path = 'PlantsVsZombies\GamePNGS\Icehooter.png'

    def __init__(self, position) -> None:
        Peashooter.__init__(self, position, self.image_path)
    
    def shoot(self):
        self.peas.add(IcePea(self.make_pea_pos()))

    def make_pea_pos(self):
        return (self._position[0] + 25, self._position[1] - 75)