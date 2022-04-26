import random

def odp(answer):
    if answer in range(1,5):
        return 'odp: '+str(answer)
    elif answer==8:
        return '8'
    else:
        return 'liczba >5 && <10'
r=random.randint(1,9)
los=odp(r)
print(los)
    
