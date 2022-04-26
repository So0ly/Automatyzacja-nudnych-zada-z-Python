import random
licz=random.randint(1,20)
print ('Pewna liczba od 1 do 20')
for liczWybór in range(1,7):
    print('Spróbuj odgadnąć liczbę')
    a=int(input())
    if a<licz:
        print('Za mała')
    elif a>licz:
        print('Za duża')
    else:
        break;
if a==licz:
    print('Odgadłeś po '+str(liczWybór)+' próbach')
else:
    print('Nie udało się, liczba to: '+str(licz))
