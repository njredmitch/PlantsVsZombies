import pygame
from Plants.plant import Plant
from Zombies.zombie import Zombie
from Projectiles.projectile import Projectile
from GameObjects.sun import Sun
from Model.player import Player
from plant_shop import PlantShop

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

class FrontYard:

    def __init__(self) -> None:
        super().__init__()
        self._zombies = [[] ] * 5
        self._peashooters = [[]] * 5
        self._game_sqaures = self.initialize_game_sqaures()
        self._game_sqaures_group = self.initialize_game_squares_group()
        self._plants_group = pygame.sprite.Group()
        self._zombie_group = pygame.sprite.Group()
        self._projectile_group = PS.peas
        self._sun_group = pygame.sprite.Group()
        self._square_group = self.initialize_sqaure_group()
        self._shop_group = pygame.sprite.Group()
 
    def initialize_game_squares_group(self):
        return [GameSquare(85, 145, 335, 240),
                              GameSquare(85, 145, 425, 240),
                              GameSquare(95, 145, 520, 240),
                              GameSquare(85, 145, 615, 240),
                              GameSquare(85, 145, 705, 240),
                              GameSquare(85, 145, 795, 240),
                              GameSquare(85, 145, 885, 240),
                              GameSquare(85, 145, 975, 240),
                              GameSquare(85, 145, 1065, 240),
                              GameSquare(85, 125, 335, 370),
                              GameSquare(85, 125, 425, 370),
                              GameSquare(95, 125, 520, 370),
                              GameSquare(85, 125, 615, 370),
                              GameSquare(85, 125, 705, 370),
                              GameSquare(85, 125, 795, 370),
                              GameSquare(85, 125, 885, 370),
                              GameSquare(85, 125, 975, 370),
                              GameSquare(105, 125, 1065, 370),
                              GameSquare(85, 130, 335, 505),
                              GameSquare(85, 130, 425, 505),
                              GameSquare(95, 130, 520, 505),
                              GameSquare(85, 130, 615, 505),
                              GameSquare(85, 130, 705, 505),
                              GameSquare(85, 130, 795, 505),
                              GameSquare(85, 130, 885, 505),
                              GameSquare(85, 130, 975, 505),
                              GameSquare(105, 130, 1065, 505),
                              GameSquare(85, 120, 335, 625),
                              GameSquare(85, 120, 425, 625),
                              GameSquare(95, 120, 520, 625),
                              GameSquare(85, 120, 615, 625),
                              GameSquare(85, 120, 705, 625),
                              GameSquare(85, 120, 795, 625),
                              GameSquare(85, 120, 885, 625),
                              GameSquare(85, 120, 975, 625),
                              GameSquare(105, 120, 1065, 625),
                              GameSquare(90, 145, 335, 760),
                              GameSquare(85, 145, 425, 760),
                              GameSquare(95, 145, 520, 760),
                              GameSquare(85, 145, 615, 760),
                              GameSquare(85, 145, 705, 760),
                              GameSquare(85, 145, 795, 760),
                              GameSquare(85, 145, 885, 760),
                              GameSquare(85, 145, 975, 760),
                              GameSquare(105, 145, 1065, 760)]
    
    def initialize_game_sqaures(self):
        yard = {}
        for g in self._game_sqaures_group():
            yard[g]  = None
        
        return yard

    def initialize_sqaure_group(self):
        t = pygame.sprite.Group
        for s in self._game_sqaures:
            t.add(s)

        return t    
    
    def initialize_shop(self):
        self._shop_group = pygame.sprite.Group
        self._shop_group.add(PlantShop('PlantsVsZombies\GamePNGS\Sunflower_Shop.png', (0, 100), 50, 'SF'))
        self._shop_group.add(PlantShop('PlantsVsZombies\GamePNGS\Walnut_Shop.png', (0, 160), 50, 'W'))
        self._shop_group.add(PlantShop('PlantsVsZombies\GamePNGS\Peashooter_Shop.png', (0, 220), 100, 'GP'))
        self._shop_group.add(PlantShop('PlantsVsZombies\GamePNGS\Iceshooter_Shop.png', (0, 280), 175, 'IP'))
        self._shop_group.add(PlantShop('PlantsVsZombies\GamePNGS\Flameshooter_Shop.png', (0, 340), 200, 'FP'))
    
    def any_zombies_left(self):
        for row in self._zombies:
            if len(row) > 0:
                return False
        return True
        
    def add_plant(self, plant : Plant):
        if isinstance(plant, PS):
            self._plants_group.add(plant)
            self._peashooters[self.get_peashooter_index(plant)].append(plant)
        else:
            self._plants_group.add(plant)
    
    def add_zombie(self, z : Zombie):
        if isinstance(z, list):
            for z in z:
                self._zombies[self.get_zombie_index(z)].append(z)
                self._zombie_group.add(z)
        else:
            self._zombies[self.get_zombie_index(z)].append(z)
            self._zombie_group.add(z)
            
    def add_sun(self, s : Sun):
        self._sun_group.add(s)

    def remove_plant(self, plant : Plant):
        if isinstance(plant, PS):
            self._peashooters[self.get_peashooter_index(plant)].pop(plant)
            self._plants_group.remove(plant)
        else:
            self._plants_group.remove(plant)
    
    def remove_zombie(self, z : Zombie):
        self._zombies[self.get_zombie_index(z)].pop(z)
        self._zombie_group.remove(z)
    
    def remove_projectile(self, p : Projectile):
        self._projectile_group.remove(p)
    
    def remove_sun(self, s : Sun):
        self._sun_group.remove(s)

    def get_peashooter_index(self, ps : PS):
        return ps.get_position()[1]//150
    
    def get_zombie_index(self, z : Zombie):
        return z.get_position()[1]//150

    def get_plants(self):
        return self._plants_group
    
    def get_zombies(self):
        return self._zombies
    
    def get_zombies_group(self):
        return self._zombie_group
    
    def get_projectiles(self):
        return self._projectile_group
    
    def get_peashooters(self):
        return self._peashooters
    
    def get_sun(self):
        return self._sun_group
    
    def get_game_squares(self):
        return self._game_sqaures

    def get_game_sqaures_group(self):
        return self._game_sqaures
    
    def get_groups(self):
        return [self._plants_group, self._zombie_group, self._projectile_group, self._sun_group, self._square_group, self._shop_group]
    
class GameSquare(pygame.sprite.Sprite):

    def __init__(self, width, height, x, y) -> None:
        super().__init__()
        self._pos = (x, y)
        self.image = pygame.Surface((width,height))
        self.image.set_alpha(0)
        self.rect = self.image.get_rect(midbottom=self._pos)
    
    def get_pos(self):
        return self._pos
    
    