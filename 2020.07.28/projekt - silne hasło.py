#! python3
import re
print("Wpisz hasło")
passw=input()
if len(passw)>=8 and passw.alnum==True:
    passw1Regex=re.compile(r"""(
        
    )""",re.VERBOSE)
    passwRegex.search(passw)
else:
    print("Słabe hasło - długość")
