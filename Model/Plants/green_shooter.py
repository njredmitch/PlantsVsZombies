from Model.Plants.peashooter import Peashooter
from Model.Projectiles.green_pea import GreenPea
import copy

class GreenPeashooter(Peashooter):
    """represents a peashooter that shoots normal peas
    """
    image_path = 'PlantsVsZombies\GamePNGS\Peashooter.png'


    def __init__(self, position : tuple[int]) -> None:
        """initializes the green peashooter

        Args:
            position (tuple[int]): the x,y position to place the greenpeashooter at
        """
        Peashooter.__init__(self, position, self.image_path)

    def shoot(self):
        """shoots a green pea onto the yard
        """
        self.peas.add(GreenPea(self.make_pea_pos()))

    def make_pea_pos(self):
        """makes an x,y position where it shoots peas from

        Returns:
            tuple[int]: the x,y position where the pea will be placed
        """
        return (self._position[0] + 30, self._position[1] - 75)
    
    def deepcopy(self):
        """creates a deep copy of itself

        Returns:
            GreenPeashooter: the copy
        """
        return GreenPeashooter(copy.copy(self._position))