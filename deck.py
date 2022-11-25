import pandas as pd

#from bird import Bird

deck = []
df = pd.read_excel(r"birds_excel.xlsx")
df = df.drop(['ID', 'ScientificName', 'PowerDetails', 'FoodNone'], 1)

for _, row in df.iterrows():
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
    print(row)
    #deck.append(Bird(owner=None, EnglishName=row['EnglishName'], VictoryPoints=row['VictoryPoints']),
    #            NestType=row['NestType'], )