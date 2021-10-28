# Jesper Svensson & Erik Smeds 2021-11-02


# Hämtar glosor från en fil, vars filnamn skickas som en parameter,
# sedan returneras glosorna
def getGlosorFromFile(filnamn):
    # Returnerar en dict, med ordparen
    glosor = dict()  # Skapar en dictionary
    with open(filnamn, "r", encoding="utf8") as glosfil:  # Öppnar filen
        # Går igenom alla rader i textfilen
        # På varje rad finns ett ordpar som delas upp i och läggs in i dictionaryn
        # med ena språket som key och andra som value
        for rad in glosfil:
            if rad.find('>') > 0:
                glosor['lang'] = rad.replace('\n', '').split(">")
            else:
                wordpair = rad.replace('\n', '').split(";")
                language1 = wordpair[0]
                language2 = wordpair[1]
                glosor[language1] = language2

        # Om inte språket var angivet i filen
        if 'lang' not in glosor:
            glosor['lang'] = ['Srpåk1', 'Språk2']
    glosfil.close()
    return glosor


# Denna funktionen kör själva quizen
def glosquiz(glosor):
    if len(glosor) < 2:
        print('Inga glosor hittades!')
        return

    # Skriver ut vilket språk de olika kolumnerna är på
    antal_mellanslag = 24 - len(glosor['lang'][0]) - len(glosor['lang'][1])

    print(glosor['lang'][0], antal_mellanslag * ' ', glosor['lang'][1])
    print('==========================')

    # Lista med orden från det första språket/alla keys
    words_lang1 = list(glosor.keys())

    # Skriver ut alla ord så man kan träna på dem
    for i in range(0, len(words_lang1)):
        # Hoppa över om det är vilket språk-namnen
        if words_lang1[i] == 'lang':
            continue

        # Sparar ordet på det andra språket
        word_lang2 = glosor[words_lang1[i]]

        antal_mellanslag = 24 - len(words_lang1[i]) - len(word_lang2)
        print(words_lang1[i], antal_mellanslag * ' ', word_lang2)

    # Quizen
    print('\n'*4)  # Gör lite radbyten
    print(f'Nu ska du översätta ordens som står på', glosor['lang'][0])
    print('='*40)

    correct_answears = 0  # Antalet rätt man fått

    # Loopar igenom allar ord i listan och låter användaren skriva in översättningen
    for i in range(0, len(words_lang1)):
        # Hoppa över om det är vilket språk-namnen
        if words_lang1[i] == 'lang':
            continue

        print(f'Vad betyder {words_lang1[i]}?')

        guess = input('Skriv här: ')

        if guess == glosor[words_lang1[i]]:
            print('Rätt!!')
            correct_answears += 1
        elif guess == 'exit!':
            # Avslutar programmet
            return
        else:
            print(f'Fel! Rätt svar är {glosor[words_lang1[i]]}')

    print(f'Antal rätta svar: {correct_answears} av {len(words_lang1)}')


# Main funktion som kör hela programmet
def main():
    filnamn = input('Vilken fil vill du läsa in glosor ifrån? ')
    gloslista = getGlosorFromFile(filnamn)
    glosquiz(gloslista)


main()


## Test data ##
'''



'''
