import pygame
from Model.player import Player
from Model.front_yard import FrontYard

class Graphics:

    def __init__(self, yard :FrontYard, player : Player):
        pygame.init()
        self._font = pygame.font.Font(None, 60)
        self._sun_font = pygame.font.Font(None, 30)
        self._yard = yard
        self._player = player

    def draw_graphics(self, screen : pygame.display, made):
        background = pygame.image.load('PlantsVsZombies\GamePNGS\FrontyardFull.png')
        player_surf = self._sun_font.render(f'SUN: {self._player.get_sun()}', True, 'Black')
        made_surf = self._sun_font.render(f'Made: {made}',  True, 'Black')

        screen.blit(background, (0,0))
        screen.blit(player_surf, (560,20))
        screen.blit(made_surf, (700,20))
        
        self._yard.get_plants().draw(screen)
        self._yard.get_zombies_group().draw(screen)
        self._yard.get_projectiles().draw(screen)
        self._yard.get_sun().draw(screen)
        self._yard.get_game_sqaures_group().draw(screen)
        self._yard._shop_group.draw(screen)
        self._yard._unplaced.draw(screen)

        if self._player.get_final_status() != None:
            if not self._player.get_final_status():
                screen.blit(self._font.render('YOU LOST, THE ZOMBIES ATE YOU', True, 'Red'), (300,350))
            else:
                screen.blit(self._font.render('YOU KILLED ALL THE ZOMBIES, YOU WIN!!', True, 'Black'), (200,250))

        pygame.display.update()