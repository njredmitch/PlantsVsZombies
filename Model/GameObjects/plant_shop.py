import pygame
import schedule

class PlantShop(pygame.sprite.Sprite):
    """Represents a shop for a plant
    """

    def __init__(self, path : str, cpath : str, pos : tuple[int], cost :  int, plant, refresh : int, status : bool):
        """initializes the plant shop

        Args:
            path (str): the path to the image of the opened shop
            cpath (str): the path to the image of the closed shop
            pos (tuple[int]): the  position of the shop
            cost (int): the cost of the plant in the shop
            plant (Plant): the plant to be purchased
            refresh (int): the time the shop will be closed for after a purchase is made
            status (bool): status of the shop True for open, False for closed
        """
        super().__init__()
        self._open_path = path
        self._closed_path = cpath
        self._refresh_time = refresh
        self.pos = pos
        self._cost = cost
        self._plant = plant
        self._open = status
        self._closed_timer = schedule.Scheduler()
        if status:
            self.image = pygame.image.load(path)
            self._closed_timer.every(refresh).seconds.do(self.open)
        else:
            self.image = pygame.image.load(cpath)
        self.rect = self.image.get_rect(midleft=pos)

    def close(self):
        """closes the shop, changing the image and activating the timer that reopens it
        """
        self._open = False
        self.image = pygame.image.load(self._closed_path)
        self.rect = self.image.get_rect(midleft=self.pos)
        self._closed_timer.clear()
        self._closed_timer.every(self._refresh_time).seconds.do(self.open)
    
    def open(self):
        """opens the shop and changes the image
        """
        self._open = True
        self.image = pygame.image.load(self._open_path)
        self.rect = self.image.get_rect(midleft=self.pos)

    def is_open(self):
        """checks if the shop is open

        Returns:
            Boolean: True if open, False if closed
        """
        return self._open

    def run_event(self):
        """Runs the event to re-open the shop, that isstored in the timer
        """
        self._closed_timer.run_pending()

    def get_rect(self):
        """gets the rectangle of the shop

        Returns:
            Rectangle: the rectangle of the shop
        """
        return self.rect

    def get_cost(self):
        """gets the cost of the plant

        Returns:
            int: the cost of the plant
        """
        return self._cost
    
    def get_plant(self):
        """gets the plant that is purchasable from the shop

        Returns:
            Plant: the purchased plant 
        """
        return self._plant
    
    def __str__(self) -> str:
        return f'{self._cost}'