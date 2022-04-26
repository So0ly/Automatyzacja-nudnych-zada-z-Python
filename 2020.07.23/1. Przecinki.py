spam=['jabłka','banany','tofu','koty']
def funkcja(parametr):
    for i in range(0,len(parametr)):
        if i==len(parametr)-2:
            print(parametr[i], end=' i ')
        else:
            print(parametr[i],end=', ')
funkcja(spam)
