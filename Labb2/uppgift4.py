import random


def main():
    tal1 = random.randint(1, 10)
    tal2 = random.randint(1, 10)
    produkt = tal1 * tal2

    print("Tal 1:", tal1)
    print("Tal 2:", tal2)

    antal_försök = 1
    while True:
        svar = int(input("Skriv vad produkten blir: "))
        if svar == produkt:
            print("Rätt!")
            print("Du gjorde", antal_försök, "försök.")
            break
        else:
            print("Fel!")

        antal_försök += 1


main()
