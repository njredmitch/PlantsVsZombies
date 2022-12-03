from Model.Zombies.zombie import Zombie

class ConeZombie(Zombie):
    image_path = 'PlantsVsZombies\GamePNGS\Conehead.png'

    def __init__(self, position) -> None:
        super().__init__(self, 400, position, 10, self.image_path)