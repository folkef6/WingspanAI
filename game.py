from birdfeeder import Birdfeeder
from board import Board
from player import Player

ROUNDS = [8,7,6,5]

class Game:
    # Fix deck of bird cards
    deck = []
    
    def __init__(self, players:int) -> None:
        self.players = [Player(self) for i in range(players)]
        self.board = Board()
        self.bird_cards = []
        self.birdfeeder = Birdfeeder()
        
    def new_bird_cards(self) -> None: 
        pass
        
    def game(self) -> None:
        for round in ROUNDS:
            self.birdfeeder.reroll()
            
            for turn in round: 
                for player in self.players:
                    pass