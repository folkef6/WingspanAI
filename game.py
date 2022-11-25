from birdfeeder import Birdfeeder
from board import Board
from player import Player

ROUNDS = [8,7,6,5]

class Game:
    
    
    
    def __init__(self, players:int) -> None:
        self.deck = []
        assert players <= 5
        self.players = [Player(self, number) for i in range(players)]
        self.bird_cards = []
        self.birdfeeder = Birdfeeder()
        
    def new_bird_cards(self) -> None: 
        pass
        
    def game(self) -> None:
        for round in ROUNDS:
            self.birdfeeder.reroll()
            self.new_bird_cards()
            
            for turn in round: 
                for player in self.players:
                    pass