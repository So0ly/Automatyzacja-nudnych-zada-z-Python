#! python3
#to samo ale działające w pw.py
PASSWORDS={'email':'diahwdhaiud',
           'blog':'dwadwadaww',
           'luggage':'wadadwadwad'}
import sys,pyperclip
if len(sys.argv)<2:
    print('skopiowanie hasła dla wskazanego konta')
    sys.exit()
account=sys.argv[1]

if account in PASSWORDS:
    pyperclip.copy(PASSWORDS[account])
    print('Hasło dla konta '+account+' zostało skopiowane do schowka.')
else:
    print('Nie istnieje konto o nazwie '+account+'.')
