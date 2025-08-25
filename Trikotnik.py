#stevilo_vrstic = input("Koliko vrstic želiš, da je program dolg? ")
#for i in range(int(stevilo_vrstic)):
  #  print('*' * (i + 1))

def enakorobni_trikotnik(višina):
    
    for i in range((višina)):
        print(" " * (višina - i - 1), end = "")
        print("*" * (2 * i + 1))
višina = input(int("Koliko vrstic želiš, da je program dolg? "))
enakorobni_trikotnik(višina)