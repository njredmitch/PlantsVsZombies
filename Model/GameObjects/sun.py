import pygame
import random
import sched, time

class Sun(pygame.sprite.Sprite):
    image_path = 'PlantsVsZombies\GamePNGS\Sun.png'
    def __init__(self, position) -> None:
        super().__init__()
        self._pos = self._set_pos(position)
        self._image = pygame.image.load(self.image_path)
        self._rect = self.image.get_rect(mid_bottom=position)
        self.run_lifespan()
        
    def run_lifespan(self):
        s = sched.scheduler(time.time, time.sleep)
        s.add(25, None, self.fade)
        s.run()

    def update_position(self, x, y):
        self._pos[0] += x
        self._pos[1] += y
    
    def update_ypos(self):
        self._pos[1] += 1
    
    def is_clicked(self, pos):
        return self._rect.collidepoint(pos)
    
    def _set_pos(self, pos):
        p = random.sample([(pos[0] + 20, pos[1] - 90),
                           (pos[0] + 20, pos[1]),
                           (pos[0] - 20, pos[1] - 90),
                           (pos[0] - 20, pos[1])])[0]
        self._pos = p
    
    def fade(self):
        self.kill()