from enum import Enum
from helper_classes import *
from typing import List, Callable
from player import Player

class Bird:
    
    def __init__(self, owner:Player, name:str, points:int,
                 nest:Nest, habitats: List[Habitat],
                 max_eggs:int, function_type:Function_types,
                 function: Callable, worm_cost: int,
                 berry_cost:int, wheat_cost:int, 
                 mouse_cost:int, fish_cost) -> None:
        self.name = name
        self.points = points
        self.nest = nest
        self.habitats = habitats
        self.max_eggs = max_eggs
        self.function_type = function_type
        self.function = function
        self.eggs = 0
        self.is_played = False
        self.worm_cost = worm_cost
        self.berry_cost = berry_cost
        self.wheat_cost = wheat_cost
        self.mouse_cost = mouse_cost
        self.fish_cost = fish_cost
        
    
    def activate_function(self):
        self.function()
    
    def lay_eggs(self, amount: int):
        assert self.eggs + amount <= self.max_eggs
        
        self.eggs += amount
    
    
    