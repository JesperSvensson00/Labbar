import random


def foot():
    foot = 30.48
    print("En foot är", foot, "cm.")


def meter_till_foot(längd):
    foot = 0.3048
    svar = längd * foot
    return svar


def skriv_ut_tabell():
    antal_gånger = int(input("Hur många gånger vill du köra loopen? "))
    for i in range(1, antal_gånger+1):
        print(meter_till_foot(i))


def gissa():
    tal = random.randint(1, 10)
    print("Antal meter:", tal)

    antal_försök = 1
    while True:
        svar = float(input("Skriv vad det blir i foot: "))
        if svar == meter_till_foot(tal):
            print("Rätt!")
            print("Du gjorde", antal_försök, "försök.")
            break
        else:
            print("Fel!")

        antal_försök += 1


def main():
    foot()
    skriv_ut_tabell()
    gissa()


main()
