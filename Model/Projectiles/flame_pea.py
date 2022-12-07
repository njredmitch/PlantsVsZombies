from Model.Projectiles.pea import  Pea

class FlamePea(Pea):
    """represents a flame pea
    """
    image_path = 'PlantsVsZombies\GamePNGS\Flamepea.png'
    
    def __init__(self, position : tuple[int]) -> None:
        """initializes the flame pea

        Args:
            position (tuple[int]): the x,y position it will be placed at
        """
        super().__init__(position, 40, FlamePea.image_path)