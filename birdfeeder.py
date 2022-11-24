from random import random


class Birdfeeder: 
    dice = {"wheat_dice" : 0,
            "worm_dice" : 0,
            "berry_dice" : 0,
            "mouse_dice" : 0,
            "fish_dice" : 0,
            "wheat_worm_dice" : 0}
    
    can_reroll = False
    
    def reroll(self):
        for key in self.dice.keys():
            self.dice[key] = 0
            
        for _ in range(6):
            self.dice[random.choice(list(self.dice.keys()))] +=1
            
    def __init__(self) -> None:
        self.reroll()