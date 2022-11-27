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
        print(f"\nPlayer{self.player_number}'s Turn:\n")
        self.display_inventory()
        
        
        
    
    def first_turn(self, deck) -> None: 
        print(f"Player{self.player_number}'s selection:")
        bird_cards = [list.pop(deck) for _ in range(5)]
        print("Birdcards:")
        for bird in bird_cards: 
            print(bird.name)
        print("\nFood choices: worm, berry, wheat, fish, mouse")
        i = 0
        while(i < 5):
            choice = input()
            
            matching_bird=False
            for bird in bird_cards:
                if choice == bird.name:
                    self.bird_cards.append(bird)
                    i+=1
                    matching_bird=True
            if matching_bird:
                continue
            if choice == "worm" or choice == "Worm":
                self.worm += 1
                i+=1
                continue
            if choice == "wheat" or choice == "Wheat":
                self.wheat += 1
                i+=1
                continue
            if choice == "berry" or choice == "Berry":
                self.berry += 1
                i+=1
                continue
            if choice == "fish" or choice == "Fish":
                self.fish += 1
                i+=1
                continue
            if choice == "mouse" or choice == "Mouse":
                self.mouse += 1
                i+=1
                continue
            print("No matching choice")
        
        self.display_inventory()

    def display_inventory(self):
        print("Players bird-cards:")
        print(self.bird_cards)
        print("Players food:")
        print(f"Worms: {self.worm}\n"+ f"Wheat: {self.wheat}\n"+ 
              f"Berries: {self.berry}\n"+ f"Fish: {self.fish}\n"+
              f"Mice: {self.mouse}\n")