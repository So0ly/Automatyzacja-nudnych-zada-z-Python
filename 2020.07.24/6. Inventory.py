inv={'strzała':12,'złote monety':42,'lina':1,'pochodnia':6,'sztylet':1}
dragonLoot=['złote monety','sztylet','złote monety','złote monety','rubin']
def addToInventory(invent,addedItems):
   for k,v in invent.items():
      ##########################
       for i in range(0,len(addedItems)-1):
           if addedItems[i]==k:
               print (k)
       ##############        
def displayInventory(inventory):
    print("Inwentarz:")
    item_total=0
    for k,v in inventory.items():
        print(k+': '+str(v))
        item_total+=v
    print("Całkowita liczba przedmiotów: "+str(item_total))
inv=addToInventory(inv,dragonLoot)
displayInventory(inv)
