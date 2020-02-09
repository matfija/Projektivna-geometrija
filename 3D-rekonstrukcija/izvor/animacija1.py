#!/usr/bin/env python3

# Ukljucivanje modula za matematiku
import numpy as np

# Ukljucivanje modula za animaciju
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

# Ukljucivanje 3D rekonstrukcije
from tridrek1 import rekonstruisi

# Enumeracija bafera tipki
PRAZNO = 0      # sve nule
NAPRED = 1      # jedinica
NAZAD = 2       # 1 << 1
GORE = 4        # 1 << 2
DOLE = 8        # 1 << 3
LEVO = 16       # 1 << 4
DESNO = 32      # 1 << 5
RESET = 64      # 1 << 6
tipke = PRAZNO  # prazan

# Klasa za predstavljanje misa
class Mis:
  def __init__(self):
    self.x = 0
    self.y = 0

# Klasa za predstavljanje oka/kamere
class Oko:
  # Konstruktor oka
  def __init__(self, x, y, z, cx, cy, cz):
    # Greska u slucaju zakljucavanja
    if x == cx and y == cy:
      raise ValueError
    
    # Inicalizacija Dekartovih koordinata
    self.x = x
    self.y = y
    self.z = z

    # Inicijalizacija sfernih koordinata
    self.r = np.sqrt((x-cx)**2 + (y-cy)**2 + (z-cz)**2)
    self.phi = np.arctan2(y-cy, x-cx)
    self.theta = np.arcsin((z-cz)/self.r)

    # Cuvanje pocetnih vrednosti
    self.r0 = self.r
    self.phi0 = self.phi
    self.theta0 = self.theta
    
    # Inicijalizacija sfernog pomeraja
    self.d_r = 10
    self.d_phi = np.pi/100
    self.d_theta = np.pi/100

    # Inicijalizacija sfernog minimuma
    self.r_min = 300
    self.phi_min = -np.pi
    self.theta_min = -np.pi/2 + np.pi/20

    # Inicijalizacija sfernog maksimuma
    self.r_max = 2000
    self.phi_max = np.pi
    self.theta_max = np.pi/2 - np.pi/20
    
    # Inicijalizacija centra pogleda
    self.cx = cx
    self.cy = cy
    self.cz = cz

  # Izracunavanje Dekartovih koordinata
  def popravi(self):
    self.x = self.cx + self.r * np.cos(self.theta) * np.cos(self.phi)
    self.y = self.cy + self.r * np.cos(self.theta) * np.sin(self.phi)
    self.z = self.cz + self.r * np.sin(self.theta)

  # Oko se priblizava
  def napred(self):
    # Svako kretanje kamere
    # zaustavlja resetovanje
    global tipke
    tipke &= ~RESET
    
    # Smanjuje se radijus
    self.r -= self.d_r

    # Popravka jer r = [5, 20]
    self.r = max(self.r, self.r_min)

  # Oko se udaljava
  def nazad(self):
    # Svako kretanje kamere
    # zaustavlja resetovanje
    global tipke
    tipke &= ~RESET
    
    # Povecava se radijus
    self.r += self.d_r

    # Popravka jer r = [5, 20]
    self.r = min(self.r, self.r_max)

  # Oko se penje
  def gore(self):
    # Svako kretanje kamere
    # zaustavlja resetovanje
    global tipke
    tipke &= ~RESET
    
    # Povecava se polar
    self.theta += self.d_theta

    # Popravka jer theta = [-pi/2, pi/2]
    self.theta = min(self.theta, self.theta_max)

  # Oko se spusta
  def dole(self):
    # Svako kretanje kamere
    # zaustavlja resetovanje
    global tipke
    tipke &= ~RESET
    
    # Smanjuje se polar
    self.theta -= self.d_theta

    # Popravka jer theta = [-pi/2, pi/2]
    self.theta = max(self.theta, self.theta_min)

  # Oko ide nalevo
  def levo(self):
    # Svako kretanje kamere
    # zaustavlja resetovanje
    global tipke
    tipke &= ~RESET
    
    # Smanjuje se azimut
    self.phi -= self.d_phi
    
    # Popravka jer phi = [-pi, pi)
    if self.phi < self.phi_min:
        self.phi += 2*np.pi

  # Oko ide nadesno
  def desno(self):
    # Svako kretanje kamere
    # zaustavlja resetovanje
    global tipke
    tipke &= ~RESET
    
    # Povecava se azimut
    self.phi += self.d_phi
    
    # Popravka jer phi = [-pi, pi)
    if self.phi >= self.phi_max:
        self.phi -= 2*np.pi

  # Vracanje oka na pocetni polozaj
  def reset(self):
    # Kamera se u sfernom koordinatnom sistemu
    # posmatra kao trojka (r, phi, theta); cilj
    # resetovanja je da tu trojku transformise
    # u (r0, phi0, theta0), gde su nulom indeksirane
    # pocetne vrednosti parametara; ova tranformacija
    # moze biti translacija po vektoru pomeraja
    t_r = self.r0 - self.r
    t_phi = self.phi0 - self.phi
    t_theta = self.theta0 - self.theta
    
    # Duzina prvog vektora
    duzina1 = np.abs(t_r)/10
    kraj1 = True

    # Normalizacija izracunatog vektora
    # deljenjem sa njegovom duzinom
    if duzina1 != 0:
      t_r /= duzina1

      # Translacija po radijusu pogleda,
      # ali samo ako je vrednost pomeraja
      # manja od udaljenosti bitnih tacaka
      if abs(t_r) < abs(self.r0 - self.r):
        self.r += t_r
        kraj1 = False
      else:
        self.r = self.r0

    # Isti slucaj je i sa drugim vektorom
    duzina2 = 50*np.sqrt(t_phi**2 + t_theta**2)
    kraj2 = True
    if duzina2 != 0:
      t_phi /= duzina2
      t_theta /= duzina2
    
      # Slicno kao dosad, samo za azimutalni ugao
      if abs(t_phi) < abs(self.phi0 - self.phi):
        self.phi += t_phi
        kraj2 = False
      else:
        self.phi = self.phi0
      
      # Slicno kao dosad, samo za polarni ugao
      if abs(t_theta) < abs(self.theta0 - self.theta):
        self.theta += t_theta
        kraj2 = False
      else:
        self.theta = self.theta0
    
    # Indikator da li je vracanje zavrseno
    return kraj1 and kraj2

# Globalni identifikator tajmera
TIMER_ID = 0

# Globalno vreme osvezavanja tajmera
TIMER_INTERVAL = 20

# Dimenzije prozora
sirina, visina = 600, 600

# Parametri rekonstrukcije
rek, ivm, ivv = rekonstruisi()
c = np.mean(rek, axis = 0)

# Globalno oko/kamera
oko = Oko(c[0]+1040, c[1]+120, c[2]-75,
             c[0],     c[1],    c[2])

# Objekat misa
mis = Mis()

# Funkcija za obradu dogadjaja misa
def misko(taster, stanje, x, y):
  # Pamti se pozicija pokazivaca
  mis.x = x
  mis.y = y

# Funkcija za obradu prevlacenja misa
def pomeraj(x, y):
  # Promena pozicije pokazivaca
  pom_x = x - mis.x
  pom_y = y - mis.y

  # Pamti se nova pozicija
  mis.x = x
  mis.y = y

  # Ukoliko je pomeraj po x osi pozitivan,
  # mis je prevucen nadesno, sto znaci da
  # se oko pomera nalevo, i suprotno
  if pom_x > 0:
    oko.levo()
  elif pom_x < 0:
    oko.desno()

  # Ukoliko je pomeraj po y osi pozitivan,
  # mis je prevucen nagore, sto znaci da
  # se i oko pomera nagore, i suprotno
  if pom_y > 0:
    oko.gore()
  elif pom_y < 0:
    oko.dole()

# Funkcija koja se poziva na tajmer
def tajmer(*args):
  # Uzimanje tipki
  global tipke

  # Resetovanje pogleda
  if tipke & RESET:
    # Kraj animacije resetovanja
    if oko.reset():
      tipke &= ~RESET
  
  # Oko se priblizava
  if tipke & NAPRED:
    oko.napred()
    
  # Oko se udaljava
  if tipke & NAZAD:
    oko.nazad()

  # Oko se penje
  if tipke & GORE:
    oko.gore()

  # Oko se spusta
  if tipke & DOLE:
    oko.dole()

  # Oko ide nalevo
  if tipke & LEVO:
    oko.levo()

  # Oko ide nadesno
  if tipke & DESNO:
    oko.desno()

  # Forsiranje ponovnog iscrtavanja
  glutPostRedisplay()

  # Ponovno postavljanje tajmera
  glutTimerFunc(TIMER_INTERVAL, tajmer, TIMER_ID)

# Funkcija za obradu otpustanja tipki
def tipkeg(taster, *args):
  global tipke
  if taster in [b'a', b'A']:
    tipke &= ~LEVO
  elif taster in [b'd', b'D']:
    tipke &= ~DESNO
  elif taster in [b'e', b'E']:
    tipke &= ~NAPRED
  elif taster in [b'q', b'Q']:
    tipke &= ~NAZAD
  elif taster in [b's', b'S']:
    tipke &= ~DOLE
  elif taster in [b'w', b'W']:
    tipke &= ~GORE

# Funkcija za obradu dogadjaja tastature
def tipked(taster, *args):
  # Uzimanje tipki
  global tipke

  # Prekid programa u slucaju Esc,
  # sto je 1b u hex sistemu zapisa
  if taster == b'\x1b':
    sys.exit()
  # Obrada tipki za kretanje kamere
  elif taster in [b'a', b'A']:
    tipke |= LEVO
  elif taster in [b'd', b'D']:
    tipke |= DESNO
  elif taster in [b'e', b'E']:
    tipke |= NAPRED
  elif taster in [b'q', b'Q']:
    tipke |= NAZAD
  elif taster in [b's', b'S']:
    tipke |= DOLE
  elif taster in [b'w', b'W']:
    tipke |= GORE
  elif taster in [b'r', b'R']:
    tipke ^= RESET

# Crtanje rekonstruisanog objekta
def objekat():
  # Pocetak iscrtavanja linija
  glBegin(GL_LINES)

  # Plava boja za malu kutiju
  glColor3f(0, 0, 1)

  # Crtanje svake ivice
  for i, j in ivm:
    glVertex3f(*rek[i-1])
    glVertex3f(*rek[j-1])

  # Crvena boja za veliku kutiju
  glColor3f(1, 0, 0)

  # Crtanje svake ivice
  for i, j in ivv:
    glVertex3f(*rek[i-1])
    glVertex3f(*rek[j-1])

  # Kraj iscrtavanja linija
  glEnd()
    
# Funkcija za prikaz scene
def prikaz():
  # Ciscenje prozora: ciscenje bafera boje i dubine;
  # prothodni sadrzaj prozora brise se tako sto se boja
  # svih piksela postavlja na zadatu boju pozadine
  glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

  # Postavljanje matrice transformacije;
  # ucitava se jedinicna matrica koja se
  # kasnije mnozi matricama odgovarajucih
  # geometrijskih transformacija
  glMatrixMode(GL_MODELVIEW)
  glLoadIdentity()

  # Izracunavanje polozaja oka
  oko.popravi()

  # Vidni parametri; scena se tranformise tako
  # da se oko nadje ispred, a objekti na centru
  # scene, cime se simulira sinteticka kamera 
  gluLookAt( oko.x,  oko.y,  oko.z,  # Polozaj oka/kamere
            oko.cx, oko.cy, oko.cz,  # Srediste pogleda
               0,      0,      1   ) # Vektor normale

  # Crtanje rekonstruisanog objekta
  objekat()

  # Zamena iscrtanih bafera
  glutSwapBuffers()

# Glavna (main) fja
def main():
  # Opis: RGB (crvena, zelena, plava) sistem
  # boja, bafer dubine za pravilno postavljanje
  # objekata, dva bafera scene zarad manjeg
  # seckanja prilikom postavljanja nove slike
  glutInitDisplayMode(GLUT_RGB | GLUT_DEPTH | GLUT_DOUBLE)

  # Pravljenje prozora: usput ide
  # postavljanje dimenzija i imena
  glutInitWindowSize(sirina, visina)
  glutCreateWindow(b'3D rekonstrukcija')

  # Postavljanje sive za boju 'ciscenja prozora',
  # koja se ujedno uzima za zadatu boju pozadine
  glClearColor(0.96, 0.96, 0.96, 1)

  # Ukljucivanje umeksavanja linija
  glEnable(GL_LINE_SMOOTH)

  # Postavljanje sirine linije
  glLineWidth(4)

  # Ukljucivanje provere dubine
  glEnable(GL_DEPTH_TEST)

  # Vezivanje funkcija za prikaz,
  # mis, tastaturu i promenu prozora
  glutDisplayFunc(prikaz)
  glutMouseFunc(misko)
  glutMotionFunc(pomeraj)
  glutKeyboardFunc(tipked)
  glutKeyboardUpFunc(tipkeg)
                       # Sprecava se promena dimenzija
  glutReshapeFunc(lambda *args: glutReshapeWindow(sirina, visina))

  # Postavljanje glavnog tajmera
  glutTimerFunc(TIMER_INTERVAL, tajmer, TIMER_ID)

  # Postavljanje matrice projekcije
  glMatrixMode(GL_PROJECTION)
  gluPerspective(40,            # Ugao perspektive
                 sirina/visina, # Odnos dimenzija prozora
                 1,             # Prednja ravan odsecanja
                 3000)          # Zadnja ravan odsecanja

  # Glavna petlja animacije
  glutMainLoop()

# Obavestenje o gresci ukoliko je modul
# pokrenut kao samostalan program
if __name__ == '__main__':
  sys.exit('Animacija nije samostalan program! Pokrenite main!')
