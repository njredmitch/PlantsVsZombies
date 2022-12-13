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
from Model.GameObjects.shovel import ShovelBlock as SB

class FrontYard:
    """Represents the front yard of a house, stores all game objects
    """
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
        self._shovel_group = pygame.sprite.GroupSingle(SB((150, 0)))
        self._active = pygame.sprite.GroupSingle()

    def initialize_game_squares_group(self):
        """initializes all of the games sqaure sprites to be added to a group

        Returns:
            list[GameSquare]: the gamesqaures to be added to the group
        """
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
        """creates a dict[Gamesqaure : Plant] to pair each 
        plant with the gamesqaure it is placed on

        Returns:
            dict[Gamesqaure : Plant]: the gamesqaures paired with no plants
        """
        yard = {}
        for g in self._game_sqaures_group.sprites():
            yard[g]  = None
        
        return yard
    
    def initialize_shop(self):
        """initializes the plant shops

        Returns:
            list[PlantShop]: the plant shops to be stored
        """
        shop = [PlantShop('PlantsVsZombies\GamePNGS\Sunflower_Shop.png',
                          'PlantsVsZombies\GamePNGS\Sunflower_Closed_Shop.png',(0, 30), 50, S((0, 30)), 8, True),
                PlantShop('PlantsVsZombies\GamePNGS\Walnut_Shop.png', 
                          'PlantsVsZombies\GamePNGS\Walnut_Closed_Shop.png', (0, 90), 50, W((0, 90)), 15, True),
                PlantShop('PlantsVsZombies\GamePNGS\Peashooter_Shop.png', 
                          'PlantsVsZombies\GamePNGS\Peashooter_Closed_Shop.png', (0, 150), 100, GS((0, 150)), 8, True),
                PlantShop('PlantsVsZombies\GamePNGS\Iceshooter_Shop.png', 
                          'PlantsVsZombies\GamePNGS\Iceshooter_Closed_Shop.png', (0, 210), 175, IS((0, 210)), 8, False),
                PlantShop('PlantsVsZombies\GamePNGS\Flameshooter_Shop.png', 
                          'PlantsVsZombies\GamePNGS\Flameshooter_Closed_Shop.png', (0, 270), 200, FS((0, 270)), 8, False)]
        return shop
    
    def any_zombies_left(self):
        """checks if any zombies are left in the yard

        Returns:
            Boolean: True zombies are in the yard, false otherwise
        """
        for row in self._zombies:
            if len(row) > 0:
                return True
        return False
        
    def add_plant(self, plant : Plant, square):
        """adds a plant to the yard, adding each plant 
        to the necessary containers

        Args:
            plant (Plant): the plant to be added
            square (GameSquare): the game sqaure to pair with the plant
        """
        if isinstance(plant, PS):
            self._plants_group.add(plant)
            self._peashooters[self.get_peashooter_row(plant)].append(plant)
        elif isinstance(plant, S):
            self._sunflowers.append(plant)
            self._plants_group.add(plant)
        else:
            self._plants_group.add(plant)
        self._game_sqaures[square] = plant
        self._active.remove(plant)

    def add_zombie(self, z : Zombie):
        """add(s) zombie(s) to the yard, adding a 
        zombie to the necessary containers

        Args:
            z (Zombie/list[Zombie]): The zombie(s) to be added to the yard
        """
        if isinstance(z, list):
            for z in z:
                self._zombies[self.get_zombie_row(z)].append(z)
                self._zombie_group.add(z)
        else:
            self._zombies[self.get_zombie_row(z)].append(z)
            self._zombie_group.add(z)

    def add_sun(self, s : Sun):
        """adds a sun object to the yard

        Args:
            s (Sun): the sun object to be added
        """
        self._sun_group.add(s)

    def remove_plant(self, plant : Plant, square):
        """removes a plant from the yard

        Args:
            plant (Plant): the plant to remove
            square (_type_): the game sqaure paired with the plant
        """
        if isinstance(plant, PS):
            self._peashooters[self.get_peashooter_row(plant)].remove(plant)
        if isinstance(plant, S):
            self._sunflowers.remove(plant)
        self._game_sqaures[square] = None
        plant.kill()
        
    def remove_zombie(self, z : Zombie):
        """removes a zombie from the yard

        Args:
            z (Zombie): the zombie to remove
        """
        self._zombies[self.get_zombie_row(z)].remove(z)
        z.kill()
    
    def remove_projectile(self, p : Projectile):
        """removes a projectile from the yard

        Args:
            p (Projectile): the projectile to remove
        """
        self._projectile_group.remove(p)
    
    def remove_sun(self, s : Sun):
        """removes sun from the yard

        Args:
            s (Sun): the sun to remove
        """
        s.kill()

    def get_peashooter_row(self, ps : PS):
        """finds the row a peashooter should be placed/is in

        Args:
            ps (PS): the peashooter to check

        Returns:
            int: the row the peashooter is in
        """
        return ps.get_position()[1]//145 - 1
    
    def get_zombie_row(self, z : Zombie):
        """finds the row the zombie is/should be located at

        Args:
            z (Zombie): the zombie to check

        Returns:
            int: the row
        """
        return z.get_position()[1]//150 - 1

    def get_plants(self):
        """returns all the plants currently in the yard

        Returns:
            Group: the Group container storing all the plants
        """
        return self._plants_group
    
    def get_zombies(self):
        """returns the zombies in the yard

        Returns:
            List[List[Zombie]]: the matrix storing the zombies
        """
        return self._zombies
    
    def get_zombies_group(self):
        """returns the zombies in the yard

        Returns:
            Group: the Group container storing all the zombies
        """
        return self._zombie_group
    
    def get_projectiles(self):
        """returns all the projectiles in the yard

        Returns:
            Group: the group storing all the projectiles
        """
        return self._projectile_group
    
    def get_peashooters(self):
        """returns all the peashooters in the yard

        Returns:
            List[List[Peashooters]]: the matrix storing peashooters
        """
        return self._peashooters
    
    def get_sunflowers(self):
        """returns all the sunflowers in the yard

        Returns:
            list[Sunflower]: the list storing the sunflowers
        """
        return self._sunflowers

    def get_sun(self):
        """returns the sun currently in the yard

        Returns:
            Group: the group storing all of the sun objects
        """
        return self._sun_group
    
    def get_game_squares(self):
        """returns all of the gamesqaure, plant pairs of the yard

        Returns:
            Dict[Gameqaure : Plant]: the gamesqaure plant pairs of the yard
        """
        return self._game_sqaures

    def get_game_sqaures_group(self):
        """returns all of the game sqaure objects in the yard

        Returns:
            Group: the gamesqaure objects located in the yard
        """
        return self._game_sqaures_group

    def get_shop_group(self):
        """returns all of the plant shops 

        Returns:
            Group: the group storing the plant shops
        """
        return self._shop_group

    def get_shovel_group(self):
        """returns the shovel block the player can get the shovel from

        Returns:
            _type_: _description_
        """
        return self._shovel_group
    
class GameSquare(pygame.sprite.Sprite):
    """Represents a single sqaure found in the yard
    """
    def __init__(self, width, height, x, y) -> None:

        super().__init__()
        self._pos = (x, y)
        self.image = pygame.Surface((width,height))
        self.image.set_alpha(0)
        self.rect = self.image.get_rect(midbottom=self._pos)
    
    def get_rect(self):
        """gets the rectangle of the GameSquare

        Returns:
            Rectangle: the rectangle of the Gamesqaure
        """
        return self.rect

    def get_pos(self):
        """Gets the position of the game square

        Returns:
            tuple(int): the x,y position of the game sqaure
        """
        return self._pos