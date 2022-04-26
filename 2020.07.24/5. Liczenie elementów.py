allGuests={'Alicja':{'apples':5,'pretzels':12},
           'Bob':{'ham sandwiches':3,'apples':2},
           'Karol':{'cups':3,'apple pies':1}}
def totalBrought(guests,item):
    numBrought=0
    for k,v in guests.items():
        numBrought+=v.get(item,0)
    return numBrought
print('Liczba przyniesionych produktów:')
print(' -Jabłka           '+str(totalBrought(allGuests,'apples')))
print(' -Kubki            '+str(totalBrought(allGuests,'cups')))     
print(' -Ciastka          '+str(totalBrought(allGuests,'cookies')))
print(' -Kanapki z szynką '+str(totalBrought(allGuests,'ham sandwiches')))
print(' -Jabłeczniki      '+str(totalBrought(allGuests,'apple pies')))


