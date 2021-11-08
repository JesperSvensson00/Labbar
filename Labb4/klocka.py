# Erik Smeds och Jesper Svensson 2021-11-09

class Klocka:

    def __init__(self):
        self.time = 0

    def __str__(self):
        timmar = int(self.time/60)
        minuter = self.time % 60

        timmar = timmar if timmar > 9 else '0' + str(timmar)
        minuter = minuter if minuter > 9 else '0' + str(minuter)

        return str(timmar) + ':' + str(minuter)

    def tick(self):
        self.time += 1

    def printKlocka(self):
        timmar = (int(self.time/60))
        minuter = (self.time % 60)

        timmar = timmar if timmar > 9 else '0' + str(timmar)
        minuter = minuter if minuter > 9 else '0' + str(minuter)

        print(str(timmar) + ':' + str(minuter))

    def setTime(self, time):
        self.time = time

    def getTime(self):
        return self.time

    def getMinutes(self):
        return self.time % 60

    def getMinutes(self):
        return int(self.time/60)


klocka = Klocka()


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

    klocka.tick()

    klocka.setTime(55646)

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
927:26
'''
