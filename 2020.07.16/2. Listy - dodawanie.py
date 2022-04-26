lista=[]
while True:
    print("Podaj słowo nr "+str(len(lista)+1))
    lis=input()
    if lis=='':
        break
    lista+=[lis]
print("Lista słów:")
for lis in lista:
    print(' '+lis)
