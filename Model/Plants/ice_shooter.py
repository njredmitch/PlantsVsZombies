from Model.Plants.peashooter import Peashooter
from Model.Projectiles.ice_pea import IcePea
import copy

class Iceshooter(Peashooter):
    """Represents an Peashooter that slows attacked zombies
    """
    image_path = 'PlantsVsZombies\GamePNGS\Iceshooter.png'

    def __init__(self, position : tuple[int]) -> None:
        """initializes the Iceshooter

        Args:
            position (tuple[int]): the x,y position to place the iceshooter at
        """
        Peashooter.__init__(self, position, self.image_path)
    
    def shoot(self):
        """shoots an IcePea onto the yard
        """
        self.peas.add(IcePea(self.make_pea_pos()))

    def make_pea_pos(self):
        """creates the position where it will shoot peas at

        Returns:
            tuple[int]: the x,y position to shoot icepeas at
        """
        return (self._position[0] + 25, self._position[1] - 75)

    def deepcopy(self):
        """creates a deep copy of itself

        Returns:
            IceShooter: the copy
        """
        return Iceshooter(copy.copy(self._position))