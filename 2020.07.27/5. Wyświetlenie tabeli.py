tableData=[['jabłka','pomarańcze','wiśnie','banany'],
           ['Alicja','Bob','Karol','Dawid'],
           ['psy','koty','łosie','gęsi']]

def printTable(lista):
    naj=[lista[0][0],lista[1][0],lista[2][0]]
    for i in range (0,len(lista)):
        for b in range(0,len(lista[i])):
            if len(lista[i][b])>len(naj[i]):
                naj[i]=lista[i][b]
    for i in range(0,len(lista[0])):
       print(lista[0][i].rjust(len(naj[0]))+" "+lista[1][i].rjust(len(naj[1]))+" "+lista[2][i].rjust(len(naj[2])))         
printTable(tableData)
