#!/usr/bin/env python3

# Ukljucivanje sistemskog modula
from sys import exit as greska

# Ukljucivanje modula za matematiku
import numpy as np
import numpy.linalg as LA

# Normalizacija tacaka
def normalizuj(tacke):
  # Afinizacija tacaka
  tacke = np.array([*map(lambda x:
                         (x[0]/x[2], x[1]/x[2], 1),
                         tacke)])

  # Teziste tacaka
  tez = np.mean(tacke, axis = 0)

  # Matrica translacije
  g = np.array([[  1,   0, -tez[0]],
                [  0,   1, -tez[1]],
                [  0,   0,    1  ]])

  # Transliranje svih tacaka
  tacke = np.array([*map(lambda x: g@x, tacke)])

  # Prosek rastojanja
  rast = np.mean(np.array([*map(lambda x:
                                np.sqrt(x[0]**2 + x[1]**2),
                                tacke)]))

  # Matrica homotetije
  s = np.array([[np.sqrt(2)/rast,         0,           0     ],
                [       0,         np.sqrt(2)/rast,    0     ],
                [       0,                0,           1     ]])

  # Skaliranje svih tacaka;
  # vracanje i transformacije
  return s@g, np.array([*map(lambda x: s@x, tacke)])

# Fja za 3D rekonstrukciju
def rekonstruisi():
  #####################################################
  ##### 3D REKONSTRUKCIJA IZ RAVANSKIH PROJEKCIJA #####
  #####################################################
  
  # Piksel koordinate vidljivih tacaka (osam), na
  # osnovu kojih se odredjuje fundamentalna matrica
  x1  = np.array([331,  76, 1.])
  y1  = np.array([393,  75, 1.])
  x2  = np.array([496,  55, 1.])
  y2  = np.array([561,  76, 1.])
  x3  = np.array([717, 167, 1.])
  y3  = np.array([565, 198, 1.])
  x4  = np.array([539, 188, 1.])
  y4  = np.array([373, 196, 1.])
  x19 = np.array([923, 600, 1.])
  y19 = np.array([860, 655, 1.])
  x20 = np.array([701, 780, 1.])
  y20 = np.array([457, 778, 1.])
  x23 = np.array([920, 786, 1.])
  y23 = np.array([856, 839, 1.])
  x24 = np.array([696, 988, 1.])
  y24 = np.array([462, 977, 1.])

  # Vektori tih tacaka
  xx = np.array([x1, x2, x3, x4, x19, x20, x23, x24])
  yy = np.array([y1, y2, y3, y4, y19, y20, y23, y24])

  # Normalizacija tacaka
  tx, xxx = normalizuj(xx)
  ty, yyy = normalizuj(yy)

  # Jednacina y^T * F * x = 0, gde su nepoznate
  # koeficijenti trazene fundamentalne matrice
  jed = lambda x, y: np.array([np.outer(y, x).flatten()])

  # Matrica formata 8x9 koja predstavlja osam
  # jednacina dobijenih iz korespondencija
  jed8 = np.concatenate([jed(x, y) for x, y in zip(xxx, yyy)])

  # DLT algoritam, SVD dekompozicija
  SVDJed8 = LA.svd(jed8)

  # Vektor koeficijenata fundamentalne matrice,
  # dobijen kao poslednja vrsta matrice V^T
  Fvector = SVDJed8[-1][-1]

  # Fundamentalna matrica napravljena od vektora
  FFt = Fvector.reshape(3, 3)

  #####################################################
  ##### POSTIZANJE USLOVA DET(FF)=0, SING. CONST. #####
  #####################################################

  # SVD dekompozicija fundamentalne matrice
  Ut, DDt, VTt = LA.svd(FFt)

  # Zeljena matrica je singularna
  DD1t = np.diag([1, 1, 0]) @ DDt
  DD1t = np.diag(DD1t)

  # Zamena matrice DD novom DD1 i tako
  # dobijanje nove fundamentalne matrice
  FF1t = Ut @ DD1t @ VTt

  # Vracanje u pocetni koordinatni sistem
  FF = ty.T @ FF1t @ tx

  #####################################################
  ##### ODREDJIVANJE EPIPOLOVA ########################
  #####################################################

  # SVD dekompozicija fundamentalne matrice
  U, _, VT = LA.svd(FF)

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

  ###################################################
  ##### REKONSTRUKCIJA SKRIVENIH TACAKA #############
  ###################################################

  # Preostale vidljive tacke
  x5  = np.array([327, 295, 1.])
  x7  = np.array([713, 401, 1.])
  y7  = np.array([565, 423, 1.])
  x8  = np.array([539, 431, 1.])
  y8  = np.array([377, 422, 1.])
  x9  = np.array([261, 340, 1.])
  y9  = np.array([282, 311, 1.])
  y10 = np.array([712, 332, 1.])
  x11 = np.array([775, 367, 1.])
  y11 = np.array([685, 403, 1.])
  x12 = np.array([310, 416, 1.])
  y12 = np.array([237, 379, 1.])
  x13 = np.array([268, 590, 1.])
  y14 = np.array([713, 566, 1.])
  x15 = np.array([766, 619, 1.])
  y15 = np.array([684, 644, 1.])
  x16 = np.array([315, 670, 1.])
  y16 = np.array([247, 616, 1.])
  x17 = np.array([ 91, 628, 1.])
  y17 = np.array([125, 552, 1.])
  x21 = np.array([ 94, 824, 1.])
  y21 = np.array([131, 720, 1.])

  # Neophodno je naci koordinate nevidljivih tacaka
  krstx = lambda a, b, c, d, e, f, g, h, i, j: np.cross(
          np.cross(np.cross(np.cross(a, b), np.cross(c, d)), e),
          np.cross(np.cross(np.cross(f, g), np.cross(h, i)), j))

  krst = lambda *args: np.round(norm(krstx(*args)))

  # Nevidljive tacke prve projekcije
  x6  = krst( x5,  x1,  x8,  x4,  x2,
              x8,  x5,  x3,  x2,  x7)
  x10 = krst(x16, x13, x12,  x9, x11,
             x12, x11, x16, x15,  x9)
  x14 = krst(x16, x15, x12, x11, x13,
             x16, x13, x12,  x9, x15)
  x18 = krst(x20, x19, x24, x23, x17,
             x24, x21, x20, x17, x19)
  x22 = krst(x20, x19, x24, x23, x21,
             x24, x21, x20, x17, x23)

  # Nevidljive tacke druge projekcije
  y5 =  krst( y8,  y4,  y7,  y3,  y1,
              y4,  y1,  y3,  y2,  y8)
  y6 =  krst( y5,  y1,  y8,  y4,  y2,
              y8,  y5,  y3,  y2,  y7)
  y13 = krst(y15, y16, y10,  y9, y14,
             y16, y12, y15, y11,  y9)
  y18 = krst(y20, y19, y24, y23, y17,
             y24, y21, y20, y17, y19)
  y22 = krst(y20, y19, y24, y23, y21,
             y24, y21, y20, y17, y23)

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
  T2 = np.hstack([E2 @ FF, e2.reshape(3, 1)])

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
                     x10, x11, x12, x13, x14, x15, x16,
                   x17, x18, x19, x20, x21, x22, x23, x24])
  
  slika2 = np.array([y1, y2, y3, y4, y5, y6, y7, y8, y9,
                     y10, y11, y12, y13, y14, y15, y16,
                   y17, y18, y19, y20, y21, y22, y23, y24])

  # Rekonstruisane 3D koordinate tacaka
  rekonstruisane = np.array([TriD(x, y) for x, y
                             in zip(slika1, slika2)])

  # Skaliranje z-koordinate u cilju poboljsanja rezultata
  rekonstruisane380 = np.array([*map(lambda x:
                                     np.diag([1, 1, 380]) @ x,
                                     rekonstruisane)])

  # Ivice rekonstruisanih objekata
  iviceMala = np.array([[1, 2], [2, 3], [3, 4], [4, 1],
                        [5, 6], [6, 7], [7, 8], [8, 5],
                        [1, 5], [2, 6], [3, 7], [4, 8]])

  iviceSrednja = np.array([[ 9, 10], [10, 11], [11, 12], [12,  9],
                           [13, 14], [14, 15], [15, 16], [16, 13],
                           [ 9, 13], [10, 14], [11, 15], [12, 16]])

  iviceVelika = np.array([[17, 18], [18, 19], [19, 20], [20, 17],
                          [21, 22], [22, 23], [23, 24], [24, 21],
                          [17, 21], [18, 22], [19, 23], [20, 24]])

  # Vracanje rezultata
  return rekonstruisane380, iviceMala, iviceSrednja, iviceVelika

# Ispitivanje globalne promenljive koja sadrzi
# ime programa kako bi se znalo da li je pravilno
# pokrenut, a ne npr. samo importovan ili uzet
# kao ulaz programu koji interpretira kod
if __name__ == '__main__':
  greska('Tridrek nije samostalan program! Pokrenite main!')
