hoteli = [
    {"naziv": "Park", "broj zvezdica": "5", "adresa": "Novosadski Sajam 35", "grad": "Novi Sad"},
    {"naziv": "Prezident", "broj zvezdica": "5", "adresa": "Futoska 109", "grad": "Novi Sad"},
    {"naziv": "Hotel Fontana", "broj zvezdica": "3", "adresa": "Vrsacka 11", "grad": "Novi Sad"},
    {"naziv": "Hotel Moskva", "broj zvezdica": "4", "adresa": "Bulevar Jase Tomica 1", "grad": "Novi Sad"}]


def meni():
    print("**************************")
    print("1 kreiranje novog hotela \n"
          "2 ispis svih hotela\n"
          "x izlaz")
    print("**************************")


class hotel:
    def __init__(self, naziv, adresa, grad):
        self.naziv = naziv
        self.adresa = adresa
        self.grad = grad
    def __str__(self):
        return f"naziv: {self.naziv}" \
               f"adresa: {self.adresa}" \
               f"grad: {self.grad}"

class Hotel(hotel):
    def __init__(self, brzvezdica):
        hotel.__init__(self)
        self.brzvezdica = brzvezdica

    def __str__(self):
        return f"naziv: {self.naziv}, adresa: {self.adresa}, broj zvezdca: {self.brzvezdica}, grad: {self.grad}"

    def dodavanje_hotela(self):
        self.naziv = input("naziv hotela: ")
        self.grad = input("grad u kom se hotel nalazi: ")
        self.brzvezdica = input("broj zvezdica hotela: ")
        self.adresa = input("adresa na kojoj se hotel nalazi: ")
        hoteli.append({"naziv": self.naziv, "adresa": self.adresa, "broj zvezdica": self.brzvezdica, "grad": self.grad})


if __name__ == '__main__':
    while True:
        meni()

        opcija = input("")

        if opcija == '1':
            h = Hotel
            Hotel.dodavanje_hotela(h)
            print("hotel je dodat", end='\n')
        elif opcija == '2':
            i = 0
            for a in hoteli:
                print(hoteli[i], end='\n')
                i = i + 1
        elif opcija == 'x':
            print("kraj")
            break
        else:
            print("pogresn unos, unesite ponovo.")