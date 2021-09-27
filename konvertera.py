#Jesper och Jonas

#Konverteringsprogram med grafiskt gränssnitt

from tkinter import *

def inches2cm(inch): 
    return 2.54*inch

def konvertera(indata):
    utmatning["text"] = str(inches2cm(indata))

STORLEK = 20
TIMES = ("Times", STORLEK)
COURIER = ("Courier", STORLEK)
rot = Tk()

rot.title("Lindas konverteringsprogram")

huvudRam = Frame(rot)
huvudRam.grid()

info = Label(text = "Konvertera inches till cm", font = TIMES)
info.grid(row = 0, column = 0, padx = 5, pady = 5)

inmatning = Entry(font=COURIER, width = 11)
inmatning.grid(row=1, column = 0, padx = 5, pady = 5, sticky = E)

ledtext = Label(text = "inch", font=TIMES)
ledtext.grid(row = 1, column = 1, padx = 5, pady = 5, sticky = W)

utmatning = Label(font=COURIER, width = 4)
utmatning.grid(row=2, column = 0, padx = 5, pady = 5)

svarstext = Label(text = "cm", font=TIMES)
svarstext.grid(row = 2, column = 1, padx = 5, pady = 5, sticky = W)

knapp = Button(text = "Konvertera", font = TIMES, command = lambda: konvertera(float(inmatning.get())))
knapp.grid(row = 3, column = 1, padx = 5, pady = 5)

rot.mainloop()