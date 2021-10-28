from math import ceil

def getRange(max_range,min):
    x = []
    for i in range(ceil(max_range)*100):
        x.append(round(min + i/100,2))
    return x
