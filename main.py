from Model.logic import Logic
from View.graphics import Graphics
from Controller.game import Game

game_logic = Logic()
game_graphics = Graphics(game_logic._yard, game_logic._player)
game_controller = Game(game_logic, game_graphics)