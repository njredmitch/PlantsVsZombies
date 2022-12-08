import pygame
from Model.player import Player
from Model.front_yard import FrontYard

class Graphics:
    """represents the Graphics of the game
    """
    def __init__(self, yard :FrontYard, player : Player):
        """initializes the graphics

        Args:
            yard (FrontYard): the yard of the house
            player (Player): the player
        """
        pygame.init()
        self._font = pygame.font.Font(None, 60)
        self._sun_font = pygame.font.Font(None, 30)
        self._yard = yard
        self._player = player

    def draw_graphics(self, screen : pygame.display):
        """draws all of the objects onto the given screen

        Args:
            screen (pygame.display): the screen on which to draw
        """
        pygame.init()
        background = pygame.image.load('PlantsVsZombies\GamePNGS\FrontyardFull.png')
        sun_count = self._sun_font.render(f'SUN: {self._player.get_sun()}', True, 'Black')
        sun_count_background = pygame.Surface((sun_count.get_width(), sun_count.get_height()))
        sun_count_background.fill('White')

        screen.blit(background, (0,0))
        screen.blit(sun_count_background, (560,20))
        screen.blit(sun_count, (560,20))

        self._yard.get_shovel_group().draw(screen)
        self._yard.get_plants().draw(screen)
        self._yard.get_zombies_group().draw(screen)
        self._yard.get_projectiles().draw(screen)
        self._yard.get_sun().draw(screen)
        self._yard.get_game_sqaures_group().draw(screen)
        self._yard._shop_group.draw(screen)
        self._yard._active.draw(screen)

        if self._player.get_final_status() != None:
            if not self._player.get_final_status():
                screen.blit(self._font.render('YOU LOST, THE ZOMBIES ATE YOU', True, 'Red'), (300,350))
            else:
                screen.blit(self._font.render('YOU KILLED ALL THE ZOMBIES, YOU WIN!!', True, 'Black'), (200,250))

        pygame.display.update()
