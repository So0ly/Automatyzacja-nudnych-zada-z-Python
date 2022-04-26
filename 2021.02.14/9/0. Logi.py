>>>import shutil
>>> os.listdir()
['nowy', 'nowy.txt']#plik i katalog stworzone wcześniej
>>> shutil.copy('nowy.txt','nowy')#tworzy kopię w katalogu
'nowy\\nowy.txt'
>>> shutil.copy('nowy.txt','nowszy.txt')#tworzy kopię pliku
'nowszy.txt'
>>> shutil.copytree('nowy','.\\nowiutki')#kopiuje katalog z zawartością
'.\\nowiutki'
>>> shutil.move('nowy.txt','.\\nowiutki\\jeszcze_nowszy.txt')#przenosi i zmienia nazwę
'.\\nowiutki\\jeszcze_nowszy.txt'#katalog musi istnieć przy kopii/przeniesieniu
------------------------------------------
>>> os.unlink('nowszy.txt')#usuwanie pliku
>>> os.rmdir('pusty')#usuwa pusty katalog
>>> shutil.rmtree('nowiutki')#usuwa drzewo katalogu
-------------------------------------------
#############1. Zawartość katalogu###########
os.walk() - przechodzi przez wszystko co znajduje się w katalogu
-------------------------------------------
>>>import zipfile
>>> przyk=zipfile.ZipFile('Barański Mikołaj .zip')#zip z zaliczeniem u Chorasia D:
>>> przyk.namelist()#wypisuje nazwy plików i folderów w archiwum
['IMG_20210201_112133.jpg']
>>> info=przyk.getinfo('IMG_20210201_112133.jpg')#informacje o danym pliku z archiwum
>>> info.file_size#wielkość przed kompresją
5383358
>>> info.compress_size#wielkość po kompresji
5384202#coś się fest zjebało xD
>>>przyk.extractall()#rozpakowuje całego zipa
>>> przyk.extract('IMG_20210201_112133.jpg')#wypakowuje dany plik
'C:\\Users\\Soldi\\Documents\\Python - skrypty\\2021.02.14\\9\\IMG_20210201_112133.jpg'
>>> przyk.extract('IMG_20210201_112133.jpg','.\\zipowy')#wypakowuje plik do podanego miejsca, tworzy je jeśli nie istnieje
'zipowy\\IMG_20210201_112133.jpg'
>>> nowy=zipfile.ZipFile('nowy.zip','w')#utworzenie nowego zipa
>>> nowy.write('0. Logi.py',compress_type=zipfile.ZIP_DEFLATED)#zapis pliku w archiwum z jakąś metodą
>>> nowy.close()
>>> nowy=zipfile.ZipFile('nowy.zip','a')#otworzenie tego samego zipa w trybie append/dołączania
>>> nowy.write('.\\nowy')#dopisanie folderu, nie przeniosło jego zawartości
