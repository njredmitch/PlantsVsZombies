import pygame

class Sun(pygame.sprite.Sprite):
    image_path = 'PlantsVsZombies\GamePNGS\Sun.png'
    def __init__(self, position) -> None:
        super().__init__()
        self._pos = position
        self._value = 25
        self._image = pygame.image.load(self.image_path)
        self._rect = self.image.get_rect(mid_bottom=position)
    
    def get_value(self):
        return self._value
    
    def update_position(self, x, y):
        self._pos[0] += x
        self._pos[1] += y
    
    def update_ypos(self):
        self._pos[1] += 1
    