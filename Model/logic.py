import pygame
import random

from Model.Plants.sunflower import Sunflower as SF
from Model.Zombies.grunt_zombie import GruntZombie as GZ
from Model.Zombies.cone_zombie import ConeZombie as CZ
from Model.Zombies.bucket_zombie import BucketZombie as BZ

from Model.front_yard import FrontYard
from Model.player import Player

class Logic:
    
    def __init__(self) -> None:
        self._yard = FrontYard()
        self._player = Player()
        self._is_end_game = False
        self._zombies_made = 0
    
    def yard_row_entered(self, i):
        for z in self._yard.get_zombies()[i]:
            if z.get_position()[0] < 1225:
                return True
        return False

    def prime_shooters(self): #primes all shooting plants that detect zombies
        for i in range(5):
            if self.yard_row_entered(i) > 0:
                for p in self._yard.get_peashooters()[i]:
                    if not p.is_primed():
                        #print('priming')
                        p.prime()
    
    def make_projectiles(self): #make shooter plants shoot projectiles
        for i in range(5):
            for p in self._yard.get_peashooters()[i]:
                if p.is_primed():
                    p.shoot_peas()

    def update_shooters(self):
        self.prime_shooters()
        self.unprime_peashooters()

    def unprime_peashooters(self): #unprime any shooting plants that dont detect zombies 
        for i in range(5):
            if len(self._yard.get_zombies()[i]) == 0 or not self.yard_row_entered(i):
                for p in self._yard.get_peashooters()[i]:
                    if p.is_primed():
                        #print('unpriming')
                        p.unprime()

    def make_sunlight(self):
        for s in self._yard.get_sunflowers():
            s.run_event()

    def damage_zombies(self): #make projectiles damage zombies
        collisions = pygame.sprite.groupcollide(self._yard.get_zombies_group(), self._yard.get_projectiles(), False, True)
        peas = []
        for z in collisions.keys():
            for p in collisions[z]:
                z.lose_health(p.get_dmg())
                peas.append(p)
        
        for p in peas:
            self._yard.remove_projectile(p)

    def update_zombie_movement(self):
        self.stop_zombies_walk()
        self.start_zombies_walk()

    def stop_zombies_walk(self):
        for z in self._yard.get_zombies_group().sprites():
            for p in self._yard.get_plants().sprites():
                if p.get_rect().collidepoint(z.get_rect().center):
                    z.set_movement_status(False)
    
    def start_zombies_walk(self):
        for z in self._yard.get_zombies_group().sprites():
            if len(pygame.sprite.spritecollide(z, self._yard.get_plants(), False)) == 0:
                z.set_movement_status(True)

    def make_zombies_attack(self): #attacking plants
         for p in self._yard.get_plants().sprites():
            for z in self._yard.get_zombies_group().sprites():
                if p.get_rect().collidepoint(z.get_rect().midleft):
                    p.lose_health(z.get_attack_dmg())

    def remove_projectiles(self, end : int): #removing projectiles passed game border
        to_remove = []
        for p in self._yard.get_projectiles():
            if p.get_pos()[0] > end:
                to_remove.append(p)

        for p in to_remove:
            self._yard.remove_projectile(p)
    
    def remove_dead_zombies(self): #removing dead zombies
        for row in self._yard.get_zombies():
            for z in row.copy():
                if z.get_health() <= 0:
                    self._yard.remove_zombie(z)

    def remove_dead_plants(self): # remove dead plants
        for g in self._yard.get_game_sqaures_group():
            p = self._yard.get_game_squares()[g]
            if p != None and p.get_health() <= 0:
                self._yard.remove_plant(p, g)

    def check_sun_clicked(self, mouse : tuple[int]): #check if player has clicked on sun
        for s in self._yard.get_sun():
            if s.is_clicked(mouse):
                self._player.gain_sun(25)
                self._yard.remove_sun(s)
                break
    
    def give_player_sun(self):
        self._player.gain_sun(25)

    def get_shop_clicked(self, mouse):
        for p in self._yard._shop_group:
            if (p.get_rect().collidepoint(mouse) and self._player.get_sun() >= p.get_cost() 
                and not self._player.has_plant()):
                return True, p
        return False, None
            
    def buy_plant(self, mouse : tuple[int]): #player buying plant``
        has_clicked, item = self.get_shop_clicked(mouse)
        if has_clicked and not self.has_player_purchased() and not self._player.has_shovel():
            self._player.spend_sun(item.get_cost())
            plant = item.get_plant().deepcopy()
            self._player.store_plant(plant)
            self._yard._active.add(plant)
    
    def update_zombie_positions(self):
        for z in self._yard._zombie_group.sprites():
            if z.get_movement_status() == True:
                z.update_xpos(1)
                z.update_xrect()

    def update_projectile_positions(self):
        for p in self._yard.get_projectiles().sprites():
            p.update_xpos(10)
            p.get_rect().right += 10

    def update_plant_pos(self, mouse : tuple[int]): #updating position of player plant
        self._player.get_plant().set_position(mouse)
        self._player.get_plant().get_rect().center = mouse

    def place_plant(self, mouse : tuple[int]): #placing plant
        for g in self._yard.get_game_squares().keys():
            if g.get_rect().collidepoint(mouse) and self._yard.get_game_squares()[g] == None:
                p = self._player.get_plant()
                pos = g.get_pos()
                if isinstance(p, SF):
                    p.set_position((pos[0], pos[1] - 25))
                    p.get_rect().midbottom = (pos[0], pos[1] - 25)
                else:
                    p.set_position((pos[0], pos[1] - 15))
                    p.get_rect().midbottom = (pos[0], pos[1] - 15)
                self._yard.add_plant(p, g)
                self._player.store_plant(None)

    def update_shovel_pos(self, pos):
        self._player.get_shovel().update(pos)

    def acquire_shovel(self, pos):
        if self._yard.get_shovel_group().sprite.rect.collidepoint(pos) and not self.has_player_purchased() and not self._player.has_shovel():
            shovel = self._yard.get_shovel_group().sprites()[0]
            self._player.set_shovel(shovel.get_shovel().copy())
            self._yard._active.add(self._player.get_shovel())

    def use_shovel(self, mouse : tuple[int]):
        if self._yard.get_shovel_group().sprite.rect.collidepoint(mouse):
            self._player.get_shovel().kill()
            self._player.set_shovel(None)
        for g in self._yard.get_game_squares().keys():
            p = self._yard.get_game_squares()[g]
            if g.get_rect().collidepoint(mouse) and p != None:
                self._yard.remove_plant(p, g)
                self._player.get_shovel().kill()
                self._player.set_shovel(None)
        
    def has_player_purchased(self): #check if player has bought a plant
        return self._player.get_plant() != None

    def check_if_lost(self, start : int): #check if player lost
        
        for z in self._yard.get_zombies_group().sprites():
            if z.get_position()[0] < start:
                self._player.set_final_status(False)
                return True
        return False
    
    def check_if_won(self): #checks if player has won the game
        res = not self._yard.any_zombies_left() and self._is_end_game
        if res:
            self._player.set_final_status(True)
        return res

    def end_game(self, x): #ends the game if either condition is true
        return self.check_if_lost(x) or self.check_if_won()

    def zombies_enter_yard(self): #adds zombies increasing number based on zombies killed
        if self._zombies_made < 85: 
            if self._zombies_made < 7:
                self._yard.add_zombie(self.make_single_zombie())

            elif self._zombies_made == 7: 
                self._yard.add_zombie(self.make_small_z_wave())

            elif 12 <= self._zombies_made < 19: 
                self._yard.add_zombie(self.make_mini_z_wave())
            
            elif self._zombies_made == 20:
                self._yard.add_zombie(self.make_single_zombie())
            
            elif self._zombies_made == 21:
                self._yard.add_zombie(self.make_single_zombie())
            
            elif 22 <= self._zombies_made < 29: 
                self._yard.add_zombie(self.make_mini_z_wave())

            elif 30 == self._zombies_made:
                self._yard.add_zombie(self.make_medium_z_wave())
            
            elif 40 <= self._zombies_made < 70:
                self._yard.add_zombie(self.make_mini_z_wave())

            else:
                self._yard.add_zombie(self.make_final_z_wave())

    def produce_zombie(self, pos : tuple[int]): #creates a zombie based on progression through level
        i = random.random()
        z = None
        if self._zombies_made < 4:
            z = GZ(pos)

        elif 4 == self._zombies_made:
            z = CZ(pos)

        elif 5 <= self._zombies_made < 20:
            if i < 0.4:
                z = CZ(pos)
            else:
                z = GZ(pos)

        elif self._zombies_made == 20:
            z = BZ(pos)

        elif 21 <= self._zombies_made < 40:
            if 0 <= i < 0.4:
                z = GZ(pos)
            elif 0.4 <= i < 0.8:
                z = CZ(pos)
            else:
                z = BZ(pos)

        elif 40 <= self._zombies_made < 55:
            if 0 <= i < 0.3:
                z = GZ(pos)
            elif 0.3 <= i < 0.7:
                z = CZ(pos)
            else:
                z = BZ(pos)

        else:
            if 0 <= i < 0.25:
                z = GZ(pos)
            elif 0.25 <= i < 0.65:
                z = CZ(pos)
            else:
                z = BZ(pos)
        return z

    def make_single_zombie(self): #creates a zingle zombie
        self._zombies_made += 1
        x = 1225
        y = random.sample([240, 370, 505, 635, 760], 1)[0]

        return self.produce_zombie((x, y - 5))

    def make_mini_z_wave(self): #makes 2-3 zombies
        z = []
        x = 1225
        if self._zombies_made < 30:
            y = random.sample([240, 370, 505, 635, 760], 2)
            z = [self.produce_zombie((x, y[0] - 5)), 
                 self.produce_zombie((x, y[1] - 5))]
            self._zombies_made +=  2
        else:
            y = random.sample([240, 370, 505, 635, 760], 3)
            z  = [self.produce_zombie((x, y[0] - 5)), 
                    self.produce_zombie((x, y[1] - 5)),
                    self.produce_zombie((x, y[2] - 5))]
            self._zombies_made += 3
        return z

    def make_small_z_wave(self): #makes 5 zombies at once
        x = random.sample(range(1225, 1260), 5)
        y = [250, 380, 515, 635, 760]
        self._zombies_made += 5
        
        return [self.produce_zombie((x[i], y[i] - 5)) for i in range(5)]
    
    def make_medium_z_wave(self): #makes 10 zombies at once
        x = random.sample(range(1225, 1250), 10)
        y = [240, 370, 505, 635, 760]
        self._zombies_made += 10
        
        return [self.produce_zombie((x[i], y[i % 5] - 5)) for i in range(10)]
    
    def make_final_z_wave(self): #makes 20 zombies at once
        x = random.sample(range(1225, 1260), 15)
        y = [240, 370, 505, 635, 760]
        self._zombies_made += 15
        self._is_end_game = True
        return [self.produce_zombie((x[i], y[i % 5] - 5)) for i in range(15)]