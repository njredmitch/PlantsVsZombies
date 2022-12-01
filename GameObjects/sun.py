import pygame
import random

class Sun(pygame.sprite.Sprite):
    image_path = 'PlantsVsZombies\GamePNGS\Sun.png'
    def __init__(self, position) -> None:
        super().__init__()
        self._pos = position
        self._image = pygame.image.load(self.image_path)
        self._rect = self.image.get_rect(mid_bottom=position)
    
    def update_position(self, x, y):
        self._pos[0] += x
        self._pos[1] += y
    
    def update_ypos(self):
        self._pos[1] += 1
    
    def is_clicked(self, pos):
        return self._rect.collidepoint(pos)
    
    def set_pos(self, pos):
        if 0 <= random.random < 0.25:
            self._pos = (pos[0] + 20, pos[1] + 90)
        elif 0.25 <= random.random < 0.5:
            self._pos = (pos[0] + 20, pos[1])
        elif 0.25 <= random.random < 0.5:
            self._pos = (pos[0] - 20, pos[1])
        else:
           
            self._pos = (pos[0] + 20, pos[1])
    