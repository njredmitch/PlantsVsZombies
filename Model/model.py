import pygame
import random
from Plants.plant import Plant
from Zombies.zombie import Zombie
from Projectiles.projectile import Projectile
from GameObjects.sun import Sun
from GameObjects.frontyard import FrontYard
from player import Player

from Plants.peashooter import Peashooter as PS
from Plants.flameshooter import Flameshooter as FS
from Plants.iceshooter import Iceshooter as IS
from Plants.green_peashooter import GreenPeashooter as GPS
from Plants.walnut import Walnut as W
from Plants.sunflower import Sunflower as S

from Zombies.grunt_zombie import GruntZombie as GZ
from Zombies.bucket_zombie import BucketZombie as BZ
from Zombies.cone_zombie import ConeZombie as CZ

from Projectiles.pea import Pea
from Projectiles.flame_pea import FlamePea as FP
from Projectiles.ice_pea import IcePea as IP
from Projectiles.green_pea import GreenPea as GP

#note: update attack zombie method so u get collisions between plants and zombies
#remove zombie schedule and plant to attack field

class Model:
    
    def __init__(self, sprites : pygame.sprite.Group, player : Player) -> None:
        self._yard = FrontYard(sprites)
        self._player = player
        self._is_end_game = False
        self._zombies_made = 0
    
    def prime_shooters(self): #primes all shooting plants that detect zombies
        for i in range(5):
            if len(self._yard.get_peashooters[i]) > 0 and len(self._yard.get_zombies[i]) > 0:
                for p in self._yard.get_peashooters[i]:
                    if not p.is_primed():
                        p.prime()
    
    def make_projectiles(self): #make shooter plants shoot projectiles
        for i in range(5):
            for p in self._yard.get_peashooters[i]:
                if p.is_primed():
                    p.shoot_peas()

    def unprime_peashooters(self): #unprime any shooting plants that dont detect zombies 
        for i in range(5):
            if not self.peashooter_detect_zombies(i) and len(self._yard.get_peashooters) > 0:
                for p in self._yard.get_peashooters[i]:
                    if not p.is_primed():
                         p.unprime()
    
    def damage_zombies(self): #make projectiles damage zombies
        collisions = pygame.sprite.groupcollide(self._yard.get_zombies_group(), self._yard.get_projectiles(), False, True)
        peas = []
        for z in collisions.keys():
            for p in collisions[z]:
                z.lose_health(p.get_dmg)
                peas.append(p)
        
        for p in peas:
            self._yard.remove_projectile(p)

    def make_zombies_attack(self): #attacking plants
        collisions = pygame.sprite.groupcollide(self._yard.get_plants, self._yard.get_zombies_group, False, False)
        for p in collisions.keys():
            for z in collisions[p]:
                p.lose_health(z.get_attack_dmg())

    def remove_projectiles(self, end : int): #removing projectiles passed game border
        to_remove = []
        for p in self._yard.get_projectiles:
            if p.get_pos[0] > end:
                to_remove.append(p)

        for p in to_remove:
            self._yard.remove_projectile(p)
    
    def remove_zombies(self): #removing dead zombies
        for row in self._yard.get_zombies:
            for i in range(len(row)):
                if row[i].get_health() <= 0:
                    self._yard.remove_zombie(row[i])
                    self._player.killed_zombie
                    i -= 1

    def remove_dead_plants(self): # remove dead plants
        for p in self._yard.get_plants():
            if p.get_health() <= 0:
                self._yard.remove_plant(p)
                self.zombies_stop_attacking(self._yard.get_zombies_group, p)

    def check_sun_clicked(self, mouse : tuple[int]): #check if player has clicked on sun
        for s in self._yard.get_sun:
            if s.is_clicked(mouse):
                self._player.gain_sun(25)
                self._yard.remove_sun(s)
                break
    
    def buy_plant(self, mouse : tuple[int]): #player buying plant
        for p in self._yard._shop_group:
            if (p.collidepoint(mouse) and self._player.get_sun() >= p.get_cost() 
                and not self._player.has_plant()):
                self._player.spend_sun(p.get_cost())
                self._player.store_plant(p.get_plant(), mouse)
    
    def update_player_plant(self, mouse : tuple[int]): #updating position of player plant
        self._player.get_plant().set_position(mouse)

    def place_plant(self, mouse : tuple[int]): #placing plant
        for g in self._yard.get_game_squares().keys():
            if g.collidepoint(mouse) and self._yard.get_game_squares()[g] == None:
                p = self._player.get_plant()
                pos = g.get_pos()
                p.set_position((pos[0], pos()[1] - 15))
                self._player.store_plant(None)
    
    def has_player_purchased(self): #check if player has bought a plant
        return self._player.get_plant() != None
    
    def check_if_lost(self, start : int): #check if player lost
        for z in self._yard.get_zombies_group():
            if z.get_position()[0] < start:
                self._player.set_final_status(False)
                return True
                
        return False
    
    def check_if_won(self): #checks if player has won the game
        res = self._yard.any_zombies_left() and self._is_end_game
        if res:
            self._player.set_final_status(True)
        return res

    def end_game(self): #ends the game if either condition is true
        return self.check_if_lost() or self.check_if_won()

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
        i = random.random
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
        x = random.randint(1100, 1130)
        y = random.sample([250, 380, 515, 635, 770], 1)[0]

        return self.produce_zombie((x, y))

    def make_mini_z_wave(self): #makes 2-3 zombies
        z = []
        if self._zombies_made < 30:
            x = 1150
            y = random.sample([250, 380, 515, 635, 770], 2)
            z = [self.produce_zombie((x, y[0])), 
                    self.produce_zombie((x, y[1]))]
            self._zombies_made +=  2
        else:
            x = 1150
            y = random.sample([250, 380, 515, 635, 770], 3)
            z  = [self.produce_zombie((x, y[0])), 
                    self.produce_zombie((x, y[1])),
                    self.produce_zombie((x, y[2]))]
            self._zombies_made += 3
        return z

    def make_small_z_wave(self): #makes 5 zombies at once
        x = random.sample(range(1100, 1130), 5)
        y = [250, 380, 515, 635, 770]
        self._zombies_made += 5
        
        return [self.produce_zombie((x[i], y[i])) for i in range(5)]
    
    def make_medium_z_wave(self): #makes 10 zombies at once
        x = random.sample(range(1100, 1130), 10)
        y = [250, 380, 515, 635, 770]
        self._zombies_made += 10
        
        return [self.produce_zombie((x[i], y[i % 5])) for i in range(10)]
    
    def make_final_z_wave(self): #makes 20 zombies at once
        x = random.sample(range(1100, 1130), 10)
        y = [250, 380, 515, 635, 770]
        self._zombies_made += 15
        
        return [self.produce_zombie((x[i], y[i % 5])) for i in range(15)]


        

    
    


            
    


        
        
        
    
    



    



