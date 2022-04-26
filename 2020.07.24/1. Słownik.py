>>> myDog={'size':'gruby','color':'szare','disposition':'głośny'}
>>> myDog['size']
'gruby'
>>> for v in myDog.values(): #wypisuje wartości
	print(v)
gruby
szare
głośny
-----------
>>>for k in myDog.keys(): #wypisuje klucze
	print(k)
size
color
disposition
>>> for i in myDog.items(): #wypisuje krotki klucz-wartość
	print(i)
('size', 'gruby')
('color', 'szare')
('disposition', 'głośny')
-----------
>>> picnicItems={'apples':5,'cups':2}
>>> 'Przynieść '+str(picnicItems.get('cups',0))+' kubki' #get(co ma pobrać,wartość jeśli nie istnieje pobierany element)
'Przynieść 2 kubki'
>>> 'Przynieść '+str(picnicItems.get('eggs',0))+' jajka'
'Przynieść 0 jajka'
>>> picnicItems.setdefault('bananas','3') #dodaje wartość domyślną jeśli nie istnieje w ogóle
'3'
>>> picnicItems
{'apples': 5, 'cups': 2, 'bananas': '3'}
>>> picnicItems.setdefault('bananas','5')
'3'
>>> picnicItems #potwierdzenie wyższego
{'apples': 5, 'cups': 2, 'bananas': '3'}
-------------
