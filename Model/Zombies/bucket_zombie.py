from Model.Zombies.zombie import Zombie

class BucketZombie(Zombie):
    """represents a normal zombie wearing a metal bucket
    """
    image_path = 'PlantsVsZombies\GamePNGS\Buckethead.png'

    def __init__(self, position : tuple[int]) -> None:
        """initializes a bucket zombie

        Args:
            position (tuple[int]): the x,y position it will be placed at
        """
        super().__init__(1380, position, 20, BucketZombie.image_path)