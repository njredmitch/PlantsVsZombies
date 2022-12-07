from Model.Projectiles.pea import  Pea

class IcePea(Pea):
    """represents an ice pea
    """
    image_path = 'PlantsVsZombies\GamePNGS\Icepea.png'
    
    def __init__(self, position : tuple[int]) -> None:
        """initializes the ice pea

        Args:
            position (tuple[int]): the x,y position it will be placed at
        """
        super().__init__(position, 20, IcePea.image_path)