print ('Witaj, ', end='')
print ('świecie')

print('jeden','dwa','trzy', sep=', ')

def spam():
    global eggs
    eggs = 'spam'

eggs='zmienna globalna'
spam()
print(eggs)
