# Erik Smeds och Jesper Svensson 2021-11-09

class Klocka:
  # Init funktion
    def __init__(self, time):
        self.time = time  # Tid i minuter dvs en dag/24 h är 1440 min
     
    
    # String funktion
    def __str__(self):
        timmar = (int(self.time/60))  # Antalet hela timmar int() avrundra ner
        minuter = (self.time % 60)  # Antalet minuter

        # Lägger till en 0:a om timmarna eller minuterna är ensiffrig
        timmar = timmar if timmar > 9 else '0' + str(timmar)
        minuter = minuter if minuter > 9 else '0' + str(minuter)

        return str(timmar) + ':' + str(minuter)

    
    # Lägger till en minut till klockan
    # Nollställer om den tickar över 24 timmar
    def tick(self):
        self.time += 1
        
        # Om tiden överstiger 24 timmar börjar den om på 0 som en vanlig klocka
        self.time = self.time%(24*60)
        
        
            
    # Printa ut tiden
    def printKlocka(self):
        timmar = (int(self.time/60))  # Antalet hela timmar int() avrundra ner
        minuter = (self.time % 60)  # Antalet minuter

        # Lägger till en 0:a om timmarna eller minuterna är ensiffrig
        timmar = timmar if timmar > 9 else '0' + str(timmar)
        minuter = minuter if minuter > 9 else '0' + str(minuter)

        print("Klockan är: " + str(timmar) + ':' + str(minuter))

        
    # Sätter tiden till ett angivet värde
    def setTime(self, time):
        self.time = time

        # Om tiden överstiger 24 timmar börjar den om på 0 som en vanlig klocka
        self.time = self.time%(24*60)

            
    # Returnera tiden i antalet minuter
    def getTime(self):
        return self.time

    
    # Returnera tiden i antalet minuter minus hela timmar
    def getMinutes(self):
        return self.time % 60

    
    # Returnera antalet hela timmar
    def getHours(self):
        return int(self.time/60)


klocka = Klocka(0)


# Test funktion 1
def test1(klocka):
    print('------- Test 1 --------\nTestar printKlocka')
    klocka.tick()
    klocka.printKlocka()


# Test funktion 2
def test2(klocka):
    print('------- Test 2 --------')

    print("Tid innan tick:", klocka)

    klocka.tick()

    print("Tid efter tick:", klocka)


# Test funktion 3
def test3(klocka):
    print('------- Test 3 --------')

    print("Tid innan set time:", klocka)

    klocka.setTime(6686)

    klocka.tick()

    print("Tid innan set time och tick:", klocka)


# Här körs alla test funktioner
test1(klocka)
test2(klocka)
test3(klocka)

'''
------- Test 1 --------
Testar printKlocka
Klockan är: 00:01
------- Test 2 --------
Tid innan tick: 00:01
Tid efter tick: 00:02
------- Test 3 --------
Tid innan set time: 00:02
Tid innan set time och tick: 15:27
'''
