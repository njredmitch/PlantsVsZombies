import pygame
import random

from Model.Plants.sunflower import Sunflower as SF
from Model.Plants.walnut import Walnut as W

from Model.Projectiles.ice_pea import IcePea as IP

from Model.Zombies.grunt_zombie import GruntZombie as GZ
from Model.Zombies.cone_zombie import ConeZombie as CZ
from Model.Zombies.bucket_zombie import BucketZombie as BZ

from Model.front_yard import FrontYard
from Model.player import Player

class Logic:
    """this class handles the logic of the game
    """
    def __init__(self) -> None:
        self._yard = FrontYard()
        self._player = Player()
        self._is_end_game = False
        self._zombies_made = 0
    
    def yard_row_entered(self, i):
        """this method checks if the given yard row was entered by zombies

        Args:
            i (int): yard row

        Returns:
            boolean: True if entered False otehrwise
        """
        for z in self._yard.get_zombies()[i]:
            if z.get_position()[0] < 1225:
                return True
        return False

    def prime_shooters(self): #primes all shooting plants that detect zombies
        """makes any shooter type plant ready to shoot 
        if a zombie is detected in its row
        """
        for i in range(5):
            if self.yard_row_entered(i) > 0:
                for p in self._yard.get_peashooters()[i]:
                    if not p.is_primed():
                        #print('priming')
                        p.prime()
    
    def make_projectiles(self): #make shooter plants shoot projectiles
        """makes all primed shooter plants shoot a projectile
        """
        for i in range(5):
            for p in self._yard.get_peashooters()[i]:
                if p.is_primed():
                    p.shoot_peas()

    def update_shooters(self):
        """this method primes or unprimes shooter plants
        calling the prime/unprime shooter methods
        """
        self.prime_shooters()
        self.unprime_peashooters()

    def unprime_peashooters(self): #unprime any shooting plants that dont detect zombies 
        """this method unprimes any primed shooters 
        if no zombies are detected in their row
        """
        for i in range(5):
            if len(self._yard.get_zombies()[i]) == 0 or not self.yard_row_entered(i):
                for p in self._yard.get_peashooters()[i]:
                    if p.is_primed():
                        #print('unpriming')
                        p.unprime()

    def make_sunlight(self):
        """calls every flower to make sunlight if they are recharged
        """
        for s in self._yard.get_sunflowers():
            s.run_event()

    def thaw_zombies(self):
        """makes any zombie who's slowed timer is up
        return back to normal walking speed
        """
        for z in list(filter(lambda z: z.get_slowed_status(), self._yard.get_zombies_group().sprites())):
            z.run_task()

    def unlock_shops(self):
        """unlocks a shop based upon the current progression of the level
        """
        if self._zombies_made == 12:
            self._yard.get_shop_group().sprites()[3].open()
        elif self._zombies_made == 40:
            self._yard.get_shop_group().sprites()[4].open()

    def open_shops(self):
        """re-opens any shop that was closed 
        who's closed timer is finished
        """
        for shop in self._yard.get_shop_group().sprites():
            if not shop.is_open():
                shop.run_event()

    def damage_zombies(self): #make projectiles damage zombies
        """makes all zombies that were hit by a projectile take damage
        """
        collisions = pygame.sprite.groupcollide(self._yard.get_zombies_group(), self._yard.get_projectiles(), False, True)
        peas = []
        for z in collisions.keys():
            for p in collisions[z]:
                if isinstance(p, IP) and not z.get_slowed_status():
                    z.freeze()
                    z.update_scheduler()
                z.lose_health(p.get_dmg())
                self.update_zombie_conditions(z)
                peas.append(p)
        
        for p in peas:
            self._yard.remove_projectile(p)

    def update_zombie_movement(self):
        """updates zombies to stop walking or start walking
        calling the stop/start zombie walk functions
        """
        self.stop_zombies_walk()
        self.start_zombies_walk()

    def stop_zombies_walk(self):
        """stops any zombie that has collided with a plant in its row
        """
        for z in self._yard.get_zombies_group().sprites():
            for p in self._yard.get_plants().sprites():
                if p.get_rect().collidepoint(z.get_rect().center) and z.get_movement_status() == True:
                    z.set_movement_status(False)
    
    def start_zombies_walk(self):
        """makes all zombies that are currently stationary
        resume walking if they are not collided with a plant in their row
        """
        for z in self._yard.get_zombies_group().sprites():
            if len(pygame.sprite.spritecollide(z, self._yard.get_plants(), False)) == 0 and z.get_movement_status() == False:
                z.set_movement_status(True)
            else:
                plants = pygame.sprite.spritecollide(z, self._yard.get_plants(), False)
                pairs = self.make_plant_zombie_pairs(z, plants)
                same_row = list(filter(self.is_same_row, pairs))
                if  len(same_row) == 0 and z.get_movement_status() == False:
                    z.set_movement_status(True)
                elif len(same_row) != 0:
                    if all(list(map(lambda pair: not pair[1].get_rect().collidepoint(pair[0].get_rect().center), same_row))):
                        z.set_movement_status(True)

    def is_same_row(self, pair):
        """checks if a plant and zombie 
        are in the same row

        Args:
            pair (tuple[Zombie, Plant]): a zombie and plant collision

        Returns:
            Boolean: True if the collided objects are in the same row false othewise
        """
        z = pair[0]
        p = pair[1]
        return p.get_position()[1]//145 - 1 == z.get_position()[1]//150 - 1

    def make_plant_zombie_pairs(self, z, plants):
        """makes a pair between each plant collided with a given zombie

        Args:
            z (Zombie): A Zombie collided with Plants
            plants (List[Plants]): a list of all plants a Zombie has collided with

        Returns:
            list[tuple[Zombie, Plant]]: A list of all zombie plant pairs from the given collisions
        """
        return list(map(lambda p: (z, p), plants))

    def make_zombies_attack(self): #attacking plants
        """makes any zombie that has collided with a plant in its row attack it
        """
        for p in self._yard.get_plants().sprites():
            for z in self._yard.get_zombies_group().sprites():
                if p.get_rect().collidepoint(z.get_rect().center):
                    if isinstance(p, W):
                        if p.get_health() > 720:
                            p.set_image('PlantsVsZombies\GamePNGS\Walnut_Frame.png')
                            p.lose_health(z.get_attack_dmg())
                            p.set_image('PlantsVsZombies\GamePNGS\Walnut.png')
                        else:
                            p.set_image('PlantsVsZombies\GamePNGS\Injured_Walnut_Frame.png')
                            p.lose_health(z.get_attack_dmg())
                            p.set_image('PlantsVsZombies\GamePNGS\Injured_Walnut.png')
                    else:
                         p.lose_health(z.get_attack_dmg())

    def remove_projectiles(self, end : int): #removing projectiles passed game border
        """removes any projectiles that have crossed the edge of the screen

        Args:
            end (int): the edge of the screen
        """
        to_remove = []
        for p in self._yard.get_projectiles():
            if p.get_pos()[0] > end:
                to_remove.append(p)

        for p in to_remove:
            self._yard.remove_projectile(p)
    
    def remove_dead_zombies(self): #removing dead zombies
        """removes any dead zombies from the game
        """
        for row in self._yard.get_zombies():
            for z in row.copy():
                if z.get_health() <= 0:
                    self._yard.remove_zombie(z)

    def remove_dead_plants(self): # remove dead plants
        """removes any dead plants from the game
        """
        for g in self._yard.get_game_sqaures_group():
            p = self._yard.get_game_squares()[g]
            if p != None and p.get_health() <= 0:
                self._yard.remove_plant(p, g)

    def check_sun_clicked(self, mouse : tuple[int]): #check if player has clicked on sun
        """checks if the player has clicked Sun, adding to the players sun count and 
        removing the Sun object clicked
        Args:
            mouse (tuple[int]): the position of the mouse when clicked
        """
        for s in self._yard.get_sun():
            if s.is_clicked(mouse):
                self.give_player_sun()
                self._yard.remove_sun(s)
                break
    
    def give_player_sun(self):
        """adds 25 to the players sun count
        """
        self._player.gain_sun(25)

    def get_shop_clicked(self, mouse):
        """checks if a plant shop was clicked on

        Args:
            mouse (tuple(int)): the current position of the mouse

        Returns:
            (Bool, Shop): True and the Shop item clicked on or false and None
        """
        for p in self._yard.get_shop_group().sprites():
            if (p.get_rect().collidepoint(mouse) and self._player.get_sun() >= p.get_cost() 
                and not self._player.has_plant()):
                return True, p
        return False, None
            
    def buy_plant(self, mouse : tuple[int]): #player buying plant``
        """gives player a plant they purchesed if they dont already have one

        Args:
            mouse (tuple[int]): current position of the mouse
        """
        has_clicked, item = self.get_shop_clicked(mouse)
        if has_clicked and not self.has_player_purchased() and not self._player.has_shovel() and item.is_open():
            self._player.spend_sun(item.get_cost())
            plant = item.get_plant().deepcopy()
            self._player.store_plant(plant)
            self._yard._active.add(plant)
            item.close()
    
    def update_zombie_positions(self):
        """moves all the non-slowed zombies forward
        """
        zombies = list(filter(lambda z: not z.get_slowed_status(), self._yard._zombie_group.sprites()))
        for z in zombies:
            if z.get_movement_status() == True:
                z.update_xpos(1)
                z.update_xrect(1)
    
    def update_slow_zombie_positions(self):
        """moves all the slowed zombies forward
        """
        zombies = list(filter(lambda z: z.get_slowed_status(), self._yard._zombie_group.sprites()))
        for z in zombies:
            if z.get_movement_status() == True:
                z.update_xpos(1)
                z.update_xrect(1)

    def update_projectile_positions(self):
        """moves all the projectiles forward
        """
        for p in self._yard.get_projectiles().sprites():
            p.update_xpos(10)
            p.get_rect().right += 10

    def update_plant_pos(self, mouse : tuple[int]): #updating position of player plant
        """sets the position of the plant in the players inventory
        to the current mouse position

        Args:
            mouse (tuple[int]): current mouse position on the screen
        """
        self._player.get_plant().set_position(mouse)
        self._player.get_plant().get_rect().center = mouse

    def update_zombie_conditions(self, z):
        """updates the graphic of a zombie based 
        on how much damage it has sustained

        Args:
            z (Zombie): A Zombie on the yard
        """
        if z.get_health() == 40:
            z.update_image('PlantsVsZombies\GamePNGS\Injured_Zombie.png')
        elif (isinstance(z, CZ) or isinstance(z, BZ)) and z.get_health() == 120:
            z.update_image('PlantsVsZombies\GamePNGS\Zombie.png')
        elif isinstance(z, CZ) and z.get_health() == 320:
            z.update_image('PlantsVsZombies\GamePNGS\Injured_Conehead.png')
        elif isinstance(z, BZ) and z.get_health() == 700:
            z.update_image('PlantsVsZombies\GamePNGS\Injured_Buckethead.png')

    def place_plant(self, mouse : tuple[int]): #placing plant
        """places a plant onto the yard if a plant 
        is not already in the spot clicked

        Args:
            mouse (tuple[int]): the current position of the mouse
        """
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
        """sets the position of the shovel 
        to the current mouse position

        Args:
            pos (tuple[int]): current mouse position
        """
        self._player.get_shovel().update(pos)

    def acquire_shovel(self, pos):
        """gives the player a shovel if their inventory is currently empty
        and if they clicked on the shovel square

        Args:
            pos (tuple[int]): current mouse position
        """
        if self._yard.get_shovel_group().sprite.rect.collidepoint(pos) and not self.has_player_purchased() and not self._player.has_shovel():
            shovel = self._yard.get_shovel_group().sprites()[0]
            self._player.set_shovel(shovel.get_shovel().copy())
            self._yard._active.add(self._player.get_shovel())

    def use_shovel(self, mouse : tuple[int]):
        """uses the shovel to remove the plant clicked on from the yard 
        or returns the shovel to the shovel square

        Args:
            mouse (tuple[int]): current mouse position
        """
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
        """checks if a player currently has a 
        plant in their inventory

        Returns:
            Boolean: True if they have a plant False otherwise
        """
        return self._player.get_plant() != None

    def check_if_lost(self, start : int): #check if player lost
        """checks if the player lost the game

        Args:
            start (int): front back edge of the yard

        Returns:
            Boolean: True if the player lost false otherwise
        """
        for z in self._yard.get_zombies_group().sprites():
            if z.get_rect().midright[0] < start:
                self._player.set_final_status(False)
                return True
        return False
    
    def check_if_won(self): #checks if player has won the game
        """checks if the player won the game

        Returns:
            Boolean: True if the player won, false otherwise
        """
        res = not self._yard.any_zombies_left() and self._is_end_game
        if res:
            self._player.set_final_status(True)
        return res

    def end_game(self, x): #ends the game if either condition is true
        """checks if the player has won or lost and ends the game

        Args:
            x (int): back edge of the yard

        Returns:
            Boolean: True if the game should end, false otherwise
        """
        return self.check_if_lost(x) or self.check_if_won()

    def zombies_enter_yard(self): #adds zombies increasing number based on zombies killed
        """makes zombies enter the yard 
        """
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
        """creates a zombie, creating stronger zombies 
        based on the current progression of the level

        Args:
            pos (tuple[int]): the position to place the zombie at

        Returns:
            Zombie: the zombie to be added to the yard
        """
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
        """creates a single zombie

        Returns:
            Zombie: a single zombie
        """
        self._zombies_made += 1
        x = 1225
        y = random.sample([240, 370, 505, 635, 760], 1)[0]

        return self.produce_zombie((x, y - 5))

    def make_mini_z_wave(self): #makes 2-3 zombies
        """creates 2-3 zombies to be added to the yard 
        based on current progression of the level

        Returns:
            list[Zombie]: the zombies to be added to the yard
        """
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
        """creates a wave of 5 zombies to be added to the yard

        Returns:
            list[Zombie]: 5 zombies to be added to the yard
        """
        x = random.sample(range(1225, 1260), 5)
        y = [250, 380, 515, 635, 760]
        self._zombies_made += 5
        
        return [self.produce_zombie((x[i], y[i] - 5)) for i in range(5)]
    
    def make_medium_z_wave(self): #makes 10 zombies at once
        """creates a wave of 10 zombies

        Returns:
            list[Zombie]: the zombies to be added to the yard
        """
        x = random.sample(range(1225, 1250), 10)
        y = [240, 370, 505, 635, 760]
        self._zombies_made += 10
        
        return [self.produce_zombie((x[i], y[i % 5] - 5)) for i in range(10)]
    
    def make_final_z_wave(self): #makes 20 zombies at once
        """creates the final wave of zombies, making 15

        Returns:
            list[Zombie]: the zombies to be added to the yard
        """
        x = random.sample(range(1225, 1260), 15)
        y = [240, 370, 505, 635, 760]
        self._zombies_made += 15
        self._is_end_game = True
        return [self.produce_zombie((x[i], y[i % 5] - 5)) for i in range(15)]