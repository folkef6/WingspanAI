import random


class Birdfeeder: 

    
    def reroll(self):
        for key in self.dice.keys():
            self.dice[key] = 0
            
        for _ in range(6):
            self.dice[random.choice(list(self.dice.keys()))] +=1
            
    def display_birdfeeder(self):
        print( f"wheat_dice : { self.dice['wheat_dice'] } ,\n" +
            f"worm_dice : {self.dice['worm_dice']},\n" +
            f"berry_dice : {self.dice['berry_dice']},\n" +
            f"mouse_dice : {self.dice['mouse_dice']},\n" +
            f"fish_dice : {self.dice['fish_dice']},\n" +
            f"wheat_worm_dice : {self.dice['wheat_worm_dice']}")    
    
    def __init__(self) -> None:
        self.dice = {"wheat_dice" : 0,
                     "worm_dice" : 0,
                     "berry_dice" : 0,
                     "mouse_dice" : 0,
                     "fish_dice" : 0,
                     "wheat_worm_dice" : 0}
    
        self.can_reroll = False
        self.reroll()
        