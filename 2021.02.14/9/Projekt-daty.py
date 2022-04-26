#! python3
#zamiana dat z systemu amerykańskiego na europejski
import re,os,shutil
pattern=re.compile(r"""^(.*?)
    ((0|1)?\d)-
    ((0|1|2|3)?\d)-
    ((19|20)\d\d)
    (.*?)$
    """,re.VERBOSE)
for amerFilename in os.listdir('.'):#sprawdź wszystkie pliki w aktualnym katalogu
    mo=pattern.search(amerFilename)#szukaj plików według regexu

    if mo==None:#jeśli nie pasuje do regexu
        continue

    beforePart=mo.group(1) #grupy z regexu
    monthPart=mo.group(2)
    dayPart=mo.group(4)
    yearPart=mo.group(6)
    afterPart=mo.group(8)
    #zamiana na europejski styl
    euroFilename=beforePart+dayPart+'-'+monthPart+'-'+yearPart+afterPart
    absWorkingDir=os.path.abspath('.')#ścieżka do folderu
    amerFilename=os.path.join(absWorkingDir,amerFilename)#ścieżka do pliku w stylu amerykańskim
    euroFilename=os.path.join(absWorkingDir,euroFilename)
    print('Renaming "%s" to "%s"...'%(amerFilename,euroFilename))#wypisanie co się zmieni
    shutil.move(amerFilename,euroFilename)#zamiana nazwy
