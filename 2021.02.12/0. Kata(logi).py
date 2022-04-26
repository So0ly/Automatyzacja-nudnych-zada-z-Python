>>> import os
>>> os.path.join('usr','bin','spam')
'usr\\bin\\spam'
>>> os.getcwd()
'C:\\Program Files\\Python36'
>>> os.chdir('C:\\Users\\Soldi\\Documents\\Python - skrypty\\2021.02.12')
>>> os.getcwd()#Linuxowe pwd
'C:\\Users\\Soldi\\Documents\\Python - skrypty\\2021.02.12'
--------------------------------
>>> os.makedirs('jeden\dwa')#Tworzy katalogi 
>>> os.path.abspath('jeden')#Pokazuje ścieżkę bezwzględną
'C:\\Users\\Soldi\\Documents\\Python - skrypty\\2021.02.12\\jeden'
>>> os.path.abspath('.')#Kropka oznacza bieżący katalog
'C:\\Users\\Soldi\\Documents\\Python - skrypty\\2021.02.12'
>>> os.path.isabs('jeden')#Sprawdza czy ścieżka jest bezwzględna
False
>>> os.path.isabs('C:\\Users\\Soldi\\Documents\\Python - skrypty\\2021.02.12\\jeden')
True
----------------------------------
>>> os.path.relpath('C:\\','jeden')#Sprawdza względną ścieżkę
'..\\..\\..\\..\\..\\..'
>>> os.path.relpath('jeden','C:\\')#(cel,początek)
'Users\\Soldi\\Documents\\Python - skrypty\\2021.02.12\\jeden'
>>> os.path.abspath(os.path.dirname('jeden'))#Ścieżka do katalogu z elementem
'C:\\Users\\Soldi\\Documents\\Python - skrypty\\2021.02.12'
>>> os.path.abspath(os.path.basename('jeden'))#Ścieżka wraz z elementem
'C:\\Users\\Soldi\\Documents\\Python - skrypty\\2021.02.12\\jeden'
-----------------------------------
>>> ścieżka='C:\\Windows\\System32\\calc.exe'
>>> os.path.basename(ścieżka)
'calc.exe'
>>> os.path.dirname(ścieżka)
'C:\\Windows\\System32'
>>> os.path.split(ścieżka)#tworzy krotkę - dirname,basename
('C:\\Windows\\System32', 'calc.exe')
----------------------------------
>>> os.path.sep#Sprawdza jak rozdzielane są katalogi na ścieżce
'\\'
>>> os.path.altsep#alternatywny separator systemowy
'/'
>>> ścieżka.split(os.path.sep)#rozdziela tekst przy użyciu separatora^ 
['C:', 'Windows', 'System32', 'calc.exe']
>>> os.listdir('C:\\')#Wyświetla elementy w danym katalogu (pusty nawias dla aktualnego)
['$Recycle.Bin', '$SysReset', '$Windows.~WS', '$WinREAgent', 'Boot', 'bootmgr', 'BOOTNXT', 'CodeBlocks', 'Documents and Settings', 'DumpStack.log.tmp', 'eSupport', 'GOG Games', 'hiberfil.sys', 'Intel', 'Logs', 'MSOCache', 'pagefile.sys', 'PerfLogs', 'Program Files', 'Program Files (x86)', 'ProgramData', 'Recovery', 'swapfile.sys', 'System Volume Information', 'Udostępniony', 'Users', 'VTRoot', 'Windows', 'xampp']
>>> os.path.getsize('0. Kata(logi).py')#sprawdza wielkość pliku
2421
-------------------------------------
>>> os.path.exists('C:\\Windows')#sprawdza czy katalog/plik istnieje
True
>>> os.path.isfile('C:\\Windows')#sprawdza czy plik istnieje
False
>>> os.path.isdir('C:\\Windows')#sprawdza czy katalog istnieje
True
###################OFFTOPIC####################
os.environ - lista zmiennych środowiskowych
os.environ['USERNAME'] - nazwa użytkownika
os.environ['USERPROFILE'] - ścieżka do katalogu użytkownika
###############################################
>>> przyk=open('C:\\Users\\Soldi\\Documents\\Python - skrypty\\2021.02.12\\przykład.txt')#otwiera plik tekstowy - domyślnie tylko do odczytu
>>> przyktekst=przyk.read()#zczytuje zawartość pliku
>>> przyktekst
'Helou'
>>> przyk=open('przykład.txt')
>>> przyk.readlines()#zczytuje zawartość po liniach
['Helou\n', 'druga linia\n', 'trzecia linia']
#readlines i read nie cofają się na początek pliku, jeśli plik ma dopisane nowe linie - będą one zczytane oprócz tych starych
>>> przyk=open('przykład.txt','w')#otworzenie pliku do zapisu
>>> przyk.write('Zmieniony plik\n')#nadpisanie treści
15#ilość znaków (14 + \n)
>>> przyk.close()#zamknięcie pliku
>>> przyk=open('przykład.txt','a')#otworzenie pliku do append'owania
>>> przyk.write('Dodany tekst\n')#dopisanie treści
13
>>> przyk.close()
>>> przyk=open('przykład.txt','r')#otworzenie pliku tylko do odczytu
>>> przyk.readlines()
['Zmieniony plik\n', 'Dodany tekst\n']
#######open() może utworzyć dany plik ale musi posiadać parametr otworzenia pliku#####
>>> przyk=open('nowy.txt','w')
>>> przyk=open('nowszy.txt')
Traceback (most recent call last):
  File "<pyshell#96>", line 1, in <module>
    przyk=open('nowszy.txt')
FileNotFoundError: [Errno 2] No such file or directory: 'nowszy.txt'
########################################################################################
##tutaj kod z 2. Shelve.py##
>>> import pprint
>>> cats = [{'name':'Jeden','desc':'Drugi'},{'name':'Cztery','desc':'Trzeci'}]
>>> fileObj=open('Pprint.py','w')
>>> fileObj.write('cats = '+pprint.pformat(cats)+'\n')#zapis wyniku do pliku "3. Pprint.py
82
>>> fileObj.close()
>>> import Pprint#plik Pprint.py utworzony wyżej
>>> Pprint.cats
[{'desc': 'Drugi', 'name': 'Jeden'}, {'desc': 'Trzeci', 'name': 'Cztery'}]
>>> Pprint.cats[0]['desc']
'Drugi'



