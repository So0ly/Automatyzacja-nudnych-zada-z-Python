import shelve
shelfFile=shelve.open('mydata')#otwiera plik jako plik binarny
cats=['Jeden','Dwa','Trzy']
shelfFile['cats']=cats#tworzy klucz cats dla wartości wyżej
shelfFile.close()
