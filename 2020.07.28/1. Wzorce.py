import re
\d - liczba całkowita
\d{3} - wzorzec liczby całkowitej powtórzony 3 razy
\d[0-5] - wybiera tylko liczby od 0 do 5
\d[^0-5] - wybiera wszystkie cyfry oprócz od 0 do 5
\D - dowolny znak oprócz liczby całkowitej
\w - dowolna litera, cyfra, lub znak podkreślenia, może też oznaczać całe słowo
\W - dowolny znak który nie jest literą, cyfrą, lub znakiem podkreślenia
\s - dowolna spacja, tabulator lub \n
\S - dowolny znak który nie jest spacją, tabem lub \n
-------------
>>> phoneNumRegex=re.compile(r'\d\d\d-\d\d\d-\d\d\d\d') #tworzy obiekt typu Regex; wzorzec
>>> mo=phoneNumRegex.search("Numer telefonu: 415-555-4242.")#Przeszukuje text i porównuje z wzorcem
>>> print("Znaleziono numer: "+mo.group())#jeśli dopasowanie istnieje, będzie zapisane w metodzie group, jeśli nie - group będzie NULL'em
Znaleziono numer: 415-555-4242

>>> phoneNumRegex=re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)') #nawias tworzy niewidzialne grupy
>>> mo=phoneNumRegex.search("Numer telefonu: 415-555-4242.")
>>> print("Znaleziono numer: "+mo.group())
Znaleziono numer: 415-555-4242
>>> mo.group(1)
'415'
>>> mo.group()
'415-555-4242'
>>> mo.group(0)
'415-555-4242'
>>> mo.groups()
('415', '555-4242')
>>> kierunkowy, nrWłaściwy=mo.groups()
>>> print(kierunkowy)
415
>>> print(nrWłaściwy)
555-4242
-------------
>>> phoneNumRegex=re.compile(r'(\(\d\d\d\)) (\d\d\d-\d\d\d\d)')#ukośnik przed nawiasem umożliwia użycie go w numerze
>>> mo=phoneNumRegex.search("Numer telefonu: (415) 555-4242.")
>>> mo.group(1)
'(415)'
>>> heroRegex=re.compile(r"Arrow|Flash") #znak potoku/pipe'a (|) daje możliwość użycia różnych wzorców
>>> mo1=heroRegex.search("Arrow i Flash.")
>>> mo1.group()
'Arrow'
>>> mo2=heroRegex.search("Flash i Arrow.") #Wybiera pierwszy napotkany pasujący ciąg
>>> mo2.group()
'Flash'
--------------
>>> batRegex=re.compile(r'Bat(man|mobile|copter)') #Prefiks ten sam, różne dokończenia
>>> mo=batRegex.search("Batmobile stracił koło")
>>> mo.group()
'Batmobile'
>>> mo.group(1)
'mobile'
>>> batRegex=re.compile(r'Bat(wo)?man') #znak zapytania oznacza jedno lub zero wystąpień wycinka w nawiasie
>>> mo1=batRegex.search("The Adventures of Batman")
>>> mo1.group()
'Batman'
>>> mo2=batRegex.search("The Adventures of Batwoman")
>>> mo2.group()
'Batwoman'
----------------
>>> batRegex=re.compile(r'Bat(wo)*man') #gwiazdka oznacza zero lub ileś wystąpień wycinka w nawiasie
>>> mo2=batRegex.search("The Adventures of Batwoman")
>>> mo2.group()
'Batwoman'
>>> mo2=batRegex.search("The Adventures of Batman")
>>> mo2.group()
'Batman'
>>> mo2=batRegex.search("The Adventures of Batwowowowoman")
>>> mo2.group()
'Batwowowowoman'
----------------
>>> batRegex=re.compile(r'Bat(wo)+man') #plus oznacza że wycinek w nawiasie ma wystąpić conajmniej raz
>>> mo2=batRegex.search("The Adventures of Batwowowowoman")
>>> mo2.group()
'Batwowowowoman'
>>> mo2=batRegex.search("The Adventures of Batwoman")
>>> mo2.group()
'Batwoman'
>>> mo2=batRegex.search("The Adventures of Batman")
>>> mo2== None #wo nie wystąpiło ani razu więc wyszukiwanie jest puste
True
---------------
>>> śmiechReg=re.compile(r'(ha){3}')#ma powtórzyć dokładnie 3 razy
>>> wy=śmiechReg.search("hahaha")
>>> wy.group()
'hahaha'
>>> śmiechReg=re.compile(r'(ha){3,5}')#ma powtórzyć od 3 do 5 razy
>>> wy=śmiechReg.search("hahahaha")
>>> wy.group()
'hahahaha'
>>> wy=śmiechReg.search("hahahahaha")
>>> wy.group()
'hahahahaha'
---------------
>>> greedyHaRegex=re.compile(r"(Ha){3,5}")
>>> mo1=greedyHaRegex.search("HaHaHaHaHa") #bez żadnego znaku będzie wybierało najdłuższy pasujący wycinek
>>> mo1.group()
'HaHaHaHaHa'
>>> nongreedyHaRegex=re.compile(r"(Ha){3,5}?")#ze znakiem zapytania, będzie wybierało najkrótszy pasujący wycinek
>>> mo2=nongreedyHaRegex.search("HaHaHaHaHa")
>>> mo2.group()
'HaHaHa'
-------------
>>> phoneNumRegex=re.compile(r"\d{3}-\d{3}-\d{4}")
>>> phoneNumRegex.findall("tel. kom: 415-555-9999, praca: 212-555-0000") #findall wyszukuje wszystkie pasujące wycinki
['415-555-9999', '212-555-0000']
>>> phoneNumRegex=re.compile(r"(\d{3})-(\d{3})-(\d{4})") #z podziałem na grupy
>>> phoneNumRegex.findall("tel. kom: 415-555-9999, praca: 212-555-0000")
[('415', '555', '9999'), ('212', '555', '0000')]
------------------------
>>> beginsWithHello=re.compile(r"^Witaj")# ^na początku tekstu oznacza że ma rozpoczynać przeszukiwane miejsce
>>> beginsWithHello.search("Witaj, świecie")
<_sre.SRE_Match object; span=(0, 5), match='Witaj'>
>>> beginsWithHello.search("Powiedział Witaj")==None
True
----------------------
>>> endsWithNumber=re.compile(r"\d$")#$ wskazuje że podany znak ma kończyć przeszukiwane miejsce
>>> endsWithNumber.search("liczba 22")
<_sre.SRE_Match object; span=(8, 9), match='2'>
----------------------
>>> wholeStrin=re.compile(r"^[awdsawd]+$")#cały ciąg musi spełniać podane kryteria
>>> wholeStrin.search("aawdsadwasdwad")
<_sre.SRE_Match object; span=(0, 14), match='aawdsadwasdwad'>
-----------------------
>>> atRegex=re.compile(r'.ba') #znak kropki dopasowuje jeden dowolny znak przed wyrażeniem, nie uwzględnia \n
>>> atRegex.findall('Baba bada baobaby. Baba dba o oba baobaby')
['aba', ' ba', ' ba', 'oba', 'aba', 'dba', 'oba', ' ba', 'oba']
----------------------
>>> nameRegex=re.compile(r"Imię: (.*) Nazwisko: (.*)")
>>> mo=nameRegex.search("Imię: Suli Nazwisko: Barański")
>>> mo.group(1)
'Suli'
>>> mo.group(2)
'Barański'
----------------------
>>> nongreedyRegex=re.compile(r"<.*?>")# będzie szukać najkrótszego dopasowania
>>> mo=nongreedyRegex.search("<To jest obsługa> w restauracji.>")
>>> mo.group()
'<To jest obsługa>'
>>> greedyRegex=re.compile(r"<.*>")# będzie szukać najdłuższego dopasowania
>>> mo2=greedyRegex.search("<To jest obsługa> w restauracji.>")
>>> mo2.group()
'<To jest obsługa> w restauracji.>'
---------------------
>>> noNewlineRegex=re.compile(".*")
>>> noNewlineRegex.search("Służyć.\nChronić.\nPomagać.")
<_sre.SRE_Match object; span=(0, 7), match='Służyć.'>
>>> newlineRegex=re.compile(".*",re.DOTALL)#kropka ma obsługiwać też \n
>>> newlineRegex.search("Służyć.\nChronić.\nPomagać.")
<_sre.SRE_Match object; span=(0, 25), match='Służyć.\nChronić.\nPomagać.'>
----------------------
(?) - jedno wystąpienie
(*) - wiele wystąpień
(+) - jedno lub więcej wystąpień
{n} - dokładnie n razy
{n,} - n lub więcej razy
{,n} - od 0 do n razy
{n,m} - od n do m razy
-------------------------
re.IGNORECASE / re.I #ignoruje wielkość liter
>>> robocop=re.compile(r"robocop",re.I)
>>> robocop.search("RoboCop")
<_sre.SRE_Match object; span=(0, 7), match='RoboCop'>
>>> robocop.search("robocop")
<_sre.SRE_Match object; span=(0, 7), match='robocop'>
>>> robocop.search("ROBOCOP")
<_sre.SRE_Match object; span=(0, 7), match='ROBOCOP'>
------------------------
>>> namesRegex=re.compile(r"Agent \w+")
>>> namesRegex.sub("OCENZUROWANE","Agent Alicja przekazała dokumenty dla Agent Beaty") #sub zamienia tekst pasujący do wzorca 
'OCENZUROWANE przekazała dokumenty dla OCENZUROWANE'
>>> agentNamesRegex=re.compile(r"Agent (\w)\w*")#jest to podział na dwie grupy, nawias jest drugą grupą a cyfra 1 oznacza którą grupę ma zmienić, sub działa na słowo agent i następne bez pierwszej litery
>>> agentNamesRegex.sub(r"\1****", "Agent Alicja powiedziała Agent Karolinie, że Agent Ewa wiedziała o podwójnej roli Agent Beaty.")
'A**** powiedziała K****, że E**** wiedziała o podwójnej roli B****.'
-----------------------
phoneRegex=re.compile(r"""
(
	(\d{3}|\(\d{3}\))? #numer kierunkowy
	(\s|-|\.)?	   #separator
	\d{3}		   #pierwsze trzy cyfry
	(\s|-|\.)	   #separator
	\d{4}		   #4 cyfry
	(\s*(ext|x|ext.)\s*\d{2,5})? #numer wewnętrzny
)""",re.VERBOSE) #VERBOSE pozwala na umieszczenie komentarzy co powoduje czytelniejszy kod
someRegex=re.compile("foo",re.I|re.DOTALL|re.VERBOSE) #połączenie argumentów































