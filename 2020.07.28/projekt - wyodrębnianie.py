#! python3
import pyperclip,re
#regex telefonu
phoneRegex=re.compile(r"""(
    (\d{3]|\(\d{3}\))?              #kierunkowy
    (\s|-|\.)?                      #separator
    (\d{3})                         #pierwsze cyfry
    (\s|-|\.)                       #separator
    (\d{4})                         #ostatnie cyfry
    (\s*(ext|x|ext.)\s*(\d{2,5}))?  #nr wewnętrzny
)""",re.VERBOSE)
#regex email'a
emailRegex=re.compile(r"""(
    [a-zA-Z0-9._%+-]+ #nazwa użytkownika, conajmniej jeden znak
    @
    [a-zA-Z0-9.-]+    #nazwa domeny
    (\.[a-zA-Z]{2,4}) #kropka i końcówka linku
)""",re.VERBOSE)
#wyszukanie dopasowań w schowku
text=str(pyperclip.paste())
matches=[]
for groups in phoneRegex.findall(text):
    phoneNum = '-'.join([groups[1],groups[3],groups[5]])
    if groups[8]!='':
        phoneNum+=' x'+groups[8]
    matches.append(phoneNum)
for groups in emailRegex.findall(text):
    matches.append(groups[0])
#skopiowanie
if len(matches)>0:
    pyperclip.copy('\n'.join(matches))
    print("Skopiowano:")
    print("\n".join(matches))
else:
    print("Nie znaleziono żadnego nr telefonu lub adresu email")

