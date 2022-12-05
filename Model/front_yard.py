import pygame

from Model.Plants.plant import Plant
from Model.Plants.peashooter import Peashooter as PS
from Model.Plants.flame_shooter import Flameshooter as FS 
from Model.Plants.green_shooter import GreenPeashooter as GS 
from Model.Plants.ice_shooter import Iceshooter as IS 
from Model.Plants.sunflower import Sunflower as S 
from Model.Plants.walnut import Walnut as W 

from Model.Zombies.zombie import Zombie
from Model.Projectiles.projectile import Projectile
from Model.GameObjects.sun import Sun
from Model.GameObjects.plant_shop import PlantShop

class FrontYard:

    def __init__(self) -> None:
        super().__init__()
        self._zombies = [[], [], [], [], []]
        self._peashooters = [[], [], [], [], []]
        self._sunflowers = []
        self._game_sqaures_group = pygame.sprite.Group(self.initialize_game_squares_group())
        self._game_sqaures = self.initialize_game_sqaures()
        self._plants_group = pygame.sprite.Group()
        self._zombie_group = pygame.sprite.Group()
        self._projectile_group = PS.peas
        self._sun_group = S.sun_group
        self._shop_group = pygame.sprite.Group(self.initialize_shop())
        self._unplaced = pygame.sprite.GroupSingle()

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
        for g in self._game_sqaures_group.sprites():
            yard[g]  = None
        
        return yard
    
    def initialize_shop(self):
        shop = [PlantShop('PlantsVsZombies\GamePNGS\Sunflower_Shop.png', (0, 30), 50, S((0, 30))),
                PlantShop('PlantsVsZombies\GamePNGS\Walnut_Shop.png', (0, 90), 50, W((0, 90))),
                PlantShop('PlantsVsZombies\GamePNGS\Peashooter_Shop.png', (0, 150), 100, GS((0, 150))),
                PlantShop('PlantsVsZombies\GamePNGS\Iceshooter_Shop.png', (0, 210), 175, IS((0, 210))),
                PlantShop('PlantsVsZombies\GamePNGS\Flameshooter_Shop.png', (0, 270), 200, FS((0, 270)))]
        return shop
    
    def any_zombies_left(self):
        for row in self._zombies:
            if len(row) > 0:
                return True
        return False
        
    def add_plant(self, plant : Plant):
        if isinstance(plant, PS):
            self._plants_group.add(plant)
            self._peashooters[self.get_peashooter_index(plant)].append(plant)
        elif isinstance(plant, S):
            self._sunflowers.append(plant)
            self._plants_group.add(plant)
        else:
            self._plants_group.add(plant)
        self._unplaced.remove(plant)
        print(plant.groups())
    
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
            self._peashooters[self.get_peashooter_index(plant)].remove(plant)
        if isinstance(plant, S):
            self._sunflowers.remove(plant)
        plant.kill()
        
    def remove_zombie(self, z : Zombie):
        print(f'removing {z}')
        self._zombies[self.get_zombie_index(z)].remove(z)
        z.kill()
    
    def remove_projectile(self, p : Projectile):
        self._projectile_group.remove(p)
    
    def remove_sun(self, s : Sun):
        s.kill()

    def get_peashooter_index(self, ps : PS):
        return ps.get_position()[1]//150 - 1
    
    def get_zombie_index(self, z : Zombie):
        print(z.get_position()[1]//150 - 1)
        return z.get_position()[1]//150 - 1

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
    
    def get_sunflowers(self):
        return self._sunflowers

    def get_sun(self):
        return self._sun_group
    
    def get_game_squares(self):
        return self._game_sqaures

    def get_game_sqaures_group(self):
        return self._game_sqaures_group

    def get_groups(self):
        return [self._plants_group, self._zombie_group, self._sun_group, self._projectile_group,  self._game_sqaures_group, self._shop_group]
    
class GameSquare(pygame.sprite.Sprite):

    def __init__(self, width, height, x, y) -> None:
        super().__init__()
        self._pos = (x, y)
        self.image = pygame.Surface((width,height))
        self.image.set_alpha(0)
        self.rect = self.image.get_rect(midbottom=self._pos)
    
    def get_rect(self):
        return self.rect
    def get_pos(self):
        return self._pos