def isPhoneNumber(text):
    if len(text)!=12:
        return False
    for i in range(0,3):
        if not text[i].isdecimal():
            return False
    if text[3]!="-":
        return False
    for i in range (4,7):
        if not text[i].isdecimal():
            return False
    if text[7]!="-":
        return False
    for i in range(8,12):
        if not text[i].isdecimal():
            return False
    return True
print("315-555-4242 to numer telefonu:")
print(isPhoneNumber('315-555-4242'))
print("text to nr tel:")
print(isPhoneNumber('text'))
#2
msg="W tym tekscie są dwa numery telefonu, 415-555-1011 oraz 415-555-9999. Program ma je odnaleźć"
for i in range(len(msg)):
    wycinek=msg[i:i+12]
    if isPhoneNumber(wycinek):
        print('Znaleziono numer telefonu: '+wycinek)
print('Gotowe')
