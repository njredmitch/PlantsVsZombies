from abc import ABC
import schedule
import pygame

class Zombie(ABC, pygame.sprite.Sprite):

    def __init__(self, health, position, dmg, path) -> None:
        ABC.__init__(self)
        pygame.sprite.Sprite.__init__(self)
        self._health = health
        self._position = position
        self._attack_dmg = dmg
        self._life_state = True
        self._slowed_status = False
        self._movement_status = True
        self._event_schedule = schedule
        self._plant_to_attack = None
        self.image = pygame.image.load(path)
        self.rect = self.image.get_rect(midbottom = self._position)
        
    def lose_health(self, dmg):
        self._health -= dmg

    def draw(self, display: pygame.display):
        display.blitz()

    def attack(self, plant):
        self._movement_status = False
        self.plant_to_attack = plant
        self._event_schedule.every(5).seconds.do(self.attack_plant())

    def attack_plant(self):
        self.plant_to_attack.lose_health(self._attack_dmg)

    def convert_image(self):
        self.image.convert_alpha()
    
    def stop_attacking(self):
        self._plant_to_attack = None
        self._movement_status = True
        self._event_schedule.clear()
    
    def get_plant(self):
        return self._plant_to_attack

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
    
    def update_xpos(self, xpos):
        self._position[0] = xpos
    
    def update_ypos(self, ypos):
        self._position[1] = ypos
    
    def set_life_state(self, state):
        self._life_state = state
    
    def set_movement_status(self, status):
        self._movement_status = status
    
    def set_slowed_status(self, status):
        self._slowed_status = status
    
   