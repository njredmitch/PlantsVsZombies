from pea import  Pea

class IcePea(Pea):
    image_path = 'PlantsVsZombies\GamePNGS\Icepea.png'
    
    def __init__(self, position) -> None:
        super().__init__(position, 10, self.image_path)