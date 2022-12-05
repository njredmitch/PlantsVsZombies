from Model.Zombies.zombie import Zombie

class GruntZombie(Zombie):
    image_path = 'PlantsVsZombies\GamePNGS\Zombie.png'

    def __init__(self, position) -> None:
        super().__init__(200, position, 20, self.image_path)