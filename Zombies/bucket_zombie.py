import pygame
import schedule

from zombie import Zombie

class BucketZombie(Zombie, pygame.sprite.Sprite):
    image_path = 'PlantsVsZombies\GamePNGS\Buckethead.png'

    def __init__(self, position) -> None:
        Zombie().__init__(self, 600, position, 10)
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(self.image_path)
        self.rect = self.image.get_rect(midbottom = self._position)
        self._event_schedule = schedule
        self._plant_to_attack = None

    def draw(self, display: pygame.display):
        display.blit(self.rect)
    
    def attack(self, plant):
        self._plant_to_attack = plant
        self._event_schedule.every(5).seconds.do(self.attack_plant())

    def attack_plant(self):
        self._plant_to_attack.lose_health(self._attack_dmg)

    def convert_image(self):
        self.image.convert_alpha()
    
    def update_plant(self):
        self._plant_to_attack = None
    
    def stop_attacking(self):
        self._event_schedule.clear()