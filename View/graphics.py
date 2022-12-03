import pygame
from Model.player import Player
from Model.front_yard import FrontYard

class Graphics:

    def __init__(self, yard :FrontYard, player : Player):
        pygame.init()
        self._screen = pygame.display.set_mode((1200,800))
        self._yard = yard
        self._player = player
        self._font = pygame.font.Font(None, 60)

    def draw(self):
        background = pygame.image.load('PlantsVsZombies\GamePNGS\FrontyardFull.png')
        self._screen.blit(background, (0,0))
        for group in self._yard.get_groups():
            group.draw(self._screen)

        if self._player.get_final_status():
            self._screen.blit(self._font.render('YOU LOST, THE ZOMBIES ATE YOU', True, 'Red'), (300,350))
        else:
            self._screen.blit(self._font.render('YOU KILLED ALL THE ZOMBIES, YOU WIN!!', True, 'Black'), (200,250))

        pygame.display.update()
