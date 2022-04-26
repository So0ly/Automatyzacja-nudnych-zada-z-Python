try:#program ma wywołać kod który może potencjalnie wywołać błąd
except:#jeśli wywołanie try da błąd
raise Exception('')#Wypisuje komunikat błędu
---------------------------------------
import traceback
errorFile.write(traceback.format_exc())#wpisanie do wcześniej otworzonego pliku logów z błędami
assert zmienna==prawda#program się wywali jeśli zmienna nie ma wartości prawda
----------------------------------------
import logging
