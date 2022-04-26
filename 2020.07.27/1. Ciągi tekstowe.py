>>>print("Witajcie!\nJak się pan czuje, panie O\'Hara?\nDziękuję, w porządku.")
Witajcie!
Jak się pan czuje, panie O'Hara?
Dziękuję, w porządku.
\n - nowa linia
\\ - ukośnik
\t - tab
\"
\'
-------
>>> print(r"To jest kot pana O\'Hary.") #litera r przed tekstem spowoduje że nie będzie on zmodyfikowany
To jest kot pana O\'Hary.
-------
>>>print("""Ten tekst jest wypisywany tak jak jest pisany;

Tu jest drugi wiersz

a tu trzeci
""")
Ten tekst jest wypisywany tak jak jest pisany;

Tu jest drugi wiersz

a tu trzeci
-------
"""Komentarz wielowierszowy"""
-------
>>> spam="Helou"
>>> spam.upper()
'HELOU'
>>> spam.lower()
'helou'
>>> spam.islower() #sprawdza czy wszystkie litery są małe
False
>>> spam.isupper() #sprawdza czy wszystkie litery są duże
False
>>> spam="HELOU!"
>>> spam.isupper()
True

spam.isalpha() - sprawdza czy jest zbudowany tylko z liter i nie jest pusty
spam.isalnum() - sprawdza czy jest zbudowany tylko z liter i cyfr i czy nie jest pusty
spam.isdecimal() - sprawdza czy jest zbudowany tylko z cyfr i nie jest pusty
spam.istitle() - sprawdza czy tylko na początku ma wielką literę i nie jest pusty
spam.isspace() - sprawdza czy jest zbudowany tylko ze spacji, tabów oraz znaków nowego wiersza i nie jest pusty
---------
>>> spam.startswith("H")
True
>>> spam.startswith("HELOU")
True
>>> spam.endswith("HELOU!")
True
--------
>>> ' i '.join(['jeden','dwa','trzy']) #ciąg poprzedzający funkcję jest łącznikiem
'jeden i dwa i trzy'
>>> "Jeden dwa trzy".split() #domyślnie rozdziela na spacjach, tabach i \n
['Jeden', 'dwa', 'trzy']
>>> "Jeden dwa trzy".split('d') #rozdziela w każdym miejscu występowania 'd'
['Je', 'en ', 'wa trzy']
>>> "witaj".rjust(10) #wyrównanie do prawej; domyślnie spacją
'     witaj'
>>> "witaj".ljust(10) #wyrównanie do lewej
'witaj     '
>>> "witaj".ljust(10,'*')
'witaj*****'
>>> "witaj".rjust(10,'*')
'*****witaj'
>>> "witaj".center(10) #wycentrowanie
'  witaj   '
>>> "witaj".center(10,'=')
'==witaj==='
----------
>>> spam='            Witaj         '
>>> spam
'            Witaj         '
>>> spam.strip()
'Witaj'
>>> spam.lstrip()
'Witaj         '
>>> spam.rstrip()
'            Witaj'
>>> spam="SpamSpamBaconSpamEggsSpamSpam"
>>> spam.strip("ampS")
'BaconSpamEggs'
>>> spam.strip("Sm")
'pamSpamBaconSpamEggsSpamSpa'
-----------
>>> import pyperclip
>>> pyperclip.copy("Witaj")
>>> pyperclip.paste()
'Witaj'










