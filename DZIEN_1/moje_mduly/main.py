# import dane
# import dane as dn
from dane import nrfilii as nf
from dane import book as bk
from moje_funkcje.fkolekcje import czytaj_liste,czytaj_slownik

print(nf)
print(bk)

print(f"użycie funkcji z modułu fkolekcje.py")
print(f"lista:")
czytaj_liste(nf)
print(f"słownik:")
czytaj_slownik(bk)
