def unos_korisnika():
    ime = input("Unesite korisnicko ime: ")
    sifra = input("Unesite lozinku: ")
    file.write(ime + ' | ')
    file.write(sifra)
    file.write("\n")


file = open("treci.txt", "a")

unos = True

while unos:
    unos_korisnika()
    print("**********")
    a = input("Da li zelite da nastavite?(da|ne): ")
    if a == 'da':
        unos = True
    elif a == 'ne':
        break
    else:
        print("pogresan unos")

file.close()
