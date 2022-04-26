#! python3
#backup katalogu
import zipfile,os

def backupToZip(folder):
    folder=os.path.abspath(folder)#pobieramy ścieżkę bezwzględną
    number=1#zmienna dopisywana do backupa
    while True:
        zipFilename=os.path.basename(folder)+'_'+str(number)+'.zip'
        if not os.path.exists(zipFilename):
            break;
        number=number+1
    print('Tworzenie archiwum %s...'%(zipFilename))
    backupZip=zipfile.ZipFile(zipFilename,'w')

    for foldername, sub, file in os.walk(folder):#podobnie do 1.py
        print('Dodawanie plików w %s...'%(foldername))
        backupZip.write(foldername)
        for filename in file:
            newBase=os.path.basename(folder)+'_'
            if filename.startswith(newBase) and filename.endswith('.zip'):
                continue
            backupZip.write(os.path.join(foldername,filename))
    backupZip.close()
    print('Gotowe')
backupToZip('C:\\Users\\Soldi\\Documents\\Python - skrypty\\2021.02.14\\9')
