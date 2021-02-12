import random


def meni():
    print("**************************")
    print("1 dodaj knjigu")
    print("2 podaci o biblioteci")
    print("3 podaci o knjizi")
    print("x Izlaz ")
    print("**************************")


class biblioteka:

    def __init__(self, imebib):
        self.naziv = imebib
        self.knjige = []


class knjiga:

    def __init__(self, naslov, autor, zanr):
        self.isbn = str(random.randint(1, 1000))
        self.naslov = naslov
        self.autor = autor
        self.zanr = zanr
        self.biblioteka = biblioteka


biblioteka = biblioteka("gradska biblioteka")
biblioteka.knjige = [{"Naslov": "Ubiti pticu rugalicu", "Autor": "Harper Li", "Zanr": "roman", "ISBN": str(random.randint(1, 1000))},
                     {"Naslov": "Ana Karenjna", "Autor": "Lav Tolstoj", "Zanr": "roman", "ISBN": str(random.randint(1, 1000))},
                     {"Naslov": "Plavi mercedes", "Autor": "Stiven King", "Zanr": "roman", "ISBN": str(random.randint(1, 1000))},
                     {"Naslov": "Ostri predmeti", "Autor": "Dzilijan Flin", "Zanr": "roman", "ISBN": str(random.randint(1, 1000))}]


def podaci_o_biblioteci():
    print("biblioteka:", biblioteka.naziv)
    print("dostupne knjige: ", biblioteka.knjige)


def dodavanjeknjige():
    naslov = input("unesite naziv: ")
    autor = input("unesite autora: ")
    zanr = input("unesite zanr: ")
    nova_knjiga = knjiga(naslov, autor, zanr)
    biblioteka.knjige.append({"Naslov": nova_knjiga.naslov,
                              "Autor": nova_knjiga.autor,
                              "Zanr": nova_knjiga.zanr,
                              "ISBN": nova_knjiga.isbn})
    print("knjiga je dodata")


def podaci_o_knjigama():
    pretraga_po_isbn = input("Unesite ISBN knjige: ")

    for knjiga in biblioteka.knjige:
        if pretraga_po_isbn == knjiga["ISBN"]:
            print(knjiga)
            x = 1
            break
        else:
            x = 2
    if x == 2:
        print("knjiga nije dostupna")


if __name__ == '__main__':
    while True:
        meni()

        opcija = input(">>> ")

        if opcija == "1":
            dodavanjeknjige()
        if opcija == "2":
            podaci_o_biblioteci()
        if opcija == "3":
            podaci_o_knjigama()
        if opcija == "x":
            break
