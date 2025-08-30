def palindrom (beseda):
    dolzina = len(beseda)
    for crke in range(dolzina):
        s_crka = beseda[crke]
        p_crka = beseda[dolzina - 1 - crke]
        if s_crka != p_crka:
            return False
    return True
def odstrani_crke (beseda):
    dolzina = len(beseda)
    for i in range(dolzina):
        if palindrom(beseda[0:dolzina - i]):
            return i
print (odstrani_crke(input("Vnesi besedo: ")))