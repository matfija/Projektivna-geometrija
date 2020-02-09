#!/usr/bin/env python3

# Ukljucivanje modula za matematiku
import numpy as np
import numpy.linalg as LA

# Ukljucivanje modula za upozorenja
import warnings

# NAPOMENA: svi razmatrani uglovi zadati su u radijanima,
# sto je u skladu sa uobicajenom informatickom praksom

# Matrica rotacije koja odgovara sopstvenim rotacijama
# za ugao phi oko x-ose, theta oko y-ose, psi oko z-ose
# odnosno obrnuto iz tacke gledista polaznog repera
def Euler2A(phi, theta, psi):
  # Greska ako nisu brojevi
  if not isinstance(phi, (int, float)) or\
     not isinstance(theta, (int, float)) or\
     not isinstance(psi, (int, float)):
    raise ValueError
  
  # Rotacija za ugao phi oko x-ose
  Rx = np.array([[     1,             0,               0      ],
                 [     0,         np.cos(phi),    -np.sin(phi)],
                 [     0,         np.sin(phi),     np.cos(phi)]])

  # Rotacija za ugao theta oko y-ose
  Ry = np.array([[ np.cos(theta),     0,         np.sin(theta)],
                 [     0,             1,              0       ],
                 [-np.sin(theta),     0,         np.cos(theta)]])

  # Rotacija za ugao psi oko z-ose
  Rz = np.array([[np.cos(psi),   -np.sin(psi),        0       ],
                 [np.sin(psi),    np.cos(psi),        0       ],
                 [     0,             0,              1       ]])

  # Kompozicija u suprotnom redosledu,
  # prema odgovarajucoj teoremi
  return Rz @ Ry @ Rx

# Jedinicni vektor i ugao takvi da ulazna matrica
# rotacije odgovara rotaciji oko rezultujuceg vektora
# za rezultujuci ugao, ogranicen izmedju 0 i pi
def AxisAngle(A):
  # Greska ako matrica nije ortogonalna
  # ili joj determinantna nije jedan
  if not np.allclose(A @ A.T, np.eye(3))\
     or not np.isclose(LA.det(A), 1):
    raise ValueError

  # Racunanje sopstvenih vrednosti i vektora
  w, v = LA.eig(A)

  # Izvlacenje indeksa sopstvene vrednosti 1
  ind = np.argwhere(np.isclose(w, 1))[0,0]

  # Izvlacenje odgovarajuceg sopstvenog vektora; on
  # je zapravo trazena osa rotacije; usput privremeno
  # iskljucivanje upozorenja o odbacivanju imaginarnog
  # dela kompleksnog broja posto je on garantovano nula
  # u ovom slucaju; zarad ocuvanja preciznosti neophodna
  # je upotreba realnih brojeva sa dvostrukom tacnoscu
  warnings.filterwarnings('ignore')
  p = np.array(v[:, ind], dtype = np.float64)
  warnings.resetwarnings()

  # Proizvoljan jedinicni vektor normalan na prethodni;
  # pazi se na slucaj(eve) kada su neke koordinate nule
  # p ~ [0, y, z] && (y!=0 || z!=0)
  if np.isclose(p[0], 0):
    u = np.array([0, -p[2], p[1]])
  # p ~ [x, y, z] && x!=0
  else:
    u = np.array([-p[1], p[0], 0])
  u = u/LA.norm(u)

  # Zarotirani vektor i odredjivanje ugla
  up = A @ u
  phi = np.arccos(u @ up)

  # Eventualna promena znaka ose, kako bi rotacija uvek
  # bila u pozitivnom smeru, prema pravilu desne ruke
  if LA.det(np.array([u, up, p])) < 0:
    p = -p

  # Vracanje odredjene ose i ugla
  return p, phi

# Matrica rotacije oko orijentisane ose
# tj. vektora sa ulaza za ugao sa ulaza
def Rodrigez(p, phi):
  # Greska ako nije broj
  if not isinstance(phi, (int, float)):
    raise ValueError
  
  # Greska ako je nula-vektor
  n = LA.norm(p)
  if np.isclose(n, 0):
    raise ValueError
  
  # Normalizacija ulaznog vektora
  p = p/n

  # Matrica ose rotacije
  ppt = p.reshape(3, 1) @ p.reshape(1, 3)
  
  # Matrica vektorskog mnozenja
  px = np.array([[  0,  -p[2], p[1]],
                 [ p[2],  0,  -p[0]],
                 [-p[1], p[0],  0  ]])

  # Vracanje matrice prema formuli Rodrigeza
  return ppt + np.cos(phi)*(np.eye(3)-ppt) + np.sin(phi)*px

# Ojlerovi uglovi koji odgovaraju
# ulaznoj matrici rotacije
def A2Euler(A):
  # Greska ako matrica nije ortogonalna
  # ili nije sa determinantnom jedan
  if not np.allclose(A @ A.T, np.eye(3))\
     or not np.isclose(LA.det(A), 1):
    raise ValueError

  # 'Zakljucani ziroskop', pa ima beskonacno
  # mnogo resenja; bira se ono sa phi = 0
  if np.isclose(np.abs(A[2,0]), 1):
    phi = 0.
    theta = -np.sign(A[2,0]) * np.pi/2
    psi = np.arctan2(-A[0,1], A[1,1])
  # Jedinstveno resenje
  else:
    phi = np.arctan2(A[2,1], A[2,2])
    theta = np.arcsin(-A[2,0])
    psi = np.arctan2(A[1,0], A[0,0])

  # Vracanje izracunatih uglova
  return phi, theta, psi

# Jedinicni kvaternion koji predstavlja
# rotaciju oko ulazne ose za ulazni ugao
def AxisAngle2Q(p, phi):
  # Greska ako nije broj
  if not isinstance(phi, (int, float)):
    raise ValueError
  
  # Realni deo kvaterniona
  w = np.cos(phi/2)

  # Greska ako je nula-vektor
  n = LA.norm(p)
  if np.isclose(n, 0):
    raise ValueError

  # Normalizacija ose
  p = p/n

  # Imaginarni deo kvaterniona
  x, y, z = np.sin(phi/2) * p

  # Vracanje izracunatog kvaterniona
  return np.array([w, x, y, z])

# Jedinicni vektor i ugao takvi da ulazni
# kvaternion odgovara rotaciji oko rezultujuce ose
# za rezultujuci ugao, ogranicen izmedju 0 i pi
def Q2AxisAngle(q):
  # Greska ako je nula-kvaternion
  n = LA.norm(q)
  if np.isclose(n, 0):
    raise ValueError
  
  # Normalizacija kvaterniona
  q = q/n

  # Eventualna negacija kvaterniona kako bi
  # rezultujuci ugao bio u zeljenom rasponu
  if q[0] < 0: q = -q

  # Izvlacenje svih koeficijenata
  w, x, y, z = q

  # Nulta rotacija u slucaju identiteta
  if np.isclose(w, 1):
    return np.array([1., 0., 0.]), 0.

  # Ugao rotacije
  phi = 2 * np.arccos(w)

  # Osa rotacije
  p = np.array([x, y, z])
  p = p/LA.norm(p)

  # Vracanje odredjene ose i ugla
  return p, phi

# Linearna interpolacija polozaja
# izmedju c1 i c2 za vreme [0, tu]
def linear(c1, c2, tu, t):
  # Greska ako su losi ulazni podaci
  if not isinstance(tu, (int, float)) or \
     not isinstance(t, (int, float)) or \
     not 0 <= t <= tu:
    raise ValueError

  # Vracanje interpoliranog polozaja
  return (1 - t/tu) * c1 + t/tu * c2

# Jedinicni kvaternion koji predstavlja linearnu
# interpolaciju (Lerp) izmedju ulaznih q1 i q2
# u trenutku t iz diskretnog intervala [0, tu]
def Lerp(q1, q2, tu, t):
  # Greska ako su losi ulazni podaci
  if len(q1) != 4 or len(q2) != 4 or \
     not isinstance(tu, (int, float)) or \
     not isinstance(t, (int, float)) or \
     not 0 <= t <= tu:
    raise ValueError
  
  # Greska ako su nula-kvaternioni
  n1 = LA.norm(q1)
  n2 = LA.norm(q2)
  if np.isclose(n1, 0) or np.isclose(n2, 0):
    raise ValueError
  
  # Normalizacija kvaterniona
  q1 = q1/n1
  q2 = q2/n2

  # Interpolirani kvaternion
  q = linear(q1, q2, tu, t)

  # Normalizacija interpoliranog
  n = LA.norm(q)
  q = q/n

  # Vracanje interpoliranog kvaterniona
  return q

# Jedinicni kvaternion koji predstavlja sfernu
# lin. interp. (SLerp) izmedju ulaznih q1 i q2
# u trenutku t iz diskretnog intervala [0, tu]
def SLerp(q1, q2, tu, t):
  # Greska ako su losi ulazni podaci
  if len(q1) != 4 or len(q2) != 4 or \
     not isinstance(tu, (int, float)) or \
     not isinstance(t, (int, float)) or \
     not 0 <= t <= tu:
    raise ValueError
  
  # Greska ako su nula-kvaternioni
  n1 = LA.norm(q1)
  n2 = LA.norm(q2)
  if np.isclose(n1, 0) or np.isclose(n2, 0):
    raise ValueError
  
  # Normalizacija kvaterniona
  q1 = q1/n1
  q2 = q2/n2

  # Kosinus ugla izmedju kvaterniona
  cos = np.inner(q1, q2)

  # Obrtanje u cilju kretanja po kracem
  # luku sfere po kojoj je interpolacija
  if cos < 0:
    q1 = -q1
    cos = -cos

  # Lerp u slucaju prebliskih kvaterniona
  if cos > 0.95:
    return Lerp(q1, q2, tu, t)

  # Ugao izmedju kvaterniona
  phi = np.arccos(cos)

  # Vracanje interpoliranog kvaterniona
  # koji je ovde garantovano jedinicni
  return np.sin(phi * (1 - t/tu)) / np.sin(phi) * q1 \
           + np.sin(phi * t/tu) / np.sin(phi) * q2

# Pomocna fja za pretvaranje Ojlerovih
# uglova u kvaternion tog polozaja
def Euler2Q(phi, theta, psi):
  return AxisAngle2Q(*AxisAngle(Euler2A(phi, theta, psi)))

# Pomocna fja za pretvaranje kvaterniona
# u Ojlerove uglove tog polozaja
def Q2Euler(q):
  return A2Euler(Rodrigez(*Q2AxisAngle(q)))

# Fja za testiranje
def test():
  # Profesorov test primer
  #phi = -np.arctan(1/4)
  #theta = -np.arcsin(8/9)
  #psi =  np.arctan(4)

  # Moj test primer
  phi = np.pi/3
  theta = np.pi/3
  psi = np.pi/3

  # Ojlerovi uglovi
  print('Ojlerovi uglovi:')
  print('\u03D5 =', phi)
  print('\u03B8 =', theta)
  print('\u03C8 =', psi)
  print()

  # Matrica rotacije
  print('Euler2A:')
  A = Euler2A(phi, theta, psi)
  print('A =')
  print(A)
  print()

  # Osa i ugao
  print('AxisAngle:')
  p, phi0 = AxisAngle(A)
  print('p =', p)
  print('\u03D5 =', phi0)
  print()

  # Vracanje na matricu
  print('Rodrigez:')
  A = Rodrigez(p, phi0)
  print('A =')
  print(A)
  print()

  # Vracanje na uglove
  print('A2Euler:')
  phi, theta, psi = A2Euler(A)
  print('\u03D5 =', phi)
  print('\u03B8 =', theta)
  print('\u03C8 =', psi)
  print()

  # Kvaternion
  print('AxisAngle2Q:')
  q = AxisAngle2Q(p, phi0)
  w, x, y, z = q
  print(f'q = {w:f} {x:+f}i {y:+f}j {z:+f}k')
  print()

  # Vracanje na osu i ugao
  print('Q2AxisAngle:')
  p, phi0 = Q2AxisAngle(q)
  print('p =', p)
  print('\u03D5 =', phi0)

# Poziv test funkcije ukoliko
# je modul direktno izvrsen
if __name__ == '__main__':
  test()
