import pygame

class ShovelBlock(pygame.sprite.Sprite):
    """represents the block to grab a shovel from
    """
    def __init__(self, pos) -> None:
        """initializes the shovel block

        Args:
            pos (tuple[int]): the x,y coordinate to place the block at
        """
        super().__init__()
        self.image = pygame.image.load('PlantsVsZombies\GamePNGS\Shovel_square.png')
        self.rect = self.image.get_rect(midtop = pos)
        self._shovel = Shovel(pos)

    def get_shovel(self):
        """gets the shovel stored in the block

        Returns:
            Shovel: a copy of the stored shovel
        """
        return self._shovel.copy()
    
    def get_rect(self):
        """gets the rectangle of the block

        Returns:
            Rectangle: the rectangle
        """
        return self.rect

class Shovel(pygame.sprite.Sprite):
    """represents a shovel
    """
    def __init__(self, pos) -> None:
        """initializes the shovel

        Args:
            pos (tuple[int]): the x,y position of the shovel
        """
        super().__init__()
        self.image = pygame.image.load('PlantsVsZombies\GamePNGS\Shovel.png')
        self.rect = self.image.get_rect(midtop = pos)
        self._pos = pos

    def update_pos(self, pos : tuple[int]):
        """updates the shovels position

        Args:
            pos (tuple[int]): the new x,y position of the shovel
        """
        self._pos = pos
    
    def update_rect(self, pos : tuple[int]):
        """updates the position of the shovels rectangle

        Args:
            pos (tuple[int]): the new x,y position of the shovels rectangle
        """
        self.rect.center = pos
    
    def update(self, pos : tuple[int]) -> None:
        """updates the shovels position and rectangle

        Args:
            pos (tuple[int]): the new x,y position
        """
        self.update_pos(pos)
        self.update_rect(pos)
    
    def copy(self):
        """creates a copy of the shovel opject

        Returns:
            Shovel: the shovels copy
        """
        return Shovel(self._pos)