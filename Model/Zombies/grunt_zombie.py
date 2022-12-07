from Model.Zombies.zombie import Zombie

class GruntZombie(Zombie):
    """represents a normal zombie
    """
    image_path = 'PlantsVsZombies\GamePNGS\Zombie.png'

    def __init__(self, position : tuple[int]) -> None:
        """initializes the normal zombie

        Args:
            position (tuple[int]): the x,y position it will be placed at
        """
        super().__init__(200, position, 20, GruntZombie.image_path)