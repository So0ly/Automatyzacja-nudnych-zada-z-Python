def collatz(number):
    while number!=1:
        if number%2==0:
           number//=2
           print(number)
           collatz(number)
        elif number%2==1:
            number=3*number+1
            print(number)
            collatz(number)
print('Podaj liczbę:')
try:
    collatz(int(input()))
except ValueError: print('Podaj liczbę całkowitą')

