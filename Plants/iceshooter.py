from peashooter import Peashooter

class Iceshooter(Peashooter):
    image_path = 'PlantsVsZombies\GamePNGS\Icehooter.png'
    COST = 175

    def __init__(self, position) -> None:
        Peashooter.__init__(self, position, self.image_path)
        
    @staticmethod
    def get_cost():
        return Iceshooter.COST
    
    def shoot():
        pass