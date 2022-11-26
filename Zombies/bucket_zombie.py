from zombie import Zombie

class BucketZombie(Zombie, pygame.sprite.Sprite):
    image_path = 'PlantsVsZombies\GamePNGS\Buckethead.png'

    def __init__(self, position) -> None:
        super().__init__(self, 600, position, 10, self.image_path)