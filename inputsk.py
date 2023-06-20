def vypis_typy(zoznam):
    for prvok in zoznam:
        typ = type(prvok)
        if typ == int or typ == float:
            print(prvok, "- číslo")
        elif typ == str:
            print(prvok, "- reťazec")
        else:
            print(prvok, "- iný typ")

zoznam = [12, 'x', None, 3.14, [], range(5), '123']
vypis_typy(zoznam)



def nakup(zoznam):
    cena = 0
    for i in range(0, len(zoznam), 2):
        mnozstvo = zoznam[i]
        jednotkova_cena = zoznam[i+1]
        cena += mnozstvo * jednotkova_cena
    return cena

cena = nakup([3, 2.5, 0.5, 10, 1.2, 1.2])
print(cena)




def sucin(zoznam):
    if len(zoznam) == 0:
        return 1
    else:
        result = 1
        for prvok in zoznam:
            result *= prvok
        return result


c = [2, 3, 5, 7, 11]
print(sucin(c))
print(sucin(list(range(1, 11))))
print(sucin([2] * 20))