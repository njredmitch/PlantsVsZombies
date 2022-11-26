class Player:

    def __init__(self) -> None:
        self._sun = 50
        self._plant = None
        


    def store_plant(self, plant):
        self._plant = plant
    
    def remove_plant(self):
        self._plant = None

    def spend_sun(self, val):
        self._sun -= val
    
    def gain_sun(self, val):
        self._sun += val

