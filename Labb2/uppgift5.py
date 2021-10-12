# Jesper och Kawthar 2021-10-12

import random

# Skriver ut info om hur långe ne foot är i meter


def foot():
    foot = 30.48
    print("En foot är", foot, "cm.")


# Omvandlar inputvärdet i meter till foot och returnera det
def meter_till_foot(längd):
    foot = 0.3048
    svar = längd * foot
    return svar


# Skriver ut en multiplikations tabell förett angivet värde
def skriv_ut_tabell():
    antal_gånger = int(input("Hur många gånger vill du köra loopen? "))
    for i in range(1, antal_gånger+1):
        print(meter_till_foot(i))


# Denna funktionen slumpar en längd i meter och låter användaren gissa på vad det blir i foot
def gissa():
    print("\n\nNu kommer du få gissa på vad talet (i meter) nedan blir i foot:")

    # Slumpar ett tal mellan 1 och 10 och skriver ut det
    tal = random.randint(1, 10)
    print("Antal meter:", tal)

    antal_försök = 1
    while True:  # Loopar till användaren svara rätt
        # Omvandlar värdet till en float
        svar = float(input("Skriv vad det blir i foot: "))
        if svar == meter_till_foot(tal):
            print("Rätt!")
            print("Du gjorde", antal_försök, "försök.")
            break  # Avbryter loopen
        else:
            print("Fel!")

        antal_försök += 1


# Kör alla funktioner
def main():
    foot()
    skriv_ut_tabell()
    gissa()


main()

'''
-----När vi kör programmet visas följande-----
En foot är 30.48 cm.
Hur många gånger vill du köra loopen? *Skriver in 10*
0.3048
0.6096
0.9144000000000001
1.2192
1.524
1.8288000000000002
2.1336
2.4384
2.7432000000000003
3.048

Nu kommer du få gissa på vad talet (i meter) nedan blir i foot:
Antal meter: 8
Skriv vad det blir i foot: *Skriver in 4*
Fel!
Skriv vad det blir i foot: *Skriver in 2.4384*
Rätt!
Du gjorde 2 försök.
-----Slut-----
'''
