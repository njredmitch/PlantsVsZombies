from abc import ABC
from Model.Projectiles.projectile import Projectile

class Pea(Projectile, ABC):

    def __init__(self, position, dmg, path) -> None:
        Projectile.__init__(self, position, dmg, path)
        ABC.__init__(self)