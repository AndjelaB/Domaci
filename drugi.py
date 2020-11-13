def spajanje():
    str1 = input("unesite prvi string: ")
    str2 = input("unesite drugi string: ")
    strp = str1[0:3]
    strd = str2[-3:]
    novistr = strp + strp + strd
    print(novistr)

if __name__ == '__main__':
    spajanje()
