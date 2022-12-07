import pygame
import copy
from Model.Plants.plant import Plant

class Walnut(Plant):
    """represents a walnut
    """
    image_path = 'PlantsVsZombies\GamePNGS\Walnut.png'

    def __init__(self, position : tuple[int]) -> None:
        """intializes the walnut

        Args:
            position (tuple[int]): the x,y position it will be placed at
        """
        Plant.__init__(self, 1440, position, self.image_path)
    
    def set_image(self, path):
        """updates the image to a new one

        Args:
            path (str): the path to the new image
        """
        self.image = pygame.image.load(path)
        self.rect = self.image.get_rect(midbottom = self._position)

    def deepcopy(self):
        """creates a deep copy of itself

        Returns:
            Walnut: its copy
        """
        return Walnut(copy.copy(self._position))