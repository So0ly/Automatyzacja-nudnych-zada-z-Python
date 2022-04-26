import random,sys,os,math
for i in range(5):
    print(random.randint(1,10))
while True:
    print('Wpisz exit')
    zm=input()
    if zm=='exit':
        sys.exit()
    print(zm+' to nie polecenie wyjścia')
