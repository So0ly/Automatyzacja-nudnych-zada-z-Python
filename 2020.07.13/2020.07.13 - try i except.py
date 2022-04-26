def spam (divideBy):
    try:
        return 42/divideBy
    except ZeroDivisionError:
        print('Błąd: Dzielenie prze zero')
print (spam(2))
print (spam(12))
print (spam(0))
