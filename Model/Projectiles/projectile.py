from abc import ABC
import pygame

class ProjectileMeta(type(ABC), type(pygame.sprite.Sprite)): pass

class Projectile(ABC, pygame.sprite.Sprite):
    """Represents a projectile
    """
    __metaclass__=ProjectileMeta
    def __init__(self, position : tuple[int], dmg : int, path  : str) -> None:
        """initializes the projectile

        Args:
            position (tuple[int]): the x,y position it will be placed at
            dmg (int): the damage it deals
            path (str): the path to its image
        """
        ABC.__init__(self)
        pygame.sprite.Sprite.__init__(self)
        self._dmg = dmg
        self._position = position
        self.image = pygame.image.load(path)
        self.rect = self.image.get_rect(midleft = self._position)
    
    def get_pos(self):
        """returns its position

        Returns:
            tuple[int]: its x,y position
        """
        return self._position

    def update_xpos(self, x):
        """increases the x position

        Args:
            x (int): the amount to increase the position
        """
        self._position = (self._position[0] + x, self._position[1])
    
    def update_ypos(self):
        """updates the y position
        """
        pass

    def get_dmg(self):
        """gets its damage

        Returns:
            int: projectile's damage
        """
        return self._dmg
    
    def get_rect(self):
        """gets the projectiles rectangle

        Returns:
            Rectangle: its rectangle
        """
        return self.rect