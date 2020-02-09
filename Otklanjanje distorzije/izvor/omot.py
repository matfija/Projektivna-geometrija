#!/usr/bin/env python3

# Modul preuzet iz autorovog seminarskog
# rada pisanog za kurs Programske paradigme

# Ukljucivanje sistemskog modula
from sys import exit as greska

# Ukljucivanje funkcionalnog modula
from functools import partial

# Ukljucivanje modula sa operatorima
from operator import gt, itemgetter

# Odredjivanje polozaja prosledjene tacke
def vekt_proiz(t, u, v):
  a = (t[0]-u[0], t[1]-u[1])
  b = (v[0]-u[0], v[1]-u[1])
  
  # Vracanje dela vektorskog proizvoda
  return a[0]*b[1] - a[1]*b[0]

# Vracanje tacaka sa leve strane vektora
def podela(u, v, tacke):
    # lambda t: partial(gt, 0)(partial(vekt_proiz, u=u, v=v)(t))
    # return list(filter(lambda t: vekt_proiz(t, u, v) < 0, tacke))
    return [t for t in tacke if vekt_proiz(t, u, v) < 0]

# Prosirivanje pretrage omotnih tacaka
def prosiri(u, v, tacke):
    # Nema prosirivanja prazne liste
    if not tacke:
        return []

    # Nalazenje najudaljenije tacke
    w = min(tacke, key = partial(vekt_proiz, u=u, v=v))
    
    # Podela pretrage po odredjenoj tacki
    t1, t2 = podela(w, v, tacke), podela(u, w, tacke)
    return prosiri(w, v, t1) + [w] + prosiri(u, w, t2)

# Brzi algoritam za pronalazak konveksnog omotaca
def konveksni_omot(tacke):
    # Prazna lista tacaka nema konveksni omot
    if not tacke:
        return []
    
    # Nalazenje dve tacke omota
    u = min(tacke, key = itemgetter(0))
    v = max(tacke, key = itemgetter(0))
    
    # Podela pretrage na levu i desnu stranu
    levo, desno = podela(u, v, tacke), podela(v, u, tacke)

    # Nalazenje omota na obe strane
    omot = [v] + prosiri(u, v, levo) + [u] + prosiri(v, u, desno)

    # Popravka u slucaju dve tacke
    return [omot[0]] if len(omot) == 2 \
     and omot[0] == omot[1] else omot

# Obavestenje o gresci ukoliko je modul
# pokrenut kao samostalan program
if __name__ == '__main__':
  greska('Omot nije samostalan program! Pokrenite main!')
