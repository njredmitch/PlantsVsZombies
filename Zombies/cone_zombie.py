import pygame
import schedule
from zombie import Zombie

class ConeZombie(Zombie, pygame.sprite.Sprite):
    image_path = 'PlantsVsZombies\GamePNGS\Conehead.png'

    def __init__(self, position) -> None:
        Zombie(self).__init__(self, 400, position, 10)
        pygame.sprite.Sprite(self).__init__(self)
        self.image = pygame.image.load(self.image_path)
        self.rect = self.image.get_rect(midbottom = self._position)
        self._event_schedule = schedule
        self.plant_to_attack = None
    def draw(self, display: pygame.display):
        display.blitz

    def attack(self, plant):
        self.plant_to_attack = plant
        self._event_schedule.every(5).seconds.do(self.attack_plant())

    def attack_plant(self):
        self.plant_to_attack.lose_health(self._attack_dmg)

    def convert_image(self):
        self.image.convert_alpha()
    
    def update_plant(self):
        self.plant_to_attack = None