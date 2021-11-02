# Jesper Svensson & Erik Smeds 2021-11-02


# Hämtar glosor från en fil, vars filnamn skickas som en parameter,
# sedan returneras glosorna
def getGlosorFromFile(filnamn):
    glosor = dict()  # Skapar en dictionary
    with open(filnamn, "r", encoding="utf8") as glosfile:  # Öppnar filen
        # Går igenom alla rader i textfilen
        # På varje rad finns ett ordpar som delas upp och läggs in i dictionaryn
        # med ena språket som key och andra som value
        for rad in glosfile:
            if rad.find('>') > 0:
                glosor['lang'] = rad.strip().split(">")
            else:
                wordpair = rad.strip()  # Rensar strängen från mellanslag och radbryten
                wordpair = wordpair.split(";")  # Delar orden
                language1 = wordpair[0]
                language2 = wordpair[1]
                glosor[language1] = language2

        # Om inte språket var angivet i filen
        if 'lang' not in glosor:
            glosor['lang'] = ['Språk1', 'Språk2']
    glosfile.close()
    return glosor


# Denna funktionen kör själva quizen
def glosquiz(glosor):
    # Kollar så det inte blivit något fel vid inläsningen av glosorna
    if len(glosor) < 2:
        print('Inga glosor hittades!')
        return

    # Lista med de två språknamnen glosorna är på
    lang = glosor.pop('lang')

    # Skriver ut vilket språk de olika kolumnerna är på
    spaces = 20 - len(lang[0]) - len(lang[1])
    print(lang[0], spaces * ' ', lang[1])
    print('=' * 22)

    # Lista med orden från det första språket/alla keys
    all_words_lang1 = list(glosor.keys())

    # Skriver ut alla ord så man kan träna på dem
    for word_lang1 in all_words_lang1:

        # Sparar ordet på det andra språket
        word_lang2 = glosor[word_lang1]

        # Skriver ut glosorna i två kolumner
        spaces = 20 - len(word_lang1) - len(word_lang2)
        print(word_lang1, spaces * ' ', word_lang2)

    # Quizen
    print('\n'*2)  # Gör lite radbyten
    print(f'Nu ska du översätta ordens som står på', lang[0])
    print('='*46)

    correct_answears = 0  # Sparar antalet rätt man fått

    # Loopar igenom allar ord i listan och låter användaren skriva in översättningen
    for word_lang1 in all_words_lang1:

        print(f'Vad betyder {word_lang1}?')

        guess = input('Skriv här: ')

        # Jämför användarens svar och det korrekta svaret
        if guess == glosor[word_lang1]:
            print('Rätt!!')
            correct_answears += 1
        elif guess == 'exit!':
            # Avslutar programmet
            return
        else:
            print(f'Fel! Rätt svar är {glosor[word_lang1]}')

    print(f'Antal rätta svar: {correct_answears} av {len(all_words_lang1)}')


# Main funktion som kör hela programmet
def main():
    filnamn = input('Vilken fil vill du läsa in glosor ifrån? ')
    gloslista = getGlosorFromFile(filnamn)
    glosquiz(gloslista)


main()


## Test data ##
# Alla inputs från användaren står inom ** **
'''
Vilken fil vill du läsa in glosor ifrån? **setswana.txt**
Svenska       Setswana
======================
pumpa          lerotse
gröt            bogobe
kött              nama
spenat          morogo
fil             madila
kyckling          koko
majs             mmidi
bönor           dinawa



Nu ska du översätta ordens som står på Svenska
==============================================
Vad betyder pumpa?
Skriv här: **lerotse**
Rätt!!
Vad betyder gröt?
Skriv här: **bogobe**
Rätt!!
Vad betyder kött?
Skriv här: **nama**
Rätt!!
Vad betyder spenat?
Skriv här: **sajd**
Fel! Rätt svar är morogo
Vad betyder fil?
Skriv här: **jag vet ej**
Fel! Rätt svar är madila
Vad betyder kyckling?
Skriv här: **koko**
Rätt!!
Vad betyder majs?
Skriv här: **oklart**
Fel! Rätt svar är mmidi
Vad betyder bönor?
Skriv här: **idk**
Fel! Rätt svar är dinawa
Antal rätta svar: 4 av 8


'''
