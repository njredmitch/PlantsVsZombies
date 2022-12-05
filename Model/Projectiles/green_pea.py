from Model.Projectiles.pea import  Pea

class GreenPea(Pea):
    image_path = 'PlantsVsZombies\GamePNGS\Greenpea.png'
    
    def __init__(self, position) -> None:
        super().__init__(position, 20, self.image_path)
    