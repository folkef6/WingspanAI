from typing import List
from board import Board
#from game import Game

class Player: 
    
    def __init__(self, game, number) -> None:
        self.game = game

        # Cards:
        self.bird_cards    = []
        self.mission_cards = []
        
        # Food:
        self.wheat = 0
        self.worm  = 0
        self.berry = 0
        self.fish  = 0 
        self.mouse = 0
        
        # Board
        self.board = Board()
        
        # Misc: 
        self.player_number = number
        self.score = 0
        
    
    def gain_food_supply(self, wheat:int, worm:int,
                         berry:int, fish:int, 
                         mouse:int) -> None:
        
        self.wheat += wheat
        self.worm  += worm
        self.berry += berry
        self.fish  +=  fish
        self.mouse += mouse
    
    def gain_food_birdfeeder(self) -> None:
        pass
    
    def play_turn(self) -> None: 
        print()