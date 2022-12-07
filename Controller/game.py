import pygame
import time
import schedule
from sys import exit
from Model.logic import Logic
from View.graphics import Graphics

class Game:
    """Represents the controller running the game
    """
    def __init__(self, logic : Logic, graphics : Graphics) -> None:
        """initializes the controller

        Args:
            logic (Logic): the logic handeling the game
            graphics (Graphics): the graphics of the game
        """
        self._logic = logic
        self._graphics = graphics
    
    def run_game(self):
        """starts the game and runs it
        """
        pygame.init()
        screen = pygame.display.set_mode((1165,800))
        clock = pygame.time.Clock()
        FPS = 60
        loops = 0
        faster = False
        scheduler = schedule.Scheduler()
        sun_scheduler = schedule.Scheduler()
        scheduler.every(30).seconds.do(self._logic.zombies_enter_yard)
        sun_scheduler.every(20).seconds.do(self._logic.give_player_sun)

        while True:
            events = pygame.event.get()
            if not self._logic.end_game(300):
                for event in events:
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        exit()
                    
                    if event.type == pygame.MOUSEMOTION:
                        if self._logic.has_player_purchased():
                            self._logic.update_plant_pos(pygame.mouse.get_pos()) #updating player plant
                        elif self._logic._player.has_shovel():
                            self._logic.update_shovel_pos(pygame.mouse.get_pos())

                    if event.type == pygame.MOUSEBUTTONUP:
                        self._logic.check_sun_clicked(pygame.mouse.get_pos()) #clicking sun
                        self._logic.buy_plant(pygame.mouse.get_pos()) #buing plants
                        if not self._logic._player.has_shovel():
                            self._logic.acquire_shovel(pygame.mouse.get_pos())
                        elif self._logic._player.has_shovel():
                            self._logic.use_shovel(pygame.mouse.get_pos())
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if self._logic.has_player_purchased():
                            self._logic.place_plant(pygame.mouse.get_pos()) #placing  plants
                if self._logic._zombies_made == 14 and not faster:
                    faster = True
                    scheduler.clear()
                    scheduler.every(15).seconds.do(self._logic.zombies_enter_yard)
                
                
                scheduler.run_pending() 
                sun_scheduler.run_pending()
                self._run_tasks(loops)

                self._graphics.draw_graphics(screen)

            else:
                for event in events:
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        exit()
                self._graphics.draw_graphics(screen)

            loops += 1
            clock.tick(FPS)

    def _run_tasks(self, loops):
        """runs tasks to be called every iteration in the main loop

        Args:
            loops (int): how many loops have been run
        """
        self._logic.unlock_shops()
        self._logic.open_shops()
        self._logic.make_sunlight()
        self._logic.remove_projectiles(1185) #removing objects
        self._logic.remove_dead_plants()
        self._logic.remove_dead_zombies()
        self._logic.damage_zombies() #damaging zombies
        self._logic.update_shooters() # priming/unpriming shooters
        self._logic.make_projectiles()# making all shooters shoot
        self._logic.update_zombie_movement()
        self._logic.thaw_zombies()
        if loops % 30 == 0:
            self._logic.update_slow_zombie_positions()
        if loops % 30 == 0:
                    self._logic.make_zombies_attack() #attacking plants
        if loops % 5 == 0:
            self._logic.update_zombie_positions()     
        self._logic.update_projectile_positions()


