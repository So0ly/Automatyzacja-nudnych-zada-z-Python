msg='Lew nie sprzymierza się z kojotem'
count={} #tworzy słownik
for char in msg:
    count.setdefault(char,0)
    count[char]+=1
print(count)
