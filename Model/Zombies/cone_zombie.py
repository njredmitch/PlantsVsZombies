from Model.Zombies.zombie import Zombie

class ConeZombie(Zombie):
    """represents a normal zombie wearing a cone
    """
    image_path = 'PlantsVsZombies\GamePNGS\Conehead.png'

    def __init__(self, position : tuple[int]) -> None:
        """intializes the cone zombie

        Args:
            position (tuple[int]): the x,y position it will be placed at
        """
        super().__init__(640, position, 20, ConeZombie.image_path)