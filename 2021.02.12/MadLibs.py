#! python3
print('Podaj przymiotnik')
przym=input()
print('Podaj rzeczownik')
rzecz=input()
print('Podaj czasownik')
czas=input()
print('Podaj przymiotnik')
rzecz1=input()
plik=open('nowy.txt','w')
tekst=str('Wczoraj %s panda weszla na %s i zaczela %s. Pobliska %s nie ucierpiala na skutek tych wydarzen.'%(przym,rzecz,czas,rzecz1))
print(tekst)
plik.write('%s'%(tekst))
plik.close()
