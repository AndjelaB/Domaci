def FrazaIAkronim():
    fraza = input("fraza: ")
    reci = fraza.split()
    akronim = ""
    for i in reci:
        akronim = akronim + i[0].upper()

    print("akronim: ", akronim)

if __name__ == '__main__':
    FrazaIAkronim()
