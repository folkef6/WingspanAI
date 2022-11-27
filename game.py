from birdfeeder import Birdfeeder
from player import Player
import deck
from bird import Bird
ROUNDS = [8,7,6,5]

class Game:
    
    def __init__(self, players:int) -> None:
        self.deck = []
        assert players <= 5
        self.players = [Player(self, i) for i in range(players)]
        self.bird_cards = []
        self.birdfeeder = Birdfeeder()
        self.bird_deck = deck.get_bird_deck()
        
    def new_bird_cards(self) -> None: 
        self.bird_cards = [list.pop(self.bird_deck), list.pop(self.bird_deck), list.pop(self.bird_deck)]
        
    def game(self) -> None:
        round_number = 1
        for player in self.players:
            player.first_turn(self.bird_deck)
        
        for round in ROUNDS:
            print(f"Start of round {round_number} \n")
            round_number += 1
            self.birdfeeder.reroll()
            self.new_bird_cards()
            print("Cards in the birds-tray:")
            for bird in self.bird_cards:
                print(bird.name)
            print("\nDice in the birdfeeder:")
            self.birdfeeder.display_birdfeeder()    
            
            for turn in range(round): 
                for player in self.players:
                    pass