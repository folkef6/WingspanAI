import pandas as pd
from random import shuffle
from bird import Bird

def get_bird_deck():
    deck = []
    df = pd.read_excel(r"birds_excel.xlsx")
    df = df.drop(columns=['ID', 'ScientificName', 'PowerDetails', 'FoodNone'], axis= 1)

    for _, row in df.iterrows():
        # Check if row is a bird row:
        if row['EnglishName'] == "EnglishName":
            continue

        row = row.where(pd.notnull(row), None)
        # D
        if row['HabitatForest'] == 'y':
            row['HabitatForest'] = True
        else:
            row['HabitatForestl'] = False

        if row['HabitatGrasslands'] == 'y':
            row['HabitatGrasslands'] = True
        else:
            row['HabitatGrasslands'] = False

        if row['HabitatWetlands'] == 'y':
            row['HabitatWetlands'] = True
        else:
            row['HabitatWetlands'] = False

        # Handling the case with either or food
        either_or = False
        if row['FoodInvertebrate'] is not None:
            if float(row['FoodInvertebrate']) < 1 and float(row['FoodInvertebrate']) > 0:
                row['FoodInvertebrate'] = 1
                either_or = True

        if row['FoodSeed'] is not None:
            if float(row['FoodSeed']) < 1 and float(row['FoodSeed']) > 0:
                row['FoodSeed'] = 1
                either_or = True

        if row['FoodFruit'] is not None:
            if float(row['FoodFruit']) < 1 and float(row['FoodFruit']) > 0:
                row['FoodFruit'] = 1
                either_or = True

        if row['FoodFish'] is not None:
            if float(row['FoodFish']) < 1 and float(row['FoodFish']) > 0:
                row['FoodFish'] = 1
                either_or = True

        if row['FoodRodent'] is not None:
            if float(row['FoodRodent']) < 1 and float(row['FoodRodent']) > 0:
                row['FoodRodent'] = 1
                either_or = True

        deck.append(Bird(owner=None, EnglishName=row['EnglishName'], VictoryPoints=row['VictoryPoints'],
                    NestType=row['NestType'], HabitatForest=row['HabitatForest'], HabitatWater=row['HabitatWetlands'], 
                    HabitatGrass=row['HabitatGrasslands'], EggLimit = row['EggLimit'], PowerType= row['PowerType'],
                    worm_cost= row['FoodInvertebrate'], berry_cost=row['FoodFruit'], wheat_cost=row['FoodSeed'],
                    mouse_cost=row['FoodRodent'], fish_cost=row['FoodFish'], FoodWild = row['FoodWild'],
                    WingspanCM = row['WingspanCM'], either_or= either_or))
        
    shuffle(deck)
        
    return deck
    
