from peashooter import Peashooter

class Flameshooter(Peashooter):
    image_path = 'PlantsVsZombies\GamePNGS\Flameshooter.png'
    COST = 200

    def __init__(self, position) -> None:
        Peashooter.__init__(self, position, self.image_path)
        
    @staticmethod
    def get_cost():
        return Flameshooter.COST

    def shoot():
        pass
    