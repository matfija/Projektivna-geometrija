#!/usr/bin/env python3

# Modul je znacajno unapredjenje i prosirenje
# istoimenog modula napisanog za prvi domaci

# Globalna promenljiva za logovanje
LOGUJ = True

# Ukljucivanje sistemskog modula
from sys import exit as greska

# Ukljucivanje modula za matematiku
import numpy as np
import numpy.linalg as LA
from math import sqrt, log, ceil
from random import sample

# Ukljucivanje modula za slike
from cv2 import imread, remap, BFMatcher, \
              INTER_AREA, BORDER_TRANSPARENT
from cv2.xfeatures2d import SIFT_create

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

# RANSAC algoritam: p je zeljena verovatnoca da barem jedan
# uzorak bude bez autlajera, eps je pretpostavljena verovatnoca
# da je par autlajer u najgorem slucaju, s je velicina uzorka
# (fiksno 4 u slucaju odredjivanja projekcije), N je broj uzoraka
# (izvedeno iz verovatnoca), t je tolerancija (ovde empirijski
# odabrana, posto greske nisu nuzno normalno raspodeljene)
def RANSAC(nove, orig, p = 0.99, eps = 0.5, s = 4, N = 72, t = 3):
  # Prekid algoritma u slucaju neadekvatne
  # velicine uzorka, koja mora biti cetiri
  if s != 4:
    raise ValueError

  # Izvedeno iz verovatnoce; postoji i iterativno izracunavanje
  # potrebnog broja uzoraka i udela autlajera u skupu zasnovano
  # na konzervativnoj pretpostavci da su svi prosledjeni parovi
  # autlajeri, ali ono je dalo veoma lose rezultate na test
  # primerima, pa je izbegnuto zarad kvalitetnijih panorama
  N = ceil(log(1-p)/log(1-(1-eps)**s))

  # Log poruka o akciji
  if LOGUJ:
    print(f'RANSAC: iteracija {N}, tačaka {len(nove)}.')

  # Homogene koordinate od prosledjenih afinih
  nove = np.array([*map(lambda x: [x[0], x[1], 1], nove)])
  orig = np.array([*map(lambda x: [x[0], x[1], 1], orig)])

  # Skup inlajera, prazan i sa nultnom greskom
  inlajeri = [[], 0]

  # Glavna petlja algoritma
  for _ in range(N):
    # Odabir s parova
    indeksi = sample(range(len(nove)), s)

    # Racunanje tacne transformacije
    try:
      M = naivni(nove[indeksi], orig[indeksi])
    # Zanemarivanje singularne transformacije
    except:
      continue

    # Pravljenje skupa inlajera; prosirenje RANSAC-a
    # tako da, u neresenom slucaju, presudi ukupna greska
    inl = [[], 0]
    for i in range(len(nove)):
      stara = np.array([orig[i][0], orig[i][1], 1])
      nova = np.array([nove[i][0], nove[i][1], 1])
      
      rez = M @ stara
      # Zanemarivanje beskonacno udaljenih tacaka
      if rez[2] == 0:
        inl = [[], 0]
        break
      rez = np.array([round(rez[0]/rez[2]), round(rez[1]/rez[2]), 1])

      # Inlajer je ako je rezultat dobijene projekcije (rez)
      # dovoljno blizu odgovarajucoj slici (nova)
      greska = LA.norm(nova-rez)
      if greska < t:
        inl[0].append(i)
      inl[1] += greska

    # Cuvanje najveceg skupa inlajera ili onog sa
    # manjom greskom u slucaju iste kardinalnosti
    if len(inl[0]) > len(inlajeri[0]) or \
       len(inl[0]) == len(inlajeri[0]) and \
            inl[1] < inlajeri[1]:
      inlajeri = inl

      # Log poruka o akciji
      if LOGUJ:
        print(f'RANSAC: inlajera {len(inl[0])}, greška {inl[1]:.2f}.')

  # Neophodna su barem cetiri para za
  # potrebe odredjivanja projekcije
  if len(inlajeri[0]) < 4:
    raise ValueError

  # Vracanje transformacije izracunate
  # pomocu svih odredjenih inlajera
  return mDLT(nove[inlajeri[0]], orig[inlajeri[0]])

# Isecanje praznih ivica
def iseci(slika):
  # Log poruka o akciji
  if LOGUJ:
    print('Iseca se slika.')
  
  # Za svaki piksel se odredi broj nenula,
  # cime se zapravo izdvajaju crni nula pikseli
  nenule = (slika != 0).sum(axis=2)

  # Nizovi indeksa sa nenula vrednostima
  red = np.flatnonzero(nenule.sum(axis=1))
  kol = np.flatnonzero(nenule.sum(axis=0))

  # Log poruka o akciji
  if LOGUJ:
    print('Uspešno isečena slika.')
    print()

  # Rezultat je pravougaonik izmedju
  # minumima i maksimuma nenula indeksa
  return slika[red.min():red.max(),
               kol.min():kol.max()]

# Primena projektivne transformacije;
# poput warpPerspective iz OpenCV-ja;
# brze je od PIL-a sa prvog domaceg
def projektuj(stara, M, dim, gran = None):
  # Inverzija matrice, kako bi se svaki piksel nove
  # slike odredjivao preko stare umesto obrnuto; ovime
  # se izbegavaju nepopunjeni pikseli u koje se nista
  # ne bi preslikalo sa originala da je direktno radjeno
  M = LA.inv(M)

  # Inicijalizacija prazne (skroz crne) slike; veoma
  # je vazno da tip bude uint8 (neoznacen ceo broj duzine
  # osam bita tj. jedan bajt), jer inace OpenCV ne prepoznaje
  # numpy matricu kao sliku; otprilike mi je ceo sat otisao
  # na debagovanje zasto fja nije radila pre eksplicitnog
  # navodjenja tipa; obratiti paznju i na indeksiranje u
  # OpenCV-ju: redovi su osa 1, a kolone 0
  nova = np.zeros((dim[1], dim[0], stara.shape[2]), dtype = np.uint8)

  # Odredjivanje granice ako nije zadata;
  # lenjo se uzimaju svi novi pikseli
  if gran is None:
    gran = (0, 0), (dim[1], dim[0])

  # Transformacija piksel po piksel;
  # obratiti paznju na obrnute indekse
  for j in range(gran[0][1], gran[1][1]):
    for i in range(gran[0][0], gran[1][0]):
      # Direktan racun umesto mnozenja matrica;
      # ovo u neku ruku ubrzava izvrsavanje
      imen = M[2,0]*j + M[2,1]*i + M[2,2]
      jj = int(round((M[0,0]*j + M[0,1]*i + M[0,2]) / imen))
      ii = int(round((M[1,0]*j + M[1,1]*i + M[1,2]) / imen))

      # Preskakanje 'praznih' piksela; ne zanima nas
      # potreban original koji se nalazi izvan slike
      if ii < 0 or ii >= stara.shape[0] or \
         jj < 0 or jj >= stara.shape[1]:
        continue

      # Prepisivanje piksela iz originala
      nova[i, j] = stara[ii, jj]

  return nova

# Spajanje dve slike
def spoj(leva, desna, sleva = False, nove = None, orig = None):
  # Ukoliko nisu prosledjene tacke, moraju se naci
  if nove is None or orig is None \
     or not nove or not orig \
     or len(nove) != len(orig) \
     or len(nove) < 4:
    # Log poruka o akciji
    if LOGUJ:
      print()
      print('Traže se korespondencije.')
    
    # Upotreba SIFT (scale-invariant feature transform)
    # algoritma za pronalazak zanimljivih tacaka na slikama
    sift = SIFT_create()
    kpl, desl = sift.detectAndCompute(leva, None)
    kpd, desd = sift.detectAndCompute(desna, None)

    # Uparivanje dobijenih deskriptora
    # brute-force metodom najblizih suseda
    parovi = BFMatcher().knnMatch(desd, desl, k=2)

    # Filtriranje parova izuzimanjem onih previse
    # dalekih; ovo nije neophodno, ali olaksava
    # posao RANSAC-u i znatno ga ubrzava
    bliski = [m for m, n in parovi if m.distance < 0.5 * n.distance]

    # Neophodna su barem cetiri para za
    # potrebe odredjivanja projekcije
    if len(bliski) < 4:
      raise ValueError

    # Izdvajanje originala (sa desne slike)
    # i slika (sa leve slike) za projekciju
    orig = np.float32([kpd[m.queryIdx].pt
                       for m in bliski]).reshape(-1,2)
    nove = np.float32([kpl[m.trainIdx].pt
                       for m in bliski]).reshape(-1,2)

    # Log poruka o akciji
    if LOGUJ:
      print('Uspešno odabrane korespondencije.')
  elif LOGUJ:
    print()

  # Log poruka o akciji
  if LOGUJ:
    print('Određuje se transformacija.')

  # Izracunavanje matrice projekcije
  M = RANSAC(nove, orig)
  if sleva:
    M = LA.inv(M)

  # Log poruka o akciji
  if LOGUJ:
    print('Uspešno određena transformacija.')

  # Dimenzije ulaznih slika
  dim1 = leva.shape[1], leva.shape[0]
  dim2 = desna.shape[1], desna.shape[0]

  if sleva:
    dim1, dim2 = dim2, dim1

  # Pronalazak tacaka van slike
  cosk = np.array([[    0,          0,      1],
                   [dim2[0]-1,      0,      1],
                   [    0,      dim2[1]-1,  1],
                   [dim2[0]-1,  dim2[1]-1,  1]])
  cosk = np.array([*map(lambda x: M@x, cosk)])
  cosk = np.array([*map(lambda x: [x[0]/x[2], x[1]/x[2], 1], cosk)])
  mini = cosk[:, 0].min(), cosk[:, 1].min()
  mini = [*map(lambda x: abs(ceil(min(x, 0))), mini)]

  # Nova matrica, sa dodatkom translacije koja
  # dosad nevidljive elemente smesta na sliku
  M = np.array([[1,   0,  mini[0]],
                [0,   1,  mini[1]],
                [0,   0,     1  ]]) @ M

  # Dimenzije slike koja nije fiksirana
  cosk = np.array([*map(lambda x: [x[0]+mini[0], x[1]+mini[1], 1], cosk)])
  dim = (ceil(max(cosk[:, 0].max()+1, dim1[0]+mini[0])),
         ceil(max(cosk[:, 1].max()+1, dim1[1]+mini[1])))

  # Obuhvatajuci pravougaonik (bounding box)
  # slike koja nije fiksna zarad ustede vremena;
  # ukoliko su dimenzije nove slike dosta vece
  # od polazne, nema potrebe gledati crne piksele
  minx = int(ceil(cosk[:, 0].min()))
  maxx = int(ceil(cosk[:, 0].max()))+1
  miny = int(ceil(cosk[:, 1].min()))
  maxy = int(ceil(cosk[:, 1].max()))+1
  gran = (miny, minx), (maxy, maxx)
  
  # Cuvanje fiksirane i slike koju treba
  # transformisati pod informativnijim imenima
  fiksna = leva
  transf = desna

  if sleva:
    fiksna, transf = transf, fiksna

  # Log poruka o akciji
  if LOGUJ:
    print(f'Transformiše se {"leva" if sleva else "desna"} slika.')

  # Transformacija slike koja nije fiksirana
  transf = projektuj(transf, M, dim, gran)

  # Log poruka o akciji
  if LOGUJ:
    print('Uspešno izvršena transformacija.')

  # Log poruka o akciji
  if LOGUJ:
    print('Spajaju se slike.')

  # Uzduzne granice preklapanja
  if sleva:
    lgran = mini[0]
    dgran = maxx
  else:
    lgran = minx
    dgran = dim1[0]+mini[0]

  # Postavljanje fiksne slike na mesto;
  # prvo obrada delova pre i posle granice
  if sleva:
    transf[mini[1]:dim1[1]+mini[1],
            dgran :dim1[0]+mini[0]] = \
                 [[fiksna[i-mini[1],j-mini[0]]
           for j in range( dgran , dim1[0]+mini[0])]
           for i in range(mini[1], dim1[1]+mini[1])]
  else:
    transf[mini[1]:dim1[1]+mini[1],
           mini[0]:     lgran     ] = \
                 [[fiksna[i-mini[1],j-mini[0]]
           for j in range(mini[0],      lgran     )]
           for i in range(mini[1], dim1[1]+mini[1])]

  
  # Funkcija za filtriranje crnih piskela
  crn = lambda p: all(map(lambda x: x == 0, p))

  # Funkcija za interpolaciju piksela
  duzina = dgran - lgran + 1
  if sleva:
    pros = lambda y, x, j: (dgran-j)/duzina*x + (j-lgran+1)/duzina*y
  else:
    pros = lambda x, y, j: (dgran-j)/duzina*x + (j-lgran+1)/duzina*y

  # Tezinsko uprosecavanje (interpolacija)
  # necrnih piksela unutar granicnog pojasa
  transf[mini[1]:dim1[1]+mini[1],
          lgran :     dgran     ] = [[transf[i,j]
            if crn(fiksna[i-mini[1],j-mini[0]])
    else fiksna[i-mini[1],j-mini[0]] if crn(transf[i,j])
   else pros(fiksna[i-mini[1],j-mini[0]], transf[i,j], j)
         for j in range( lgran ,      dgran     )]
         for i in range(mini[1], dim1[1]+mini[1])]

  # Log poruka o akciji
  if LOGUJ:
    print('Uspešno spojene slike.')

  # Isecanje praznih ivica
  return iseci(transf)

# Reprojekcija slike na valjak, sto ublazava iskrivljenje;
# prerada koda sa http://www.morethantechnical.com/2018/10/30/
# cylindrical-image-warping-for-panorama-stitching/
def cilindrizuj(slika, par = 650):
  # Dimenzije ulazne slike
  vis, sir = slika.shape[:2]

  # Pretpostavljena matrica kamere
  K = np.array([[par,   0,   sir/2],
                [ 0,   par,  vis/2],
                [ 0,    0,     1  ]])
    
  # Koordinate piksela
  y, x = np.indices((vis, sir))
  X = np.stack([x, y , np.ones_like(x)], axis = -1).reshape(vis*sir, 3)
  
  # Normalizacija koordinata
  Kinv = LA.inv(K) 
  X = (Kinv @ X.T).T
  
  # Cilindricne koordinate
  # (sin\theta, h, cos\theta)
  A = np.stack([np.sin(X[:, 0]),
                    X[:, 1],
                np.cos(X[:, 0])],
               axis = -1).reshape(sir*vis,3)
    
  # Vracanje u ravan slike
  B = (K @ A.T).T
  B = B[:, :-1] / B[:, [-1]]
  
  # Izuzimanje tacaka van slike
  B[(B[:, 0] < 0) | (B[:, 0] >= sir) | \
    (B[:, 1] < 0) | (B[:, 1] >= vis)] = -1
  B = B.reshape(vis, sir, -1)

  # Transformacija prema cilindricnim koordinatama
  return remap(slika, B[:, :, 0].astype(np.float32),
                      B[:, :, 1].astype(np.float32),
             INTER_AREA, borderMode = BORDER_TRANSPARENT)

# Racunanje panorame
def panorama(slike, srednja = None, valjak = False):
  # Eventualno remapiranje na valjak
  if valjak:
    # Log poruka o akciji
    if LOGUJ:
      print('Cilindrizuju se slike.')
    
    slike = [*map(cilindrizuj, slike)]

    # Log poruka o akciji
    if LOGUJ:
      print('Uspešno cilindrizovane slike.')
  
  # Polazi se od krajnje slike
  slika = slike.pop()
  n = len(slike)

  # Odredjivanje srednje ako nije prosledjena
  if srednja is None:
    srednja = n//2

  # Zdesna se spaja desna polovina panorame
  for i in range(srednja, n):
    slika = spoj(slike.pop(), slika, False)

  # Sleva se spaja leva polovina panorame
  for i in range(srednja):
    slika = spoj(slike.pop(), slika, True)

  return slika

# Obavestenje o gresci ukoliko je modul
# pokrenut kao samostalan program
if __name__ == '__main__':
  greska('Proj nije samostalan program! Pokrenite main!')
