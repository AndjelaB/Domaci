class krug:
    def __init__(self, poluprecnik):
        self.poluprecnik = poluprecnik
    def ok(self, obim):
        return f"obim kruga je {obim}"
    def pk(self, povrsina):
        return f"povrsina kruga je {povrsina}"


class pravougaonik:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def op(self, obim):
        return f"obim pravougaonika je {obim}"
    def pp(self, povrsina):
        return f"povrsina pravougaonika je {povrsina}"

class kvadrat:
    def __init__(self, a):
        self.a = a
    def op(self, obim):
        return f"obim kvadrata je {obim}"
    def pp(self, povrsina):
        return f"povrsina kvadrata je {povrsina}"


if __name__ == '__main__':
    ppk = float(input("unesite poluprecnik kruga: "))
    krug = krug(ppk)
    obimk = (2*krug.poluprecnik)*3.14
    print(krug.ok(obimk))
    povrsinak = (krug.poluprecnik*krug.poluprecnik)*3.14
    print(krug.pk(povrsinak))

    a = float(input("unesite stranicu pravouganika (a): "))
    b = float(input("unesite stranicu pravouganika (b): "))
    pravougaonik = pravougaonik(a, b)
    obimp = 2*(pravougaonik.a+pravougaonik.b)
    print(pravougaonik.op(obimp))
    povrsinap = pravougaonik.a*pravougaonik.b
    print(pravougaonik.pp(povrsinap))

    ak = float(input("unesite stranicu kvadrata: "))
    kvadrat = kvadrat(a)
    obimkv = 4 * kvadrat.a
    print(kvadrat.op(obimkv))
    povrsinakv = kvadrat.a * kvadrat.a
    print(kvadrat.pp(povrsinakv))