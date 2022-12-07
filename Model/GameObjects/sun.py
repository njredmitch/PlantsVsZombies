import pygame
import random

class Sun(pygame.sprite.Sprite):
    """represents Sun
    """
    image_path = 'PlantsVsZombies\GamePNGS\Sun.png'
    def __init__(self, position : tuple[int]) -> None:
        """initializes the sun

        Args:
            position (tuple[int]): the x,y position of the sunflower that made it
        """
        super().__init__()
        self._pos = self._set_pos(position)
        self.image = pygame.image.load(Sun.image_path)
        self.rect = self.image.get_rect(midbottom=self._pos)
        
    def run_lifespan(self):
        pass

    def update_position(self, x, y):
        pass
    
    def update_ypos(self):
        pass
    
    def is_clicked(self, pos : tuple[int]):
        """checks if the sun was clicked on

        Args:
            pos (tuple[int]): the x,y position of the mouse

        Returns:
            bool: True if clicked on, false otherwise
        """
        return self.rect.collidepoint(pos)
    
    def _set_pos(self, pos):
        """sets the position of the sun upon initialization 
        to one of 4 random spots

        Args:
            pos (tuple[int]): the x,y position of the sunflower that created it

        Returns:
            tuple[int]: the x,y position of sun
        """
        p = random.sample([(pos[0] + 40, pos[1] - 60),
                           (pos[0] + 40, pos[1] + 30),
                           (pos[0] - 40, pos[1] - 60),
                           (pos[0] - 40, pos[1] + 30)], 1)[0]
        return p
    
    def fade(self):
        """removes the sun from the yard
        """
        self.kill()