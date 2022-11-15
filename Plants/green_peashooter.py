import pygame
from peashooter import Peashooter

class GreenPeashooter(Peashooter, pygame.sprite.Sprite):
    image_path = 'PlantsVsZombies\GamePNGS\Peashooter.png'
    cost = 100

    def __init__(self, position) -> None:
        Peashooter.__init__(position)
        pygame.sprite.Sprite.__init__()
    
    
    def shoot():
        pass

        