# app.py

from flask import Flask, render_template

# Ustvarimo instanco aplikacije
app = Flask(__name__)

# Definiramo pot (route) za domačo stran.
# Ko uporabnik obišče '/' (glavni naslov), se izvede funkcija 'domov'.
@app.route('/')
def domov():
    """
    Prikaže domačo stran s preprostim besedilom.
    """
    # Lahko pošljemo tudi spremenljivke v predlogo
    naslov = "Moja prva spletna stran s Flaskom"
    pozdrav = "Dobrodošli na moji novi spletni strani!"
    
    # Funkcija 'render_template' poišče 'domov.html' v mapi 'templates'
    # in vanjo vstavi podane spremenljivke
    return render_template('domov.html', naslov=naslov, pozdrav=pozdrav)

# Glavni del skripte, ki zažene razvojni strežnik.
# 'debug=True' omogoča samodejno ponovno nalaganje kode ob spremembah.
if __name__ == '__main__':
    app.run(debug=True)