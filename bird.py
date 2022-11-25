from enum import Enum
from helper_classes import *
from typing import List, Callable
from player import Player

class Bird:
    
    def __init__(self, owner:Player, EnglishName:str, VictoryPoints:int,
                 NestType:str, HabitatForest: bool, HabitatGrass: bool,
                 HabitatWater:bool, EggLimit:int, PowerType:str,
                 worm_cost: int, berry_cost:int, wheat_cost:int, 
                 mouse_cost:int, fish_cost, FoodWild:int, WingspanCM: int, 
                 either_or: bool) -> None:
        self.name = EnglishName
        self.points = VictoryPoints
        self.nest = NestType
        self.forrest_habitat = HabitatForest
        self.grass_habitat = HabitatGrass
        self.water_habitat = HabitatWater
        self.max_eggs = EggLimit
        self.function_type = PowerType
        self.function = None
        self.eggs = 0
        self.is_played = False
        self.worm_cost = worm_cost
        self.berry_cost = berry_cost
        self.wheat_cost = wheat_cost
        self.mouse_cost = mouse_cost
        self.fish_cost = fish_cost
        self.any_cost = FoodWild
        self.tucked_stashed = 0
        self.either_or = either_or
        
    
    def activate_function(self):
        self.function()
    
    def lay_eggs(self, amount: int):
        assert self.eggs + amount <= self.max_eggs
        
        self.eggs += amount
    
    
    