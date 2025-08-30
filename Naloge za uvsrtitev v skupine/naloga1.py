def armstrongova_števila (števke):
    n = len (števke)
    vsota = 0
    for števka in števke:
        števka = int(števka)
        vsota = vsota + števka**n
    if vsota != int(števke):
        print("0")
    else:
        print("1")
armstrongova_števila(input("Vnesi število: "))