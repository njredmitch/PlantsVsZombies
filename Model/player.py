class Player:

    def __init__(self) -> None:
        self._sun = 50
        self._plant = None
        


    def store_plant(self, plant):
        self._plant = self.plant_to_store(plant)
    
    def remove_plant(self):
        self._plant = None

    def spend_sun(self, val):
        self._sun -= val
    
    def gain_sun(self, val):
        self._sun += val
    
    def plant_to_store(self, key):
        if key == 'FP':
            self._plant = 'flameshooter'
        elif key == 'IP':
            self._plant = 'iceshooter'
        elif key == 'GP':
            self._plant = 'greenshooter'
        elif key == 'W':
            self._plant = 'walnut'
        elif key == 'SF':
            self._plant = 'sunflower'

    def get_sun(self):
        return self._sun

