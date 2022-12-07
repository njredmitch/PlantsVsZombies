from Model.Projectiles.pea import  Pea

class GreenPea(Pea):
    """represents a green pea
    """
    image_path = 'PlantsVsZombies\GamePNGS\Greenpea.png'
    
    def __init__(self, position : tuple[int]) -> None:
        """initializes the green pea

        Args:
            position (tuple[int]): the x,y position it will  be placed at
        """
        super().__init__(position, 20, GreenPea.image_path)
    