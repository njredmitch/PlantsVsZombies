import pygame
import time
import schedule
from sys import exit
from Model.logic import Logic
from View.graphics import Graphics

class Game:

    def __init__(self, logic : Logic, graphics : Graphics) -> None:
        self._logic = logic
        self._graphics = graphics
    
    def run_game(self):
        pygame.init()
        screen = pygame.display.set_mode((1165,800))
        clock = pygame.time.Clock()
        FPS = 60
        loops = 0
        scheduler = schedule.Scheduler()
        sun_scheduler = schedule.Scheduler()
        scheduler.every(30).seconds.do(self._logic.zombies_enter_yard)
        sun_scheduler.every(15).seconds.do(self._logic.give_player_sun)

        while True:
            events = pygame.event.get()
            if not self._logic.end_game(280):
                for event in events:
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        exit()
                    
                    if event.type == pygame.MOUSEMOTION:
                        if self._logic.has_player_purchased():
                            self._logic.update_player_plant(pygame.mouse.get_pos()) #updating player plant

                    if event.type == pygame.MOUSEBUTTONUP:
                        self._logic.check_sun_clicked(pygame.mouse.get_pos()) #clicking sun
                        self._logic.buy_plant(pygame.mouse.get_pos()) #buing plants
                    
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if self._logic.has_player_purchased():
                            self._logic.place_plant(pygame.mouse.get_pos()) #placing  plants
                    
                if self._logic._zombies_made == 14:
                    scheduler.clear()
                    scheduler.every(15).seconds.do(self._logic.zombies_enter_yard)
                
                if loops % 30 == 0:
                    self._logic.make_zombies_attack() #attacking plants
                
                if loops % 5 == 0:
                    self._logic.update_zombie_positions() 
                
                
                scheduler.run_pending() 
                self._logic.make_sunlight()
                self._logic.remove_projectiles(1185) #removing objects
                self._logic.remove_dead_plants()
                self._logic.remove_dead_zombies()
                self._logic.damage_zombies() #damaging zombies
                self._logic.update_shooters() # priming/unpriming shooters
                self._logic.make_projectiles()# making all shooters shoot
                self._logic.update_zombie_movement()
                #updating positions of moving objects
                self._logic.update_projectile_positions()
                sun_scheduler.run_pending()
                self._graphics.draw_graphics(screen, self._logic._zombies_made)
            else:
                for event in events:
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        exit()
                self._graphics.draw_graphics(screen)

            loops += 1
            clock.tick(FPS)
               


