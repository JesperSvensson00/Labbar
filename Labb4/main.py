class Fro:

    def __init__(self, namn, grobarhet, pris):
        self.namn = namn
        self.grobarhet = grobarhet  # i procent (int)
        self.pris = pris            # i SEK (float)

    def __str__(self):
        return self.namn + " " + str(self.pris)

    def pris_med_moms(self):
        return self.pris*1.25

    def etikett(self):
        print(" -----", self.namn, "-----")
        print("grobarhet:", self.grobarhet, "%")
        print("pris:", self.pris)

    def rea(self, reapris):
        self.pris = reapris


def main():
    solros = Fro("Solros", 3, 12.3)

    solros.etikett()

    solros.rea(10)
    print("Reapris!!!", solros.pris)

    print(solros.pris_med_moms())

    print(solros)


main()
