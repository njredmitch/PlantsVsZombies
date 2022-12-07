from abc import ABC
import pygame

class PlantMeta(type(ABC), type(pygame.sprite.Sprite)): pass

class Plant(ABC, pygame.sprite.Sprite):
    """represents a plant
    """
    __metaclass__=PlantMeta
    def __init__(self, health : int, position : tuple[int], path : str) -> None:
        """initializes the plant

        Args:
            health (int): the health of the plant
            position (tuple[int]): the x,y of the plant
            path (str): path to the plants image
        """
        ABC.__init__(self)
        pygame.sprite.Sprite.__init__(self)
        self._health = health
        self._position = position
        self.image = pygame.image.load(path)
        self.rect = self.image.get_rect(midbottom=self._position)

    def lose_health(self, dmg):
        """makes the plant take damage

        Args:
            dmg (int): the damage taken
        """
        self._health -= dmg

    def set_position(self, position):
        """updates the position of the plant to the given one

        Args:
            position (tuple[x,y]): the new x,y position of the plant
        """
        self._position = position
    
    def get_rect(self):
        """gets the plants rectangle

        Returns:
            Rectangle: the rectangle of the plant
        """
        return self.rect

    def get_health(self):
        """gets the plant's health

        Returns:
            int: the health
        """
        return self._health
    
    def get_position(self):
        """gets the plants position

        Returns:
            tuplep[int]: the plants current x,y position
        """
        return self._position

    def __str__(self) -> str:
        return f'{self._health}, {self._position}'
    