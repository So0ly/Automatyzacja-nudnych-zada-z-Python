#! python3
#wyszukiwanie plików txt
################################DO POPRAWY
import re,os
tekstReg=re.compile(r'Zmi*')
for i in os.listdir():
    if i.endswith('.txt'):
        plik=open(i,'r')
        print('Otworzono %s'%(i))
        d=tekstReg.findall('%s'%(plik.readlines()))
        print(d)
        plik.close()
