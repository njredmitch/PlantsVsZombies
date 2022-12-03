import pygame
from Model.logic import Logic
from View.graphics import Graphics

class Game:

    def __init__(self, logic : Logic, graphics : Graphics) -> None:
        self._logic = logic
        self._graphics = graphics
    
    def run_game(self):
        pass

