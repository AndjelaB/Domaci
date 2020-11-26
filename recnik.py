print("*****************************")
print("1. recnik")
print("2. unos novih reci")
print("3. izmena")
print("4. brisanje reci")
print("5. izlaz")
print("*****************************")

reci = {
    "1": "danas",
    "2": "je",
    "3": "lep",
    "4": "dan"
    }

def noveReci():
    broj = input("unesite broj reci koju zelite da zamenite: ")
    n = len(reci)
    while broj <= str(n):
        print("vec postoji")
        broj = input("unesite broj reci koju zelite da zamenite: ")
    novarec = input("unesite rec: ")
    reci[broj] = novarec
    print(reci)

def izmena():
    broj = input("unesite broj reci koju zelite da zamenite: ")
    zamena = input("unesite rec: ")
    reci[broj] = zamena
    print(reci)

def brisanje():
    broj = input("unesite broj reci koju zelite da izbrisete: ")
    del reci[broj]
    print(reci)


if __name__ == '__main__':
    while True:
        a = input("unesite broj: ")
        if a == '1':
            print(reci)
        elif a == '2':
            noveReci()
        elif a == '3':
            izmena()
        elif a == '4':
            brisanje()
        else:
            print("kraj")
            break



