from asyncio.windows_events import NULL
import pyreadstat
import pandas as pd
import numpy as np

def name_to_id(x):
    return {
        'ALCOHOL': 0,
        'BAKERY': 1,
        'FROZEN' : 2,
        'MEAT' : 3,
        'MILK' : 4,
        'READMADE' : 5,
        'SNACKS' : 6,
        'TINNED' : 7,
        'TOILETRY' : 8,
        'VEG' : 9,
    }[x]
def id_to_name(x):
    return {
        0 : 'ALCOHOL',
        1 : 'BAKERY',
        2 : 'FROZEN',
        3 : 'MEAT',
        4 : 'MILK',
        5 : 'READMADE',
        6 : 'SNACKS',
        7 : 'TINNED',
        8 : 'TOILETRY',
        9 : 'VEG',
    }[x]
def inspect(output):
    lhs         = [tuple(result[2][0][0])[0] for result in output]
    rhs         = [tuple(result[2][0][1])[0] for result in output]
    support    = [result[1] for result in output]
    confidence = [result[2][0][2] for result in output]
    lift       = [result[2][0][3] for result in output]
    return list(zip(lhs, rhs, support, confidence, lift))
df, meta = pyreadstat.read_sav('Shopping_items.sav')  #Načte .sav file
kosikID = 1
kosiky = []
kosik = []
for row in df.values:
    if kosikID != row[0]:
        kosikID = row[0]
        kosiky.append(kosik)
        kosik = []
    kosik.append(row[1])

results = list(apriori(kosiky, min_support = 0.01, min_confidence = 0.7, min_length = 2,min_lift = 3,max_length = 5))
print(results[40])


