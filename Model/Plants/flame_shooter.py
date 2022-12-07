from Model.Plants.peashooter import Peashooter
from Model.Projectiles.flame_pea import FlamePea
import copy

class Flameshooter(Peashooter):
    """represents a peashooter that shoots flame peas
    """
    image_path = 'PlantsVsZombies\GamePNGS\Flameshooter.png'

    def __init__(self, position : tuple[int]) -> None:
        """initializes the flameshooter

        Args:
            position (tule[int]): the x,y position where it will be placed
        """
        Peashooter.__init__(self, position, self.image_path)

    def shoot(self):
        """shoots a flame pea onto the yard
        """
        self.peas.add(FlamePea(self.make_pea_pos()))

    def make_pea_pos(self):
        """makes the position where it shoots flame peas at

        Returns:
            tuple[int]: the x,y position where the pea will be placed
        """
        return (self._position[0] + 20, self._position[1] - 75)
    
    def deepcopy(self):
        """creates a deep copy of itself

        Returns:
            Flameshooter: the copy
        """
        return Flameshooter(copy.copy(self._position))