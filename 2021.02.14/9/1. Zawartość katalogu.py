import os
for folderName, subfolders, filenames in os.walk('C:\\Users\\Soldi\\Documents\\Python - skrypty'):
	print('Katalog bieżący to '+folderName)
	for subfolder in subfolders:
		print('Podkatalog katalogu '+folderName+': '+subfolder)
	for filename in filenames:
		print ('Plik katalogu '+folderName+': '+filename)
	print('')
