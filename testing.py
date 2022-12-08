import unittest
import pygame
import schedule

from Model.Plants.plant import Plant
from Model.Plants.peashooter import Peashooter as PS
from Model.Plants.flame_shooter import Flameshooter as FS 
from Model.Plants.green_shooter import GreenPeashooter as GS 
from Model.Plants.ice_shooter import Iceshooter as IS 
from Model.Plants.sunflower import Sunflower as SF 
from Model.Plants.walnut import Walnut as W 

from Model.Zombies.zombie import Zombie
from Model.Zombies.grunt_zombie import GruntZombie as GZ
from Model.Zombies.cone_zombie import ConeZombie as CZ
from Model.Zombies.bucket_zombie import BucketZombie as BZ

from Model.Projectiles.projectile import Projectile
from Model.Projectiles.pea import Pea
from Model.Projectiles.flame_pea import FlamePea as FP
from Model.Projectiles.ice_pea import IcePea as IP
from Model.Projectiles.green_pea import GreenPea as GP

from Model.GameObjects.sun import Sun
from Model.GameObjects.plant_shop import PlantShop as Shop
from Model.GameObjects.shovel import ShovelBlock as SB
from Model.GameObjects.shovel import Shovel as SH

from Model.front_yard import GameSquare as Sqaure
from Model.player import Player

class TestGame(unittest.TestCase):
    def test_plants(self):
        fs = FS((0,0))
        gs = GS((0,0))
        ice = IS((0,0))
        w = W((0,0))
        sf = SF((0,0))
        #testing Sunflower
        self.assertIsInstance(sf, SF)
        self.assertIsInstance(sf, Plant)
        self.assertNotIsInstance(sf, W)
        self.assertNotIsInstance(sf, PS)
        self.assertNotIsInstance(sf, FS)
        self.assertNotIsInstance(sf, GS)
        self.assertNotIsInstance(sf, IS)
        self.assertEqual(sf.get_position(), (0,0))
        self.assertEqual(sf.get_health(), 120)
        sf.lose_health(20)
        self.assertEqual(sf.get_health(), 100)
        #testing Walnut
        self.assertIsInstance(w, W)
        self.assertIsInstance(w, Plant)
        self.assertNotIsInstance(w, SF)
        self.assertNotIsInstance(w, PS)
        self.assertNotIsInstance(w, FS)
        self.assertNotIsInstance(w, GS)
        self.assertNotIsInstance(w, IS)
        self.assertEqual(w.get_position(), (0,0))
        self.assertEqual(w.get_health(), 1440)
        w.lose_health(20)
        self.assertEqual(w.get_health(), 1420)
        #testing FlameShooter
        self.assertIsInstance(fs, FS)
        self.assertIsInstance(fs, PS)
        self.assertIsInstance(fs, Plant)
        self.assertNotIsInstance(fs, W)
        self.assertNotIsInstance(fs, SF)
        self.assertNotIsInstance(fs, GS)
        self.assertNotIsInstance(fs, IS)
        self.assertEqual(fs.get_position(), (0,0))
        self.assertEqual(fs.get_health(), 120)
        fs.lose_health(20)
        self.assertEqual(fs.get_health(), 100)
        #testing IceShooter
        self.assertIsInstance(ice, IS)
        self.assertIsInstance(ice, PS)
        self.assertIsInstance(ice, Plant)
        self.assertNotIsInstance(ice, W)
        self.assertNotIsInstance(ice, SF)
        self.assertNotIsInstance(ice, GS)
        self.assertNotIsInstance(ice, FS)
        self.assertEqual(ice.get_position(), (0,0))
        self.assertEqual(ice.get_health(), 120)
        ice.lose_health(20)
        self.assertEqual(ice.get_health(), 100)
        #testing GreenPeashooter
        self.assertIsInstance(gs, GS)
        self.assertIsInstance(gs, PS)
        self.assertIsInstance(gs, Plant)
        self.assertNotIsInstance(gs, W)
        self.assertNotIsInstance(gs, SF)
        self.assertNotIsInstance(gs, FS)
        self.assertNotIsInstance(gs, IS)
        self.assertEqual(gs.get_position(), (0,0))
        self.assertEqual(gs.get_health(), 120)
        gs.lose_health(20)
        self.assertEqual(gs.get_health(), 100)
        #testing Peashooter
        fs.prime()
        gs.prime()
        ice.prime()
        self.assertTrue(fs.is_primed())
        self.assertTrue(gs.is_primed())
        self.assertTrue(ice.is_primed())
        fs.unprime()
        gs.unprime()
        ice.unprime()
        self.assertFalse(fs.is_primed())
        self.assertFalse(gs.is_primed())
        self.assertFalse(ice.is_primed())
    
    def test_zombies(self):
        gz = GZ((200,0))
        cz = CZ((0,0))
        bz = BZ((0,0))
        #testing Grunt Zombie
        self.assertIsInstance(gz, GZ)
        self.assertIsInstance(gz, Zombie)
        self.assertNotIsInstance(gz, CZ)
        self.assertNotIsInstance(gz, BZ)
        self.assertEqual(gz.get_health(), 200)
        self.assertEqual(gz.get_attack_dmg(), 20)
        #testing Cone Zombie
        self.assertIsInstance(cz, CZ)
        self.assertIsInstance(cz, Zombie)
        self.assertNotIsInstance(cz, GZ)
        self.assertNotIsInstance(cz, BZ)
        self.assertEqual(cz.get_health(), 640)
        self.assertEqual(cz.get_attack_dmg(), 20)
        #testing Bucket Zombie
        self.assertIsInstance(bz, BZ)
        self.assertIsInstance(bz, Zombie)
        self.assertNotIsInstance(bz, GZ)
        self.assertNotIsInstance(bz, CZ)
        self.assertEqual(bz.get_health(), 1380)
        self.assertEqual(bz.get_attack_dmg(), 20)
        #testing general Zombie
        self.assertEqual(gz.get_position(), (200,0))
        gz.freeze()
        self.assertTrue(gz.get_slowed_status())
        gz.thaw()
        self.assertFalse(gz.get_slowed_status())
        self.assertTrue(gz.get_movement_status())
        gz.set_movement_status(False)
        self.assertFalse(gz.get_movement_status())
        gz.lose_health(20)
        self.assertEqual(gz.get_health(), 180)
        gz.update_xpos(10)
        self.assertEqual(gz.get_position(), (190, 0))
    
    def test_projectiles(self):
        fp = FP((0,0))
        ip = IP((0,0))
        gp = GP((0,0))
        #test FlamePea
        self.assertIsInstance(fp, FP)
        self.assertIsInstance(fp, Pea)
        self.assertIsInstance(fp, Projectile)
        self.assertNotIsInstance(fp, IP)
        self.assertNotIsInstance(fp, GP)
        self.assertEqual(fp.get_dmg(), 40)
        #test IcePea
        self.assertIsInstance(ip, IP)
        self.assertIsInstance(ip, Pea)
        self.assertIsInstance(ip, Projectile)
        self.assertNotIsInstance(ip, FP)
        self.assertNotIsInstance(ip, GP)
        self.assertEqual(ip.get_dmg(), 20)
        #test FlamePea
        self.assertIsInstance(gp, GP)
        self.assertIsInstance(gp, Pea)
        self.assertIsInstance(gp, Projectile)
        self.assertNotIsInstance(gp, IP)
        self.assertNotIsInstance(gp, FP)
        self.assertEqual(gp.get_dmg(), 20)
        #test general Projectile
        self.assertEqual(fp.get_pos(), (0,0))
        fp.update_xpos(10)
        self.assertEqual(fp.get_pos(), (10,0))

    def test_player(self):
        player = Player()
        self.assertEqual(player.get_sun(), 50)
        self.assertIsNone(player.get_final_status())
        self.assertIsNone(player.get_plant())
        self.assertIsNone(player.get_shovel())
        player.store_plant(SF((0,0)))
        self.assertIsInstance(player.get_plant(), SF)
        player.store_plant(None)
        player.set_shovel(SH((0,0)))
        self.assertIsInstance(player.get_shovel(), SH)
        player.gain_sun(200)
        self.assertEqual(player.get_sun(), 250)
        player.spend_sun(175)
        self.assertEqual(player.get_sun(), 75)
        player.set_final_status(True)
        self.assertTrue(player.get_final_status())
        player.set_final_status(False)
        self.assertFalse(player.get_final_status())

    def test_shovel_block(self):
        block = SB((0,0))
        self.assertIsInstance(block.get_shovel(), SH)

    def test_shop(self):
        sf_shop = Shop('PlantsVsZombies\GamePNGS\Sunflower_Shop.png',
                        'PlantsVsZombies\GamePNGS\Sunflower_Closed_Shop.png',(0, 30), 50, SF((0, 30)), 8, True)
        fs_shop = Shop('PlantsVsZombies\GamePNGS\Flameshooter_Shop.png', 
                        'PlantsVsZombies\GamePNGS\Flameshooter_Closed_Shop.png', (0, 270), 200, FS((0, 270)), 8, False)
        self.assertEqual(sf_shop.get_cost(), 50)
        self.assertTrue(sf_shop.is_open())
        sf_shop.close()
        self.assertFalse(sf_shop.is_open())
        sf_shop.open()
        self.assertTrue(sf_shop.is_open())
        self.assertIsInstance(sf_shop.get_plant(), SF)
        self.assertEqual(fs_shop.get_cost(), 200)
        self.assertFalse(fs_shop.is_open())
        fs_shop.open()
        self.assertTrue(fs_shop.is_open())
        fs_shop.close()
        self.assertFalse(fs_shop.is_open())
        self.assertIsInstance(fs_shop.get_plant(), FS)

    def test_sun(self):
        sun = Sun((100,100))
        
        self.assertIn(sun._pos, [(100 + 40, 100 - 60),
                                 (100 + 40, 100 + 30),
                                 (100 - 40, 100 - 60),
                                 (100 - 40, 100 + 30)])
    
    def test_game_square(self):
        gs = Sqaure(85, 145, 335, 240)
        self.assertEqual(gs.get_pos(), (335,240))
    

testor = TestGame()
testor.test_plants()
testor.test_zombies()
testor.test_projectiles()
testor.test_player()
testor.test_shop()
testor.test_shovel_block()
testor.test_sun()
testor.test_game_square()
