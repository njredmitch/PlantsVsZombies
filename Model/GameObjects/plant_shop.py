import pygame
import schedule

class PlantShop(pygame.sprite.Sprite):

    def __init__(self, path : str, cpath : str, pos : tuple[int], cost :  int, plant, refresh : int, status : bool):
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
        self._open = False
        self.image = pygame.image.load(self._closed_path)
        self.rect = self.image.get_rect(midleft=self.pos)
        self._closed_timer.clear()
        self._closed_timer.every(self._refresh_time).seconds.do(self.open)
    
    def open(self):
        self._open = True
        self.image = pygame.image.load(self._open_path)
        self.rect = self.image.get_rect(midleft=self.pos)

    def is_open(self):
        return self._open

    def run_event(self):
        self._closed_timer.run_pending()

    def get_rect(self):
        return self.rect

    def get_cost(self):
        return self._cost
    
    def get_plant(self):
        return self._plant
    
    def __str__(self) -> str:
        return f'{self._cost}'