from abc import ABC
import pygame
import schedule

class ZombieMeta(type(ABC), type(pygame.sprite.Sprite)): pass

class Zombie(ABC, pygame.sprite.Sprite):
    __metaclass__ = ZombieMeta
    def __init__(self, health, position, dmg, path) -> None:
        ABC.__init__(self)
        pygame.sprite.Sprite.__init__(self)
        self._health = health
        self._position = position
        self._attack_dmg = dmg
        self._life_state = True
        self._slowed_status = False
        self._movement_status = True
        self.slowed_timer = schedule.Scheduler()
        self.image = pygame.image.load(path)
        self.rect = self.image.get_rect(midbottom = self._position)
        
    def lose_health(self, dmg):
        self._health -= dmg

    def run_task(self):
        self.slowed_timer.run_pending()

    def get_health(self):
        return self._health
    
    def get_attack_dmg(self):
        return self._attack_dmg
    
    def get_movement_status(self):
        return self._movement_status
    
    def get_slowed_status(self):
        return self._slowed_status
    
    def get_life_state(self):
        return self._life_state
    
    def get_position(self):
        return self._position
    
    def get_rect(self):
        return self.rect

    def update_scheduler(self):
        self.slowed_timer.clear()
        self.slowed_timer.every(20).seconds.do(self.thaw)
    
    def thaw(self):
        self._slowed_status = False

    def freeze(self):
        self._slowed_status = True

    def update_xrect(self, x):
        self.rect.left -= x

    def update_xpos(self, xpos):
        self._position = (self._position[0] - xpos, self._position[1])
    
    def update_ypos(self, ypos):
        self._position[1] = ypos
    
    def update_image(self, path):
        self.image = pygame.image.load(path)
        self.rect = self.image.get_rect(midbottom=self._position)
        
    def set_life_state(self, state):
        self._life_state = state
    
    def set_movement_status(self, status):
        self._movement_status = status

    def __str__(self) -> str:
        return f'{self._position}'
   