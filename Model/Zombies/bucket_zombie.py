from Model.Zombies.zombie import Zombie

class BucketZombie(Zombie):
    image_path = 'PlantsVsZombies\GamePNGS\Buckethead.png'

    def __init__(self, position) -> None:
        super().__init__(1380, position, 20, self.image_path)