''' 
Uppgift 1
a) 2
b) 1
c) i main på 3:e raden
d) 0
e) 0
f) längst ner main()

'''

'''
Uppgift 2
'''

# a)


def foot():
    foot = 30.48
    print("En foot är", foot, "cm.")


# b)
foot()
# Fungerar

# c)


def meter_till_foot(längd):
    foot = 0.3048
    svar = längd * foot
    return svar


# d)
print(meter_till_foot(3))
# Funkar


# Uppgift 3
# a)
def main():
    # Skriver ut en multiplikationstabell
    n = 5
    print()
    print("Multiplikationstabell för", n)
    print("-------------")
    for i in range(1, 10):
        print(i*n)
    print()

# b)


def ny_main(n):
    # Skriver ut en multiplikationstabel
    print()
    print("Multiplikationstabell för", n)
    print("-------------")
    multitabell(n)
    print()

# c)


def multitabell(n):
    for i in range(1, 10):
        print(i*n)


ny_main(6)
