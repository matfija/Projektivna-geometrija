#!/usr/bin/env python3

# Ukljucivanje sistemskog modula
from sys import exit as greska

# Ukljucivanje grafickog modula
from tkinter import Tk, Frame, Menu, LabelFrame, \
                       Canvas, Button, Entry

# Ukljucivanje pomocnog modula za
# kutijice sa iskacucim porukama
from tkinter.messagebox import showinfo, showerror, askyesno

# Ukljucivanje pomocnog modula
# za pretragu fajl sistema
from tkinter.filedialog import askopenfilename, asksaveasfilename

# Ukljucivanje modula za slike
from PIL import Image, ImageTk

# Ukljucivanje modula za matematiku
import numpy as np
import numpy.linalg as LA
from proj import naivni

# Ukljucivanje modula za kopiranje
from copy import deepcopy

# Ukljucivanje modula za niti
from threading import Thread

# Ukljucivanje modula za konveksni omotac
from omot import konveksni_omot as konv

# Nosilac programa je klasa PPGR, koja nasledjuje
# graficku klasu Tk iz modula tkinter
class PPGR(Tk):
  # Konstruktor aplikacije
  def __init__(self):
    # Log poruka o pokretanju aplikacije
    print('Dobro došli u aplikaciju PPGR!')
    
    # Pozivanje konstruktora roditeljske klase
    super().__init__()

    # Postavljanje naziva aplikacije
    self.title('Отклањање дисторзије')

    # Onemogucavanje promene velicine prozora,
    # posto je Tk prilicno plastican, pa promene
    # ugrozavaju zamisljeni izgled aplikacije
    self.resizable(False, False)

    # Inicijalizacija glavnog menija
    self.init_meni()

    # Ukljucivanje prvog frejma
    self.frejm = None
    self.postavi_frejm(Ucitavanje)
  
  # Postavljanje novog frejma
  def postavi_frejm(self, frejm):
    if self.frejm is not None:
      self.frejm.destroy()

    self.frejm = frejm(self)
    self.frejm.pack()
  
  # Inicijalizacija glavnog menija
  def init_meni(self):
    # Pravljenje glavnog menija
    self.meni = Menu(self)
    
    # Postavljanje glavnog menija i vezivanje
    # komandi za odgovarajuce funkcionalnosti
    self.meni.add_command(label = 'Помоћ (H)', command = self.pomoc)
    self.meni.add_command(label = 'Инфо (G)', command = self.info)
    self.config(menu = self.meni)
    
    # Vezivanje tipki za akcije analogne
    # onima iz prethodno postavljenog menija
    self.bind('<H>', self.pomoc)
    self.bind('<h>', self.pomoc)
    self.bind('<G>', self.info)
    self.bind('<g>', self.info)
    self.bind('<Escape>', self.kraj)
    
    # Vezivanje protokola zatvaranja prozora
    # za istu akciju kao za taster Escape
    self.protocol('WM_DELETE_WINDOW', self.kraj)
  
  # Prikazivanje prozora za pomoc
  def pomoc(self, dog = None):
    showinfo('Помоћ',
             'На почетном прозору налазе се мени и поље за одабир'
             ' слике. Одабиром слике са датотечног система појављује'
             ' се нов прозор са учитаном сликом. Левим кликом миша'
             ' означите четири тачке које желите да постану правоугаоник.'
             ' По потреби, означите још четири тачке и тиме сугеришите'
             ' апликацији где правоугаоник треба да се налази. У случају'
             ' грешке, можете поновити унос десним кликом миша. Апликацију'
             ' рестартујете на исти начин. Резултујућу слику можете'
             ' сачувати на рачунару.')
  
  # Prikazivanje glavnih informacija o aplikaciji
  def info(self, dog = None):
    showinfo('Информације',
             'Домаћи из Примене пројективне геометрије у рачунарству:'
             ' отклањање пројективне дисторзије.\n\n'
             'Лазар Васовић, 99/2016\n'
             'Математички факултет, 2019')
  
  # Zatvaranje aplikacije na zahtev korisnika
  def kraj(self, dog = None):
    # Poruka korisniku o kraju programa
    if askyesno('Kрај програма',
       'Да ли стварно желите да напустите програм?'):
      
      # Log poruka o zatvaranju aplikacije
      print('PPGR zatvoren na zahtev korisnika!')
      
      # Upotreba self.quit() zamrzava prozor na Windows-u,
      # posto prekida izvrsavanje i pokretackog programa
      self.destroy()

# Prvi frejm, za ucitavanje slike
class Ucitavanje(Frame):
  # Konstruktor frejma
  def __init__(self, koren):
    # Log poruka o pokretanju frejma
    print('Odaberite sliku za transformaciju.')
    
    # Pozivanje konstruktora roditeljske klase
    super().__init__(koren)
    
    # Inicijalizacija elemenata GKI
    self.init_gki()
  
  # Inicijalizacija elemenata GKI
  def init_gki(self):
    # Postavljanje velicine i pozicije prozora
    self.master.geometry('320x100+400+300')
    
    # Okvir za odabir
    okvir = LabelFrame(self, text = 'Одаберите слику:',
                       padx = 5, pady = 5)
    okvir.grid(column = 0, row = 0,
               padx = 15, pady = 10)
    
    # Polje za unos slike
    self.unos = Entry(okvir)
    self.unos.grid(column = 1, row = 0,
		   padx = 10, pady = 10)
    self.unos.insert(0, 'primer.bmp')
    self.unos.config(state = 'readonly')
    
    # Dugme za ucitavanje
    ucitaj = Button(okvir,
                    text = 'Учитај',
                    command = self.ucitaj)
    ucitaj.grid(column = 2, row = 0,
		    padx = 5, pady = 5)
    
    # Dugme za pretragu
    pretrazi = Button(okvir,
		      text = 'Претражи',
		      command = self.pretrazi)
    pretrazi.grid(column = 3, row = 0,
		  padx = 5, pady = 5)
  
  # Ucitavanje slike
  def ucitaj(self, dog = None):
    if not hasattr(self.master, 'fajl') \
       or self.master.fajl is None:
      showerror('Грешка',
                'Нисте одабрали датотеку за читање.')
      return

    # Otvaranje odabrane slike
    try:
      self.master.slika = Image.open(self.master.fajl)
    except:
      showerror('Грешка',
                'Одабрана датотека није слика.')
      return
    
    # Kopiranje originalne slike
    self.master.orig = self.master.slika
    self.master.dim = self.master.slika.size

    # Eventualno vertikalno skracivanje
    dim = self.master.slika.size
    
    if dim[1] > 600:
      self.master.slika = \
      self.master.slika.resize((round(dim[0]*600/dim[1]), 600),
                               Image.ANTIALIAS)

    # Eventualno horizotalno skracivanje
    dim = self.master.slika.size

    if dim[0] > 900:
      self.master.slika = \
      self.master.slika.resize((900, round(dim[1]*900/dim[0])),
                               Image.ANTIALIAS)

    # Dimenzije prikaza
    self.master.ndim = self.master.slika.size

    # Prelazak na naredni frejm
    self.master.postavi_frejm(Transformacija)
  
  # Pretraga slika
  def pretrazi(self, dog = None):
    fajl = askopenfilename(
           filetypes = [('Svi tipovi', '*.*')]
           )
    
    # Prikaz odabranog fajla
    if fajl:
      self.unos.config(state = 'normal')
      self.unos.delete(0, 'end')
      self.unos.insert(0, fajl[fajl.rfind('/')+1:])
      self.unos.config(state = 'readonly')
      self.master.fajl = fajl

# Drugi frejm, za transformaciju slike
class Transformacija(Frame):
  # Konstruktor frejma
  def __init__(self, koren):
    # Log poruka o pokretanju frejma
    print('Transformišite odabranu sliku.')
    
    # Pozivanje konstruktora roditeljske klase
    super().__init__(koren)

    # Inicijalizacija odabranih tacaka
    self.tacke = []
    self.ntacke = []

    # Inicijalizacija iscrtavanja
    self.figura = None
    self.id_tac = []
    self.id_tex = []
    self.nfigura = None
    self.nid_tac = []
    self.nid_tex = []

    # Inicijalizacija elemenata GKI
    self.init_gki()
  
  # Inicijalizacija elemenata GKI
  def init_gki(self):
    # Dimenzije odabrane slike
    dim = self.master.slika.size
    
    # Postavljanje velicine i pozicije prozora
    self.master.geometry(f'{max(dim[0]+5, 300)}x{dim[1]+5}+100+50')
    
    # Postavljanje odabrane slike na prozor
    self.slika = ImageTk.PhotoImage(self.master.slika)
    self.platno = Canvas(self, width = dim[0]+5, height = dim[1]+5)
    self.platno.create_image(dim[0]/2+2, dim[1]/2+2, image = self.slika)
    self.platno.pack()

    # Dodavanje transformacije u meni
    self.master.meni.add_command(label = 'Трансформиши (T)',
                                 command = self.trans)
    self.master.bind('<T>', self.trans)
    self.master.bind('<t>', self.trans)

    # Vezivanje dogadjaja misa
    self.platno.bind('<Button-1>', self.tacka)
    self.platno.bind('<Button-3>', self.ponovi)

  # Dodavanje tacke na platno
  def tacka(self, dog):
    if len(self.tacke) < 4:
      self.tacke.append((dog.x-2, dog.y-2))

      # Figura mora biti konveksna
      konvt = konv(self.tacke)
      if len(konvt) != len(self.tacke):
        self.tacke.pop()
        showerror('Грешка',
                  'Унета фигура мора бити конвексна.')
        return

      # Brisanje prethodno nacrtane figure
      self.platno.delete(self.figura)

      # Brisanje prethodno nacrtanih tacaka
      [*map(self.platno.delete, self.id_tac)]
      [*map(self.platno.delete, self.id_tex)]

      # Crtanje konveksnog omota novih tacaka
      self.id_tac = [self.platno.create_oval
                  (t[0], t[1], t[0]+4, t[1]+4,
               outline = 'orange', fill = 'orange')
                       for t in self.tacke]

      # Crtanje rednih brojeva tacaka
      self.id_tex = [self.platno.create_text(
                     t[0]+12, t[1]-8,
                     text = str(i+1),
                     fill = 'blue',
                     font = 'Times 15')
                     for i, t in \
                     enumerate(self.tacke)]

      # Crtanje nove figure
      self.figura = self.platno.create_polygon([*map(
                                lambda x: (x[0]+2, x[1]+2), konvt)],
                                outline = 'yellow', fill = '') \
                                if len(self.tacke) > 1 else None

    elif len(self.ntacke) < 4:
      self.ntacke.append((dog.x-2, dog.y-2))

      # Figura mora biti konveksna
      konvt = konv(self.ntacke)
      if len(konvt) != len(self.ntacke):
        self.ntacke.pop()
        showerror('Грешка',
                  'Унета фигура мора бити конвексна.')
        return

      # Brisanje prethodno nacrtane figure
      self.platno.delete(self.nfigura)

      # Brisanje prethodno nacrtanih tacaka
      [*map(self.platno.delete, self.nid_tac)]
      [*map(self.platno.delete, self.nid_tex)]

      # Crtanje novih tacaka
      self.nid_tac = [self.platno.create_oval
                   (t[0], t[1], t[0]+4, t[1]+4,
                 outline = 'blue', fill = 'blue')
                       for t in self.ntacke]

      # Crtanje rednih brojeva tacaka
      self.nid_tex = [self.platno.create_text(
                      t[0]+12, t[1]-8,
                      text = str(i+1),
                      fill = 'orange',
                      font = 'Times 15')
                      for i, t in \
                      enumerate(self.ntacke)]

      # Crtanje nove figure
      self.nfigura = self.platno.create_polygon([*map(
                                 lambda x: (x[0]+2, x[1]+2), konvt)],
                                 outline = 'green', fill = '') \
                                 if len(self.ntacke) > 1 else None
  
  # Resetovanje unosa
  def ponovi(self, dog):
    if self.ntacke:
      self.ntacke = []
      
      # Brisanje prethodno nacrtane figure
      self.platno.delete(self.nfigura)
      
      # Brisanje prethodno nacrtanih tacaka
      [*map(self.platno.delete, self.nid_tac)]
      [*map(self.platno.delete, self.nid_tex)]

    elif self.tacke:
      self.tacke = []
      
      # Brisanje prethodno nacrtane figure
      self.platno.delete(self.figura)
      
      # Brisanje prethodno nacrtanih tacaka
      [*map(self.platno.delete, self.id_tac)]
      [*map(self.platno.delete, self.id_tex)]

    # Ponovno pokretanje aplikacije
    else:
      self.master.fajl = None
      self.master.meni.delete('Трансформиши (T)')
      self.master.unbind('<T>')
      self.master.unbind('<t>')
      self.master.postavi_frejm(Ucitavanje)
  
  # Naivno izracunavanje transformacije
  def trans(self, dog = None):
    if len(self.tacke) != 4 or 1 <= len(self.ntacke) <= 3:
      showerror('Грешка',
                'Нисте унели четири тачке.')
      return

    # Brisanje transformacije iz menija
    self.platno.unbind('<Button-1>')
    self.platno.unbind('<Button-3>')
    self.master.meni.delete('Трансформиши (T)')
    self.master.unbind('<T>')
    self.master.unbind('<t>')

    # Dodavanje progresa u meni
    self.master.meni.add_command(label = 'Обрађено: 0%')

    # Transformacija u zasebnoj niti
    nit = Thread(target = self.transt)
    nit.daemon = True
    nit.start()

  # Transformacija u zasebnoj niti
  def transt(self):
    try:
      # Skaliranje unetih tacaka prema originalu
      skala = self.master.dim[0]/self.master.ndim[0],\
              self.master.dim[1]/self.master.ndim[1]
      skaliraj = lambda x: (round(skala[0]*x[0]),
                            round(skala[1]*x[1]),
                                     1         )

      self.tacke = [*map(skaliraj, self.tacke)]
      self.ntacke = [*map(skaliraj, self.ntacke)]

      # Rektifikacija preslikanih tacaka
      self.ntacke = self.rektifikuj(self.ntacke \
                   if self.ntacke else self.tacke)
      
      # Racunanje projektivne transformacije
      matrica = naivni(self.ntacke, self.tacke)
      
      # Transformacija originalne slike
      self.master.norig = self.preslikaj(matrica)
      
      # Transformacija prikazane slike
      self.master.nslika = self.master.norig.resize(self.master.ndim,
                                                    Image.ANTIALIAS)
      
      # Prelazak na naredni frejm
      self.master.poz = self.master.winfo_x(), self.master.winfo_y()
      self.master.postavi_frejm(Prikaz)

    except:
      pass

  # Rektifikacija cetiri tacke
  def rektifikuj(self, tacke):
    # Teziste cetvorougla
    tacke = np.array(tacke)
    tez = np.mean(tacke, axis = 0)
    tez = [*map(round, tez)]

    # Najveca rastojanja po osama
    sirina, visina = 0, 0
    for i in range(len(tacke)):
      for j in range(i+1, len(tacke)):
        # Izvlacenje iz indeksa
        x = tacke[i]
        y = tacke[j]

        # Potencijalna nova sirina
        nsir = abs(x[0]-y[0]) + 1
        if nsir > sirina:
          sirina = nsir

        # Potencijalna nova visina
        nvis = abs(x[1]-y[1]) + 1
        if nvis > visina:
          visina = nvis
    
    # Pomocne promenljive
    sirina = round(sirina/2)
    visina = round(visina/2)
    sk, sl = 0, 0
    kraj = False

    # Nalazenje dve tacke dijagonale
    for i in range(len(tacke)):
      for j in range(i+1, len(tacke)):
        for k in range(len(tacke)):
          if k in (i, j):
            continue
          for l in range(len(tacke)):
            if l in (i, j, k):
              continue
            
            # Izvlacenje iz indeksa
            x = tacke[i]
            y = tacke[j]
            xx = tacke[k]
            yy = tacke[l]
            
            # Prava kroz dve tacke
            a = y[1] - x[1] 
            b = x[0] - y[0]  
            c = a*x[0] + b*x[1]
            
            sk = np.sign(a*xx[0] + b*xx[1] - c)
            sl = np.sign(a*yy[0] + b*yy[1] - c)
            
            # Dijagonala je ako su znakovi
            # druge dve tacke suprotni
            if sk != sl:
              kraj = True
              break

          if kraj:
            break
        
        if kraj:
          break

      if kraj:
        break

    # Izvlacenje iz indeksa
    ii = tacke[i]
    jj = tacke[j]
    
    # i gornja leva, j donja desna
    if ii[0] <= jj[0] and ii[1] <= jj[1]:
      tacke[i] = self.gl(tez, sirina, visina)
      tacke[j] = self.dd(tez, sirina, visina)
        
      # k donja leva, l gornja desna
      if sk < 0:
        tacke[k] = self.dl(tez, sirina, visina)
        tacke[l] = self.gd(tez, sirina, visina)
      # l donja leva, k gornja desna
      else:
        tacke[l] = self.dl(tez, sirina, visina)
        tacke[k] = self.gd(tez, sirina, visina)
     
    # i donja leva, j gornja desna
    elif ii[0] <= jj[0] and ii[1] > jj[1]:
      tacke[i] = self.dl(tez, sirina, visina)
      tacke[j] = self.gd(tez, sirina, visina)
      
      # k donja desna, l gornja leva
      if sk < 0:
        tacke[k] = self.dd(tez, sirina, visina)
        tacke[l] = self.gl(tez, sirina, visina)
      # l donja desna, k gornja leva
      else:
        tacke[l] = self.dd(tez, sirina, visina)
        tacke[k] = self.gl(tez, sirina, visina)

    # i gornja desna, j donja leva
    elif ii[0] > jj[0] and ii[1] <= jj[1]:
      tacke[i] = self.gd(tez, sirina, visina)
      tacke[j] = self.dl(tez, sirina, visina)
      
      # k gornja leva, l donja desna
      if sk < 0:
        tacke[k] = self.gl(tez, sirina, visina)
        tacke[l] = self.dd(tez, sirina, visina)
      # l gornja leva, k donja desna
      else:
        tacke[l] = self.gl(tez, sirina, visina)
        tacke[k] = self.dd(tez, sirina, visina)

    # i donja desna, j gornja leva
    else:
      tacke[i] = self.dd(tez, sirina, visina)
      tacke[j] = self.gl(tez, sirina, visina)
      
      # k gornja desna, l donja leva
      if sk < 0:
        tacke[k] = self.gd(tez, sirina, visina)
        tacke[l] = self.dl(tez, sirina, visina)
      # l gornja desna, k donja leva
      else:
        tacke[l] = self.gd(tez, sirina, visina)
        tacke[k] = self.dl(tez, sirina, visina)

    return tacke

  # Funkcije za tezisni polozaj tacke
  def gl(self, tez, sirina, visina):
    return tez[0]-sirina, tez[1]-visina, 1
  def gd(self, tez, sirina, visina):
    return tez[0]+sirina, tez[1]-visina, 1
  def dl(self, tez, sirina, visina):
    return tez[0]-sirina, tez[1]+visina, 1
  def dd(self, tez, sirina, visina):
    return tez[0]+sirina, tez[1]+visina, 1
  
  # Primena projektivne transformacije
  def preslikaj(self, matrica):
    # Inverzija matrice, kako bi se svaki piksel nove
    # slike odredjivao preko stare umesto obrnuto
    matrica = LA.inv(matrica)

    # Vadjenje matrica piksela
    spix = self.master.orig.load()
    norig = Image.new(self.master.orig.mode, self.master.dim)
    npix = norig.load()

    # Transformacija piksel po piksel; petlja
    # nije najpametnije resenje, ali omogucava
    # azuriranje progresa, sto je lepa stvar
    n, m = self.master.dim[0], self.master.dim[1]
    prog = 0
    for i in range(n):
      for j in range (m):
        # Racunanje novih koordinata
        tacka = matrica @ np.array([i, j, 1])
        tacka = tacka[0]/tacka[2], tacka[1]/tacka[2]

        # Azuriranje progresa u meniju
        progg = round(100*(i*m+j+1)/(n*m))
        if progg >= prog+1:
          prog = progg
          self.master.meni.entryconfig(3, label = f'Обрађено: {prog}%')

        # Nema preslikavanja ako je original van slike
        if tacka[0] < 0 or tacka[0] >= self.master.dim[0] \
        or tacka[1] < 0 or tacka[1] >= self.master.dim[1]:
          continue

        # Kopiranje piksela sa originalne slike
        npix[i,j] = spix[tacka]

    return norig

# Treci frejm, za prikaz rezultata
class Prikaz(Frame):
  # Konstruktor frejma
  def __init__(self, koren):
    # Log poruka o pokretanju frejma
    print('Sačuvajte transformisanu sliku.')
    
    # Pozivanje konstruktora roditeljske klase
    super().__init__(koren)
    
    # Inicijalizacija elemenata GKI
    self.init_gki()
  
  # Inicijalizacija elemenata GKI
  def init_gki(self):
    # Dimenzije odabrane slike
    dim = self.master.ndim

    # Pozicija prozora pre promene
    poz = self.master.poz
    
    # Postavljanje velicine i pozicije prozora
    self.master.geometry(f'{max(dim[0]+5, 300)}x'
                         f'{dim[1]+5}+{poz[0]}+{poz[1]}')
    
    # Postavljanje odabrane slike na prozor
    self.slika = ImageTk.PhotoImage(self.master.nslika)
    self.platno = Canvas(self, width = dim[0]+5, height = dim[1]+5)
    self.platno.create_image(dim[0]/2+2, dim[1]/2+2, image = self.slika)
    self.platno.pack()

    # Brisanje starog dela menija
    self.master.meni.delete('Обрађено: 100%')

    # Vezivanje dogadjaja misa
    self.platno.bind('<Button-3>', self.restart)
    
    # Dodavanje cuvanja slike u meni
    self.master.meni.add_command(label = 'Сачувај (S)',
                                 command = self.sacuvaj)
    self.master.bind('<S>', self.sacuvaj)
    self.master.bind('<s>', self.sacuvaj)

  # Cuvanje transformisane slike
  def sacuvaj(self, dog = None):
    fajl = asksaveasfilename(
           filetypes = (('Bitmap sličica', '*.bmp'),
                        ('Drugi tip', '*.*'))
           )
    
    if fajl:
      try:
        self.master.norig.save(fajl)
      except ValueError:
        self.master.norig.save(fajl + '.bmp')

  # Ponovno pokretanje aplikacije
  def restart(self, dog = None):
    # Brisanje cuvanja iz menija
    self.master.meni.delete('Сачувај (S)')
    self.master.unbind('<S>')
    self.master.unbind('<s>')

    # Postavljanje pocetnog frejma
    self.master.fajl = None
    self.master.postavi_frejm(Ucitavanje)

# Obavestenje o gresci ukoliko je modul
# pokrenut kao samostalan program
if __name__ == '__main__':
  greska('GKI nije samostalan program! Pokrenite main!')
