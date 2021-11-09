# Erik Smeds och Jesper Svensson 2021-11-09

class Klocka:
    def __init__(self):
        self.time = 0  # Tid i minuter dvs en dag/24 h är 1440 min
     
    
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
        if self.time > 24 * 60:
            timmar = (int(self.time/60))
            antalet_dygn = int(timmar/24)
            self.time = self.time - antalet_dygn*24*60  # Tar bort antalet dagar i minuter

            
    # Printa ut tiden
    def printKlocka(self):
        timmar = (int(self.time/60))  # Antalet hela timmar int() avrundra ner
        minuter = (self.time % 60)  # Antalet minuter

        # Lägger till en 0:a om timmarna eller minuterna är ensiffrig
        timmar = timmar if timmar > 9 else '0' + str(timmar)
        minuter = minuter if minuter > 9 else '0' + str(minuter)

        print(str(timmar) + ':' + str(minuter))

        
    # Sätter tiden till ett angivet värde
    def setTime(self, time):
        self.time = time

        # Om tiden överstiger 24 timmar börjar den om på 0 som en vanlig klocka
        if self.time > 24 * 60:
            timmar = (int(self.time/60))
            antalet_dygn = int(timmar/24)
            self.time = self.time - antalet_dygn*24*60  # Tar bort antalet dagar i minuter

            
    # Returnera tiden i antalet minuter
    def getTime(self):
        return self.time

    
    # Returnera tiden i antalet minuter minus hela timmar
    def getMinutes(self):
        return self.time % 60

    
    # Returnera antalet hela timmar
    def getHours(self):
        return int(self.time/60)


klocka = Klocka()


# Test funktioner
def test1(klocka):
    print('Test 1')
    klocka.tick()
    print("Efter ett tick är klockan", klocka)


def test2(klocka):
    print('Test 2')

    print(klocka)

    klocka.tick()

    print(klocka)


def test3(klocka):
    print('Test 3')

    print(klocka)

    klocka.setTime(6686)

    klocka.tick()

    klocka.printKlocka()


test1(klocka)
test2(klocka)
test3(klocka)

'''
Test 1
Efter ett tick är klockan 00:01
Test 2
00:01
00:02
Test 3
00:02
15:27
'''
