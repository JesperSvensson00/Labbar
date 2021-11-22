# Jeppe och Erik 2021-11-22
from Recipe import Recipe


class Foodset(set):
    # Returnerar en sträng med alla ingredienser och ett mellanslag mellan varje.
    def __str__(self):
        ingredienser = ""
        for obj in self:
            ingredienser += obj + " "
        return ingredienser.strip()

    # Returnerar ture/false om det finns mindre än 6 ingredienser
    def simple(self):
        return len(self) < 6

    # Returnerar en sorterad lista med alla ingredienser
    def ordered(self):
        return sorted(self)


# Läser in filen med all data för alla recept
def inläsning(filnamn):
    with open(filnamn, "r", encoding="utf8") as file:
        alla_recept = []
        # Läser igenom alla rader i recept  filen
        for rad in file:
            recept = rad.strip().split(";")  # Lista med all data för receptet
            namn = recept[0]
            ingredienser = Foodset(recept[1:])

            # Skapar ett nytt recept objekt
            nyttRecept = Recipe(namn, ingredienser)
            # Lägger till det i listan med alla objekt
            alla_recept.append(nyttRecept)
        return alla_recept


# Skriver ut alla recept och vilka av användarens allergier som finns i dem i en fil
def allergener_till_fil(utfilnamn, alla_recept, allergier):
    with open(utfilnamn, "w", encoding="utf8") as file:
        for recept in alla_recept:
            # jämför ingredienser i recept med allergier_set
            allergener_i_recept = recept.ingredients.intersection(allergier)
            allergener_i_recept = Foodset(allergener_i_recept)

            # Kollar om det fanns några allergier i receptet
            if len(allergener_i_recept) == 0:
                file.write(recept.dish +
                           " inehåller inga av dina allergener" + "\n")
                print(recept.dish, "inehåller inga av dina allergener")
            else:
                file.write(recept.dish + " inehåller " +
                           str(allergener_i_recept) + "\n")
                print(recept.dish, "inehåller", allergener_i_recept)


# Main funktion
def main():
    alla_recept = inläsning("ingredienser.txt")
    allergier_lista = input("Vad är du allergisk mot? : ").strip().split(' ')
    allergier_set = Foodset(allergier_lista)

    ut_filnamn = input("Vilken fil vill du skriva ut på? : ")
    allergener_till_fil(ut_filnamn, alla_recept, allergier_set)
    print("Utskriften finns nu på filen " + ut_filnamn)


main()


"""
Vad är du allergisk mot? : ägg gluten
Vilken fil vill du skriva ut på? : matkoll.txt

Adas Polo inehåller inga av dina allergener      
Burritos inehåller gluten
Chili con carne inehåller inga av dina allergener
Falafel med myntasås inehåller ägg
Fiskgratäng inehåller gluten
Gräddtårta inehåller ägg gluten
Jordnötskakor inehåller inga av dina allergener  
Kladdkaka inehåller ägg
Minestrone inehåller inga av dina allergener
Paella inehåller inga av dina allergener
Pannkakor inehåller ägg gluten
Rårakor inehåller inga av dina allergener
Räksallad inehåller ägg
Spaghetti carbonara inehåller ägg gluten
Spenatlasagne inehåller gluten
Tofugryta inehåller inga av dina allergener

Utskriften finns nu på filen matkoll.txt
"""

""" I filen matkoll.txt
Adas Polo inehåller inga av dina allergener
Burritos inehåller gluten 
Chili con carne inehåller inga av dina allergener
Falafel med myntasås inehåller ägg 
Fiskgratäng inehåller gluten 
Gräddtårta inehåller gluten ägg 
Jordnötskakor inehåller inga av dina allergener
Kladdkaka inehåller ägg 
Minestrone inehåller inga av dina allergener
Paella inehåller inga av dina allergener
Pannkakor inehåller gluten ägg 
Rårakor inehåller inga av dina allergener
Räksallad inehåller ägg 
Spaghetti carbonara inehåller gluten ägg 
Spenatlasagne inehåller gluten 
Tofugryta inehåller inga av dina allergener
"""
