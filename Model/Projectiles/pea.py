from abc import ABC
from Model.Projectiles.projectile import Projectile

class Pea(Projectile, ABC):
    """represents a pea
    """

    def __init__(self, position : tuple[int], dmg : int, path : str) -> None:
        """initializes the pea

        Args:
            position (tuple[int]): the x,y position it will be placed at
            dmg (int): the damage it will deal
            path (str): the path to its image
        """
        Projectile.__init__(self, position, dmg, path)
        ABC.__init__(self)