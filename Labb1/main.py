# Jonas & Jesper 2021-10-04

PRIS_ENKEL = 24
PRIS_30DAGAR = 640

antal_resor = int(
    input('Hur många resor kommer du göra under 30 dagars perioden? (Ange heltal)'))

pris_per_resa30dagar = PRIS_30DAGAR/antal_resor
if pris_per_resa30dagar < PRIS_ENKEL:
    print("Månadskort är billigast! Pris per resa blir", pris_per_resa30dagar, "kr.")
else: 
    print("Enkelresa är billigare!")

#Vi är bäst.
