#! python3
#Menedżer haseł ale po rozdziale 8
import sys,pyperclip,shelve 
pwShelf=shelve.open('pw')
####zapis####
if len(sys.argv)==3 and sys.argv[1].lower()=='save':
    pwShelf[sys.argv[2]]=pyperclip.paste()#zapis ze schowka pod podany klucz
elif len(sys.argv)==3 and sys.argv[1].lower()=='delete':
    del pwShelf[sys.argv[2]]#usunięcie wpisu o podanym kluczu
###lista lub słowo kluczowe####
elif len(sys.argv)==2:
	if sys.argv[1].lower()=='list':
		pyperclip.copy(str(list(pwShelf.keys())))#wypisuje całą listę kluczy
	elif sys.argv[1] in pwShelf:
		pyperclip.copy(pwShelf[sys.argv[1]])#skopiowanie wartości dla danego klucza
		print('Skopiowano hasło dla konta %s'%(sys.argv[1]))
pwShelf.close()
