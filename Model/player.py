from Model.Plants.flame_shooter import Flameshooter as FS
from Model.Plants.ice_shooter import Iceshooter as IS
from Model.Plants.green_shooter import GreenPeashooter as GS
from Model.Plants.walnut import Walnut as W
from Model.Plants.sunflower import Sunflower as S

class Player:

    def __init__(self) -> None:
        self._sun = 50
        self._plant = None
        self._shovel = None
        self._final_status = None

    def store_plant(self, plant):
        self._plant = plant

    def spend_sun(self, val):
        self._sun -= val
    
    def gain_sun(self, val):
        self._sun += val
    
    def has_plant(self):
        return self._plant != None

    def has_shovel(self):
        return self._shovel != None

    def set_shovel(self, sh):
        self._shovel = sh

    def set_final_status(self, fin):
        self._final_status = fin

    def get_final_status(self):
        return self._final_status

    def get_plant(self):
        return self._plant

    def get_shovel(self):
        return self._shovel

    def get_sun(self):
        return self._sun