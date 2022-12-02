from Plants.peashooter import Peashooter as PS
from Plants.flameshooter import Flameshooter as FS
from Plants.iceshooter import Iceshooter as IS
from Plants.green_peashooter import GreenPeashooter as GS
from Plants.walnut import Walnut as W
from Plants.sunflower import Sunflower as S

class Player:

    def __init__(self) -> None:
        self._sun = 50
        self._plant = None
        self._final_status = None

    def store_plant(self, plant):
        self._plant = self.plant_to_store(plant)

    def spend_sun(self, val):
        self._sun -= val
    
    def gain_sun(self, val):
        self._sun += val
    
    def plant_to_store(self, key, pos):
        if key == 'FP':
            self._plant = FS(pos)
        elif key == 'IP':
            self._plant = IS(pos)
        elif key == 'GP':
            self._plant = GS(pos)
        elif key == 'W':
            self._plant = W(pos)
        elif key == 'SF':
            self._plant = S(pos)
    def has_plant(self):
        return self._plant != None

    def set_final_status(self, fin):
        self._final_status = fin

    def get_final_status(self):
        return self._final_status

    def get_plant(self):
        return self._plant

    def get_sun(self):
        return self._sun
    

