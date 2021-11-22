class Recipe():
    # Init funktion
    def __init__(self, dish, ingredients):
        self.dish = dish
        self.ingredients = ingredients

    # Returnera en sträng med namn och ingredienser
    def __str__(self):
        return f'{self.dish} innehåller {self.ingredients}'
