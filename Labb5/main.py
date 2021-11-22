# Labb 5 - Jesper & Niklas 2021-11-16
class Track:
    # Init funktion
    def __init__(self, track_name, artist_name, release_date, duration, explicit, popularity):

        self.track_name = track_name
        self.artist_name = artist_name
        self.release_date = release_date
        self.duration = duration
        self.explicit = explicit
        self.popularity = popularity

    def __str__(self):  # Returner info om sången som strängar
        return f'Artistnamn: {self.artist_name}, Låttitel: {self.track_name}, Popularitet: {self.popularity}'

    def __lt__(self, other):  # Jämför objektens artistnamn. Om de är samma jämför den låtnamnet
        if self.artist_name == other.artist_name:
            return self.track_name < other.track_name
        else:
            return self.artist_name < other.artist_name

    def censur(self):  # Returnera true/false om låten är explicit eller ej.
        return self.explicit

    def tidText(self):  # Returnera en text tiden i minuter och sekunder
        sec_init = int(self.duration/1000)  # Låtens längd i hela sekunder
        minutes = int(sec_init/60)          # Låtens längd i hela minuter
        # Låtens längd i sekunder minus de hela minuterna
        seconds = sec_init - minutes*60

        # Ser till att tiden skrivs på formen mm:ss
        minutes = minutes if minutes > 9 else '0' + str(minutes)
        seconds = seconds if seconds > 9 else '0' + str(seconds)

        return str(minutes) + ":" + str(seconds)

    def minuter(self):  # Returnera tiden i minuter
        sec_init = int(self.duration/1000)  # Låtens längd i hela sekunder
        minutes = int(sec_init/60)          # Låtens längd i hela minuter

        return minutes


# Läser in data filen och returnera en lista
# med alla rader om gjorda till listor
def createTrackList(filename):
    all_rows = []  # Sparar alla rader omgjorda till listor
    with open(filename, 'r', encoding='utf8') as file:
        for row in file:
            data = row.strip().split(',')  # Gör om raden till en lista med data
            all_rows.append(data)

    track_list = []  # Lista med alla track objekt

    # Går igenom listan med data-listor (hoppar över den första som är rubriker)
    for track_data in all_rows[1:]:

        # All "intresant" data
        track_name = track_data[1]
        artist_name = track_data[3]
        release_date = track_data[8]
        duration = int(track_data[12])
        explicit = True if track_data[14] == 'true' else False
        popularity = int(track_data[15])

        # Skapar ett nytt track objekt och skickar med data
        new_track = Track(track_name, artist_name, release_date,
                          duration, explicit, popularity)

        # Sparar det nya objektet i listan
        track_list.append(new_track)

    return track_list


def printList(list):  # "Tar bort" alla låtar som är Explicit och är kortare än tre minuter långa. Printar resten
    for track in list:
        if track.censur() == False and track.minuter() >= 3:
            print(track)


def main():
    # Mainfunktion
    track_list = createTrackList('eurovision_2021.csv')
    printList(track_list)
    track_list.sort()

    print()
    print('===Sorterat===')
    print()

    printList(track_list)


main()

''' Testdata
Artistnamn: Elena Tsagrinou, Låttitel: El Diablo, Popularitet: 43
Artistnamn: THE ROOP, Låttitel: Discoteque, Popularitet: 60
Artistnamn: Tusse, Låttitel: Voices, Popularitet: 63

    ...

Artistnamn: Ana Soklič, Låttitel: Amen, Popularitet: 40
Artistnamn: Tornike Kipiani, Låttitel: You, Popularitet: 38
Artistnamn: Vasil Garvanliev, Låttitel: Here I Stand, Popularitet: 37

===Sorterat===

Artistnamn: Albina, Låttitel: Tick-Tock, Popularitet: 49
Artistnamn: Ana Soklič, Låttitel: Amen, Popularitet: 40
Artistnamn: Blas Cantó, Låttitel: Voy a quedarme, Popularitet: 52

    ...

Artistnamn: Uku Suviste, Låttitel: The lucky one, Popularitet: 44
Artistnamn: VICTORIA, Låttitel: growing up is getting old - Eurovision Version, Popularitet: 48
Artistnamn: Vasil Garvanliev, Låttitel: Here I Stand, Popularitet: 37
'''
