from Model.Projectiles.pea import  Pea

class FlamePea(Pea):
    image_path = 'PlantsVsZombies\GamePNGS\Flamepea.png'
    
    def __init__(self, position) -> None:
        super().__init__(position, 40, self.image_path)