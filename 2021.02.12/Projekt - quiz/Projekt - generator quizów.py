#! python3
#generator losowych plików quizu
import random

capitals={'Alabama':'Montgomery','Alaska':'Juneau','Arizona':'Phoenix','Arkansas':'Little Rock','Kalifornia':'Sacramento','Kolorado':'Denver',
          'Connecticut':'Hartford','Delaware':'Dover','Floryda':'Tallahassee','Georgia':'Atlanta','Hawaje':'Honolulu','Idaho':'Boise','Illinois':'Springfield',
          'Indiana':'Indianapolis','Iowa':'Des Moines','Kansas':'Topeka','Kentucky':'Frankfort','Luizjana':'Baton Rouge','Maine':'Augusta','Maryland':'Annapolis','Massachusetts':'Boston',
          'Michigan':'Lansing','Minnesota':'Saint Paul','Mississippi':'Jackson','Missouri':'Jefferson City','Montana':'Helena','Nebraska':'Lincoln','Nevada':'Carson City',
          'New Hampshire':'Concord','New Jersey':'Trenton','Nowy Meksyk':'Santa Fe','Nowy Jork':'Albany','Karolina Polnocna':'Raleigh','Dakota Polnocna':'Bismarck','Ohio':'Columbus',
          'Oklahoma':'Oklahoma City','Oregon':'Salem','Pensylwania':'Harrisburg','Rhode Island':'Providence','Karolina Poludniowa':'Columbia','Dakota Poludniowa':'Pierre','Tennessee':'Nashville',
          'Teksas':'Austin','Utah':'Salt Lake City','Vermont':'Montepelier','Wirginia':'Richmond','Waszyngton':'Olympia','Wirginia Zachodnia':'Charleston','Wisconsin':'Madison','Wyoming':'Cheyenne'}
for quizNum in range(35):
    #Utworzenie plików
    quizFile = open('quiz%s.txt' % (quizNum+1),'w')
    answerFile=open('quizanswer%s.txt'%(quizNum+1),'w')
    #nagłówek
    quizFile.write('Imie i nazwisko:\n\nData:\n\nKlasa:\n\n')
    quizFile.write((' '*20)+'Quiz stolic stanow (Quiz %s)'%(quizNum+1))
    quizFile.write('\n\n')
    #losowanie kolejności
    states=list(capitals.keys())
    random.shuffle(states)
    #Utworzenie pytania dla każdego stanu
    for questionNum in range (50):
        correctAnswer=capitals[states[questionNum]]
        wrongAnswers = list(capitals.values())
        del wrongAnswers[wrongAnswers.index(correctAnswer)]
        wrongAnswers=random.sample(wrongAnswers,3)
        answerOptions=wrongAnswers+[correctAnswer]
        random.shuffle(answerOptions)
        #zapis pytania i odpowiedzi
        quizFile.write('%s. Co jest stolica stanu %s\n'%(questionNum+1,states[questionNum]))
        for i in range(4):
            quizFile.write('    %s. %s\n'%('ABCD'[i],answerOptions[i]))
        quizFile.write('\n')
        answerFile.write('%s. %s\n' %(questionNum+1,'ABCD'[answerOptions.index(correctAnswer)]))
quizFile.close()
answerFile.close()
