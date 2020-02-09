#!/usr/bin/env python3

# Ukljucivanje modula za matematiku
import numpy as np
import numpy.linalg as LA
from math import sqrt

# Matrica projekcije bazne figure
def nmat(tacke):
  # Izvlacenje tacaka iz ulaza
  A, B, C, D = tacke

  # Postavljanje sistema jednacina
  sistem = np.array([[A[0], B[0], C[0]],
                     [A[1], B[1], C[1]],
                     [A[2], B[2], C[2]]])
  kolona = np.array([D[0], D[1], D[2]])

  # Resavanje postavljenog sistema
  a, b, c = LA.solve(sistem, kolona)

  # Vracanje rezultata prema teoremi
  return np.array([[a*A[0], b*B[0], c*C[0]],
                   [a*A[1], b*B[1], c*C[1]],
                   [a*A[2], b*B[2], c*C[2]]])

# Naivni algoritam projekcije
def naivni(nove, orig = None):
  if orig is None:
      return nmat(nove[:4])

  return nmat(nove[:4]) @ LA.inv(nmat(orig[:4]))

# DLT algoritam projekcije
def DLT(nove, orig):
    # Pravljenje 2nx9 matrice korespondencija
    mat = np.array([]).reshape(0, 9)
    for i in range(len(nove)):
      x, y = orig[i], nove[i]
      mat = np.concatenate((mat,
            np.array([[     0,          0,          0,
                       -y[2]*x[0], -y[2]*x[1], -y[2]*x[2],
                        y[1]*x[0],  y[1]*x[1],  y[1]*x[2]],
                      [ y[2]*x[0],  y[2]*x[1],  y[2]*x[2],
                            0,          0,          0,
                       -y[0]*x[0], -y[0]*x[1], -y[0]*x[2]]])),
                           axis = 0)

    # SVD dekompozicija dobijene matrice
    _, _, v = LA.svd(mat)

    # Vracanje rezultata iz poslednje vrste
    # (kolone ako se posmatra transponat v)
    return v[-1].reshape(3, 3)

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
                                sqrt(x[0]**2 + x[1]**2),
                                tacke)]))

  # Matrica homotetije
  s = np.array([[sqrt(2)/rast,      0,          0     ],
                [     0,       sqrt(2)/rast,    0     ],
                [     0,            0,          1     ]])

  # Skaliranje svih tacaka;
  # vracanje i transformacije
  return s@g, np.array([*map(lambda x: s@x, tacke)])

# Modifikovani DLT
def mDLT(nove, orig):
  # Normalizacija tacaka
  to, orig = normalizuj(orig)
  tn, nove = normalizuj(nove)

  # DLT za normalizovane tacke
  dlt = DLT(nove, orig)

  # Vracanje rezultantne matrice
  return LA.inv(tn) @ dlt @ to

# Fja za testiranje
def test():
  # Slucaj sa cetiri tacke
  orig = np.array([[-5,0,1], [-6,0.5,1], [-5,3,1], [-4,2,1]])
  nove = np.array([[3,0,1], [1,1.5,1], [2.7,2.5,1], [6,2,1]])

  print('Originalne tačke:')
  print(orig)
  print()

  print('Njihove slike:')
  print(nove)
  print()

  print('Naivna matrica:')
  naiv = naivni(nove, orig)
  print(naiv)
  print()

  print('DLT matrica:')
  dlt = DLT(nove, orig)
  print(dlt)
  print()

  print('Skalirana DLT:')
  print(naiv[0][0]/dlt[0][0] * dlt)
  print()

  print('Zaključak: u pitanju je ista transformacija.')
  print()

  print('mDLT matrica:')
  mdlt = mDLT(nove, orig)
  print(mdlt)
  print()

  print('Skalirana mDLT:')
  print(dlt[0][0]/mdlt[0][0] * mdlt)
  print()

  print('Zaključak: u pitanju je ista transformacija.')
  print()

  # Slucaj sa vise tacaka
  orig = np.array([[-5,0,1], [-6,0.5,1], [-5,3,1],
                   [-4,2,1], [-2,1.5,1], [-4,0,1]])
  nove = np.array([[3,0,1], [1,1.5,1], [2.7,2.5,1],
                   [6,2,1], [6.5,0.5,1], [4,0,1]])

  print('Originalne tačke:')
  print(orig)
  print()

  print('Njihove slike:')
  print(nove)
  print()

  print('DLT bez šuma:')
  dlt0 = DLT(nove, orig)
  print(dlt0)
  print()

  print('mDLT bez šuma:')
  mdlt0 = mDLT(nove, orig)
  print(mdlt0)
  print()

  print('Skalirana mDLT:')
  print(dlt0[0][0]/mdlt0[0][0] * mdlt0)
  print()

  print('Zaključak: više tačaka unosi višeznačnost.')
  print('Sada se skaliranjem mDLT ne dobija isto kao DLT.')
  print()

  # Slucaj sa sumom
  orig[2], nove[0] = [-5.1,3,1], [3.1,0,1]

  print('Originali sa šumom:')
  print(orig)
  print()

  print('Slike sa šumom:')
  print(nove)
  print()

  print('DLT sa šumom:')
  dlt1 = DLT(nove, orig)
  print(dlt1)
  print()

  print('Skalirana DLT:')
  print(dlt0[0][0]/dlt1[0][0] * dlt1)
  print()

  print('mDLT sa šumom:')
  mdlt1 = mDLT(nove, orig)
  print(mdlt1)
  print()

  print('Skalirana mDLT:')
  print(mdlt0[0][0]/mdlt1[0][0] * mdlt1)
  print()

  print('Zaključak: šum donekle utiče na transformaciju.')

# Poziv test funkcije ukoliko
# je modul direktno izvrsen
if __name__ == '__main__':
  test()
