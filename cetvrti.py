file = open("treci.txt", "r")
for line in file.readlines():
    korisnik = line.split("|")
    name = korisnik[0]
    sifra = korisnik[1]
    print("korisnicko ime: " + name)
    print("sifra: " + sifra)
file.close()