from Model.Plants.flame_shooter import Flameshooter as FS
from Model.Plants.ice_shooter import Iceshooter as IS
from Model.Plants.green_shooter import GreenPeashooter as GS
from Model.Plants.walnut import Walnut as W
from Model.Plants.sunflower import Sunflower as S

class Player:
    """represents a player of the game
    """
    def __init__(self) -> None:
        """intializes the player
        """
        self._sun_bank = 50
        self._plant = None
        self._shovel = None
        self._final_status = None

    def store_plant(self, plant):
        """stores a plant in the players plant inventory

        Args:
            plant (Plant): the plant to store
        """
        self._plant = plant

    def spend_sun(self, val):
        """decreases the sun from the players sun bank

        Args:
            val (int): the sun spent
        """
        self._sun_bank -= val
    
    def gain_sun(self, val):
        """the sun to add the the players sun bank

        Args:
            val (int): the sun gained
        """
        self._sun_bank += val
    
    def has_plant(self):
        """checks if the player has a plant in their plant inventory

        Returns:
            bool: True if they have a plant, False otherwise
        """
        return self._plant != None

    def has_shovel(self):
        """checks if the player has a shovel in their shovel inventory

        Returns:
            bool: True if the have a shovel, false otherwise
        """
        return self._shovel != None

    def set_shovel(self, sh):
        """sets the players shovel to either a shovel or None

        Args:
            sh (Shovel/None): either a Shovel or None
        """
        self._shovel = sh

    def set_final_status(self, fin):
        """sets the final status of the player

        Args:
            fin (bool): True if the player won, False otherwise
        """
        self._final_status = fin

    def get_final_status(self):
        """gets the players final status

        Returns:
            bool/None: True if the player won, False if the player lost, or none if the game hasn't ended
        """
        return self._final_status

    def get_plant(self):
        """returns the plant in the players inventory

        Returns:
            Plant/None: a plant if the player has a plant, None if they don't have a plant
        """
        return self._plant

    def get_shovel(self):
        """gets the shovel invetory of the player

        Returns:
            Shovel/None: a shovel if the player has a shovel, None if they don't
        """
        return self._shovel

    def get_sun(self):
        """returns the sun the player has

        Returns:
            int: the amount of sun
        """
        return self._sun_bank