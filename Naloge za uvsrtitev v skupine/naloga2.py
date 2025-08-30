def vrni_denar(znesek, vnos):
    if vnos < znesek:
        print(f"'Premalo denarja! Manjka še {znesek - vnos:.2f} €'") 
    else:
         bankovci = [100, 50, 20, 10, 5, 2, 1, 0.5, 0.2, 0.1, 0.05, 0.02, 0.01] 
         razlika = vnos - znesek 
         stevilo = {}
         for bankovec in bankovci:
            količina = int(razlika // bankovec)
            if količina != 0:
                stevilo[str(bankovec)] = količina
                razlika = razlika - bankovec * količina
         print(stevilo)
vrni_denar(15.99, 15)
vrni_denar(13.37, 20)