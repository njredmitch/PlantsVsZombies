import pygame
import random
import sched, time

class Sun(pygame.sprite.Sprite):
    image_path = 'PlantsVsZombies\GamePNGS\Sun.png'
    def __init__(self, position) -> None:
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
    
    def is_clicked(self, pos):
        return self.rect.collidepoint(pos)
    
    def _set_pos(self, pos):
        p = random.sample([(pos[0] + 40, pos[1] - 60),
                           (pos[0] + 40, pos[1] + 30),
                           (pos[0] - 40, pos[1] - 60),
                           (pos[0] - 40, pos[1] + 30)], 1)[0]
        return p
    
    def fade(self):
        self.kill()