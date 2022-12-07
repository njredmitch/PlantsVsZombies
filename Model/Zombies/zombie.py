from abc import ABC
import pygame
import schedule

class ZombieMeta(type(ABC), type(pygame.sprite.Sprite)): pass

class Zombie(ABC, pygame.sprite.Sprite):
    """Represents a Zombie
    """
    __metaclass__ = ZombieMeta

    def __init__(self, health : int, position : tuple[int], dmg : int, path : str) -> None:
        """Initializes the Zombie

        Args:
            health (int): the health of the zombie
            position (tuple[int]): the position of the zombie
            dmg (int): the zombies damage
            path (str): the path to the image of the zombie
        """
        ABC.__init__(self)
        pygame.sprite.Sprite.__init__(self)
        self._health = health
        self._position = position
        self._attack_dmg = dmg
        self._slowed_status = False
        self._movement_status = True
        self.slowed_timer = schedule.Scheduler()
        self.image = pygame.image.load(path)
        self.rect = self.image.get_rect(midbottom = self._position)
        
    def lose_health(self, dmg):
        """decreases the zombies health

        Args:
            dmg (int): the damage taken
        """
        self._health -= dmg

    def run_task(self):
        """runs the task to unfreeze the zombie
        """
        self.slowed_timer.run_pending()

    def get_health(self):
        """gets the zombies health

        Returns:
            int: the health
        """
        return self._health
    
    def get_attack_dmg(self):
        """gets the damage of the zombie

        Returns:
            int: the damage
        """
        return self._attack_dmg
    
    def get_movement_status(self):
        """gets the movmement status of the zombie

        Returns:
            Boolean: True if the zombie can walk, false otherwise
        """
        return self._movement_status
    
    def get_slowed_status(self):
        """gets the slowed status of the zombie

        Returns:
            Boolean: True if the zombie is slowed, False otherwise
        """
        return self._slowed_status
    
    def get_position(self):
        """gets the zombies position

        Returns:
            tuple[int]: the x,y position of the zombie
        """
        return self._position
    
    def get_rect(self):
        """gets the rectangle of the zombie

        Returns:
            Rectangle: the rectangle
        """
        return self.rect

    def update_scheduler(self):
        """clears any jobs stored in the timer and adds a new one to thaw the zombie
        """
        self.slowed_timer.clear()
        self.slowed_timer.every(20).seconds.do(self.thaw)
    
    def thaw(self):
        """sets the zombies slowed status to False
        """
        self._slowed_status = False

    def freeze(self):
        """sets the zombies slowed status to True
        """
        self._slowed_status = True

    def update_xrect(self, x):
        """moves the zombies rectangle to the left

        Args:
            x (int): the amount to move the rectangle
        """
        self.rect.left -= x

    def update_xpos(self, xpos):
        """decreases the xposition of the zombie

        Args:
            xpos (int): the amount to decreases by
        """
        self._position = (self._position[0] - xpos, self._position[1])
    
    def update_ypos(self, ypos):
        """updates the y position of the zombie

        Args:
            ypos (int)): the amount to change it by
        """
        pass
    
    def update_image(self, path):
        """updates the image of the zombie

        Args:
            path (str): the path to the new image
        """
        self.image = pygame.image.load(path)
        self.rect = self.image.get_rect(midbottom=self._position)
        
    def set_movement_status(self, status : bool):
        """sets the movement status of the zombie

        Args:
            status (bool): True to make the zombie move, false to stop the zombie from moving
        """
        self._movement_status = status

    def __str__(self) -> str:
        return f'{self._position}'
   