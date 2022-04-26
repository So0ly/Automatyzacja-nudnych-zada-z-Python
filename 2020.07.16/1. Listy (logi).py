spam=["jed","dwa"]
>>> spam
['jed', 'dwa']
>>> spam=['jeden']
>>> spam
['jeden']
>>> spam[0]
'jeden'
>>> spam[0][3]
'e'
>>> spam=[['jeden'],['cztery']]
>>> spam[1][0][2] #wybór listy -> element -> litera
't'
>>> spam[-1][0] #wybór od końca
'cztery'
>>> spam[1][0][0:3] #wycinek
'czt'
>>> len(spam) #liczy elementy
2
>>>spam=[['jeden', 'dwa'], ['trzy', 'cztery']]
>>> del spam[0][0] #usuwa element i redukuje liczbę elementów
>>> spam [0][0]
'dwa'

>>> supplies=['długopisy','zszywacze','segregatory']
>>> for i in range(len(supplies)):
	print ('Indeks '+str(i)+' na liście supplies to: '+supplies[i])
Indeks 0 na liście supplies to: długopisy
Indeks 1 na liście supplies to: zszywacze
Indeks 2 na liście supplies to: segregatory
>>> supplies.index('zszywacze') #miejsce na liście jeśli się tam znajduje
1
>>> supplies.append('ołówki') #dodaje na końcu listy
>>> supplies
['długopisy', 'zszywacze', 'segregatory', 'ołówki']
>>> supplies.insert(1,'zszywki') #dodaje z podanym indexem
>>> supplies
['długopisy', 'zszywki', 'zszywacze', 'segregatory', 'ołówki']
-----------
>>> tab=[1,5,2,7,-2]
>>> tab.sort()
>>> tab
[-2, 1, 2, 5, 7]
>>> tab.sort(reverse=True)
>>> tab
[7, 5, 2, 1, -2]
--------
>>> print('jeden i '\ #znak \ łamie linijkę i kontynuuje ją w następnej
      +'dwa')
jeden i dwa
>>> name='Typuńciu'
>>> for i in name:
	print(i,end='')	
Typuńciu
---------
>>> spam=['a','b','c']
>>> maps=spam
>>> maps[1]='w'
>>> maps
['a', 'w', 'c']
>>> spam        #dane nie zostały skopiowane; jedna lista działa na dwóch przypisaniach
['a', 'w', 'c']
----------
>>> import copy #kopiuje zawartość bez odwołania
>>> spam=['a','b','c']
>>> maps=copy.copy(spam) #operacje na kopii nie wpływają na oryginał; operacje na oryginale wpływają na kopię
>>> maps[1]='w'
>>> spam
['a', 'b', 'c']
>>> maps
['a', 'w', 'c']
>>>maps=copy.deepcopy(spam) #operacje na oryginale nie zmieniają wartości kopii
