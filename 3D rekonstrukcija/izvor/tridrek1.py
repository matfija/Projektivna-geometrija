#!/usr/bin/env python3

# Ukljucivanje sistemskog modula
from sys import exit as greska

# Ukljucivanje modula za matematiku
import numpy as np
import numpy.linalg as LA

# Fja za 3D rekonstrukciju
def rekonstruisi():
  #####################################################
  ##### 3D REKONSTRUKCIJA IZ RAVANSKIH PROJEKCIJA #####
  #####################################################
  
  # Piksel koordinate vidljivih tacaka (osam), na
  # osnovu kojih se odredjuje fundamentalna matrica
  x1 = np.array([958, 38, 1.])
  y1 = np.array([933, 33, 1.])
  x2 = np.array([1117, 111, 1.])
  y2 = np.array([1027, 132, 1.])
  x3 = np.array([874, 285, 1.])
  y3 = np.array([692, 223, 1.])
  x4 = np.array([707, 218, 1.])
  y4 = np.array([595, 123, 1.])
  x9 = np.array([292, 569, 1.])
  y9 = np.array([272, 360, 1.])
  x10 = np.array([770, 969, 1.])
  y10 = np.array([432, 814, 1.])
  x11 = np.array([770, 1465, 1.])
  y11 = np.array([414, 1284, 1.])
  x12 = np.array([317, 1057, 1.])
  y12 = np.array([258, 818, 1.])

  # Vektori tih tacaka, bez normalizacije
  xx = np.array([x1, x2, x3, x4, x9, x10, x11, x12])
  yy = np.array([y1, y2, y3, y4, y9, y10, y11, y12])

  # Jednacina y^T * F * x = 0, gde su nepoznate
  # koeficijenti trazene fundamentalne matrice
  jed = lambda x, y: np.array([np.outer(y, x).flatten()])

  # Matrica formata 8x9 koja predstavlja osam
  # jednacina dobijenih iz korespondencija
  jed8 = np.concatenate([jed(x, y) for x, y in zip(xx, yy)])

  # DLT algoritam, SVD dekompozicija
  SVDJed8 = LA.svd(jed8)

  # Vektor koeficijenata fundamentalne matrice,
  # dobijen kao poslednja vrsta matrice V^T
  Fvector = SVDJed8[-1][-1]

  # Fundamentalna matrica napravljena od vektora
  FF = Fvector.reshape(3, 3)

  # Funkcija za proveru vazi li stvarno y^T * F * x = 0
  test = lambda x, y: y @ FF @ x

  # Vidimo da su brojevi stvarno bliski nuli
  testrez = np.array([test(x, y) for x, y in zip(xx, yy)])

  # Determinanta je takodje bliska nuli
  det = LA.det(FF)

  # SVD dekompozicija fundamentalne matrice
  SVDFF = LA.svd(FF)
  U, DD, VT = SVDFF

  # Treca vrsta V^T je prvi epipol, resenje jednacine
  # F * e1 = 0, najmanja sopstvena vrednost matrice
  e1 = VT[-1]

  # Afine koordinate prvog epipola
  norm = lambda tacka: tacka/tacka[-1]
  e1 = norm(e1)

  # Za drugi epipol ne resavamo F^T * e2 = 0,
  # vec primecujemo da je SVD dekompozicija F^T
  # transponat one od F, tako da je drugi epipol
  # poslednja kolona matrice U prvog razlaganja
  e2 = U[:, -1]

  # Afine koordinate drugog epipola
  e2 = norm(e2)

  #####################################################
  ##### POSTIZANJE USLOVA DET(FF)=0, SING. CONST. #####
  #####################################################

  # Zeljena matrica je singularna
  DD1 = np.diag([1, 1, 0]) @ DD
  DD1 = np.diag(DD1)

  # Zamena matrice DD novom DD1 i tako
  # dobijanje nove fundamentalne matrice
  FF1 = U @ DD1 @ VT

  # Iste su im U i V u dekompoziciji, pa
  # su isti epipolovi, ali FF1 ima determinantu
  # blizu nuli, pa je bolje nju koristiti
  det1 = LA.det(FF1)

  # Preostale vidljive tacke
  x6 = np.array([1094, 536, 1.])
  y6 = np.array([980, 535, 1.])
  x7 = np.array([862, 729, 1.])
  y7 = np.array([652, 638, 1.])
  x8 = np.array([710, 648, 1.])
  y8 = np.array([567, 532, 1.])
  x14 = np.array([1487, 598, 1.])
  y14 = np.array([1303, 700, 1.])
  x15 = np.array([1462, 1079, 1.])
  y15 = np.array([1257, 1165, 1.])
  y13 = np.array([1077, 269, 1.])

  ###################################################
  ##### REKONSTRUKCIJA SKRIVENIH TACAKA #############
  ###################################################

  # Neophodno je naci koordinate nevidljivih tacaka
  krstx = lambda a, b, c, d, e, f, g, h, i, j: np.cross(
          np.cross(np.cross(np.cross(a, b), np.cross(c, d)), e),
          np.cross(np.cross(np.cross(f, g), np.cross(h, i)), j))

  krst = lambda *args: np.round(norm(krstx(*args)))

  # Nevidljive tacke prve projekcije
  x5 = krst(x4, x8, x6, x2, x1,
            x1, x4, x3, x2, x8)

  x13 = krst( x9, x10, x11, x12, x14,
             x11, x15, x10, x14,  x9)

  x16 = krst(x10, x14, x11, x15, x12,
              x9, x10, x11, x12, x15)

  # Nevidljive tacke druge projekcije
  y5 = krst(y4, y8, y6, y2, y1,
            y1, y4, y3, y2, y8)

  y16 = krst(y10, y14, y11, y15, y12,
              y9, y10, y11, y12, y15)

  ###################################################
  ##### TRIANGULACIJA ###############################
  ###################################################

  # Kanonska matrica kamere
  T1 = np.hstack([np.eye(3), np.zeros(3).reshape(3, 1)])

  # Matrica vektorskog mnozenja
  vec = lambda p: np.array([[  0,   -p[2],  p[1]],
                            [ p[2],   0,   -p[0]],
                            [-p[1],  p[0],   0  ]])

  # Matrica drugog epipola
  E2 = vec(e2)

  # Druga matrica kamere
  T2 = np.hstack([E2 @ FF1, e2.reshape(3, 1)])

  # Za svaku tacku po sistem od cetiri jednacine
  # sa cetiri homogene nepoznate, mada mogu i tri
  jednacine = lambda xx, yy: np.array([ xx[1]*T1[2] - xx[2]*T1[1],
                                       -xx[0]*T1[2] + xx[2]*T1[0],
                                        yy[1]*T2[2] - yy[2]*T2[1],
                                       -yy[0]*T2[2] + yy[2]*T2[0]])

  # Afine 3D koordinate
  UAfine = lambda xx: (xx/xx[-1])[:-1]

  # Fja koja vraca 3D koordinate rekonstruisane tacke
  TriD = lambda xx, yy: UAfine(LA.svd(jednacine(xx, yy))[-1][-1])

  # Piksel koordinate sa obe slike
  slika1 = np.array([x1, x2, x3, x4, x5, x6, x7, x8, x9,
                     x10, x11, x12, x13, x14, x15, x16])
  
  slika2 = np.array([y1, y2, y3, y4, y5, y6, y7, y8, y9,
                     y10, y11, y12, y13, y14, y15, y16])

  # Rekonstruisane 3D koordinate tacaka
  rekonstruisane = np.array([TriD(x, y) for x, y
                             in zip(slika1, slika2)])

  # Mnozenje z-koordinate, posto nije bilo normalizacije
  rekonstruisane400 = np.array([*map(lambda x:
                                     np.diag([1, 1, 400]) @ x,
                                     rekonstruisane)])

  # Ivice rekonstruisanih objekata
  iviceMala = np.array([[1, 2], [2, 3], [3, 4], [4, 1],
                        [5, 6], [6, 7], [7, 8], [8, 5],
                        [1, 5], [2, 6], [3, 7], [4, 8]])

  iviceVelika = np.array([[ 9, 10], [10, 11], [11, 12], [12,  9],
                          [13, 14], [14, 15], [15, 16], [16, 13],
                          [ 9, 13], [10, 14], [11, 15], [12, 16]])

  # Vracanje rezultata
  return rekonstruisane400, iviceMala, iviceVelika

# Ispitivanje globalne promenljive koja sadrzi
# ime programa kako bi se znalo da li je pravilno
# pokrenut, a ne npr. samo importovan ili uzet
# kao ulaz programu koji interpretira kod
if __name__ == '__main__':
  greska('Tridrek nije samostalan program! Pokrenite main!')
