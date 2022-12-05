from Model.Zombies.zombie import Zombie

class ConeZombie(Zombie):
    image_path = 'PlantsVsZombies\GamePNGS\Conehead.png'

    def __init__(self, position) -> None:
        super().__init__(640, position, 20, self.image_path)