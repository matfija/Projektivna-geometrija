#!/usr/bin/env python3

# Ukljucivanje sistemskog modula
from sys import exit as greska

# Ukljucivanje grafickog modula
from tkinter import Tk, Frame, Menu, Entry, Canvas, \
                        LabelFrame, Text, Button, \
                        OptionMenu, StringVar

# Ukljucivanje pomocnog modula za
# kutijice sa iskacucim porukama
from tkinter.messagebox import showinfo, showerror, askyesno

# Ukljucivanje pomocnog modula za
# kutijice sa pitanjima za korisnika
from tkinter.simpledialog import askinteger

# Ukljucivanje pomocnog modula
# za pretragu fajl sistema
from tkinter.filedialog import askopenfilenames, asksaveasfilename

# Ukljucivanje modula za niti
from threading import Thread

# Ukljucivanje modula za slike
from cv2 import imread, imshow, imwrite, \
                resize, cvtColor, COLOR_BGR2RGB
from PIL import Image, ImageTk

# Ukljucivanje modula za panoramu
from proj import spoj, panorama

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
    self.title('Прављење панораме')

    # Onemogucavanje promene velicine prozora,
    # posto je Tk prilicno plastican, pa promene
    # ugrozavaju zamisljeni izgled aplikacije
    self.resizable(False, False)

    # Inicijalizacija glavnog menija
    self.init_meni()

    # Inicijalizacija rezultata
    self.rez = None
    self.dim = 320, 170
    self.poz = 400, 300

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
    self.meni.add_command(label = 'Помоћ (H)',
                          command = self.pomoc)
    self.meni.add_command(label = 'Инфо (G)',
                          command = self.info)
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

  # Priprema slika za prikaz
  def pripremi(self, slika):
    # Pretvaranje OpenCV/numpy slike u PIL Image;
    # pritom promena u podrazumevani PIL-ov RGB
    # kolor model naspram OpenCV-jevog BGR
    slika = Image.fromarray(cvtColor(slika, COLOR_BGR2RGB))

    # Eventualno vertikalno skracivanje
    dim = slika.size
    
    if dim[1] > 550:
      slika = slika.resize((round(dim[0]*550/dim[1]), 550),
                                   Image.ANTIALIAS)

    # Eventualno horizotalno skracivanje
    dim = slika.size

    if dim[0] > 800:
      slika = slika.resize((800, round(dim[1]*800/dim[0])),
                                   Image.ANTIALIAS)

    # Vracanje skaliranog Tk PhotoImage-a
    return ImageTk.PhotoImage(slika)
  
  # Prikazivanje prozora za pomoc
  def pomoc(self, dog = None):
    showinfo('Помоћ',
             'На почетном прозору налазе се мени, дугмад за одабир'
             ' датотека и спајање, поље са списком учитаних слика,'
             ' као и падајући мени за избор типа пројекције:\n\n'
             '\u2022 ручно – отварају се нови прозори са по две учитане'
             ' слике на којима левим кликовима миша бирате'
             ' кореспондентне тачке, а затим покрећете спајање,\n'
             '\u2022 раван – слике се пројектују на заједничку раван,\n'
             '\u2022 ваљак – слично као претходно, с тим што се, као'
             ' припремни корак, слике репројектују на ваљак, што смањује'
             ' искривљеност резултујуће панораме.\n\n'
             'Након завршене претраге фајлова, искључиво у редоследу'
             ' слева надесно, добија се резултујућа панорама, направљена'
             ' на одабрани начин и са изабраном централном сликом, а коју'
             ' можете сачувати на рачунару. У случају грешке, можете'
             ' поновити унос десним кликом миша. Апликацију рестартујете'
             ' на исти начин.')
  
  # Prikazivanje glavnih informacija o aplikaciji
  def info(self, dog = None):
    showinfo('Информације',
             'Домаћи из Примене пројективне геометрије у рачунарству:'
             ' прављење панорамске слике.\n\n'
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

# Prvi frejm, za ucitavanje slika
class Ucitavanje(Frame):
  # Konstruktor frejma
  def __init__(self, koren):
    # Log poruka o pokretanju frejma
    print('Odaberite slike za transformaciju.')
    
    # Pozivanje konstruktora roditeljske klase
    super().__init__(koren)

    # Lista slika za spajanje
    self.master.slike = []
    self.fajlovi = []
    
    # Inicijalizacija elemenata GKI
    self.init_gki()
  
  # Inicijalizacija elemenata GKI
  def init_gki(self):
    # Postavljanje velicine i pozicije prozora
    poz = self.master.poz
    dim = self.master.dim
    self.master.geometry(f'{dim[0]}x{dim[1]}+{poz[0]}+{poz[1]}')
    
    # Okvir za odabir
    okvir = LabelFrame(self, text = 'Одаберите слике:',
                             padx = 5, pady = 5)
    okvir.grid(column = 0, row = 0,
               padx = 15, pady = 10)
    
    # Dugme za pretragu
    self.pret = Button(okvir, text = 'Претражи (P)',
		              command = self.pretrazi)
    self.pret.grid(column = 2, row = 0,
		   padx = 5, pady = 5)
    self.master.bind('<P>', self.pretrazi)
    self.master.bind('<p>', self.pretrazi)

    # Dugme za spajanje
    self.spojd = Button(okvir, text = 'Спој (S)',
                               command = self.spoj)
    self.spojd.grid(column = 1, row = 0,
		    padx = 5, pady = 5)
    self.master.bind('<S>', self.spoj)
    self.master.bind('<s>', self.spoj)

    # Padajuci meni za projekciju
    self.tr = StringVar(self)
    self.tr.set('ручно')
    
    self.meni = OptionMenu(okvir, self.tr,
                                  'ручно', 'раван', 'ваљак')
    self.meni.grid(column = 3, row = 0,
	           padx = 5, pady = 5)

    # Kutijica sa spiskom slika
    self.kutijica = Text(okvir, height = 5, width = 30,
                                  state = 'disabled')
    self.kutijica.grid(column = 1, columnspan = 3, row = 1)

    # Vezivanje dogadjaja
    self.master.bind('<Button-3>', self.restart)
    self.master.bind('<R>', self.restart)
    self.master.bind('<r>', self.restart)

  # Racunanje panorame
  def pano(self, srednja):
    try:
      self.master.rez = panorama(self.master.slike, srednja,
                                 self.tr.get() == 'ваљак')
    except:
      pass

    # Prelazak na naredni frejm
    try:
      self.master.poz = self.master.winfo_x(), self.master.winfo_y()
      self.master.postavi_frejm(Rezultat)
    except:
      pass
  
  # Spajanje slika
  def spoj(self, dog = None):
    if not self.master.slike:
      showerror('Грешка',
                'Нисте одабрали слике за спајање.')
      return

    # Opozivanje dogadjaja
    self.master.unbind('<P>')
    self.master.unbind('<p>')
    self.master.unbind('<R>')
    self.master.unbind('<r>')
    self.master.unbind('<S>')
    self.master.unbind('<s>')
    self.master.unbind('<Button-3>')

    # Odredjivanje srednje slike
    n = len(self.master.slike)-1
    if n == 0:
      srednja = None
    else:
      srednja = askinteger('Центар панораме',
                'За коју слику желите да буде центар панораме,\n'
               f'дакле, фиксирана? Дозвољени опсег је [1, {n+1}].\n'
               f'Препоручена вредност је средња слика, овде {n//2+1}.\n'
                'Она ће бити одабрана уколико ништа не унесете.',
                parent = self, minvalue = 1, maxvalue = n+1)

    # Automatski odabir ako korisnik odustane
    if srednja is None:
      srednja = n//2
    else:
      srednja -= 1
    
    # Rucno spajanje zahteva novi frejm
    if self.tr.get() == 'ручно':
      # Priprema slika za obilazak redom;
      # uzimanje poslednje slike kao pocetne
      self.master.rez = self.master.slike.pop()

      # Nema posla ako je samo jedna slika
      if n == 0:
        self.master.postavi_frejm(Rezultat)
        return
      
      # Sleva se spaja leva polovina panorame
      for i in range(srednja):
        self.master.slike[i] = self.master.slike[i], True
      
      # Zdesna se spaja desna polovina panorame
      for i in range(srednja, n):
        self.master.slike[i] = self.master.slike[i], False
      
      self.master.poz = self.master.winfo_x(), self.master.winfo_y()
      self.master.postavi_frejm(Rucno)
      return

    # Blokiranje dugmadi i menija
    self.pret.config(state = 'disabled')
    self.spojd.config(state = 'disabled')
    self.meni.config(state = 'disabled')

    # Transformacija u zasebnoj niti
    nit = Thread(target = self.pano, args = [srednja])
    nit.daemon = True
    nit.start()
  
  # Pretraga slika
  def pretrazi(self, dog = None):
    fajlovi = askopenfilenames(
              filetypes = [('Svi tipovi', '*.*')]
              )

    if not fajlovi:
      return

    # Citanje slike iz fajla
    for fajl in fajlovi:
      slika = imread(fajl)

      if slika is None:
        showerror('Грешка',
                  'Одабрана датотека није слика.')
        continue
      
      # Eventualno vertikalno skracivanje
      dim = slika.shape[1], slika.shape[0]

      if dim[1] > 550:
        dim = round(dim[0]*550/dim[1]), 550
      
      # Eventualno horizotalno skracivanje
      if dim[0] > 800:
        dim = 800, round(dim[1]*800/dim[0])

      # Prikaz ucitane slike i njeno dodavanje
      # u spisak naziva ucitanih datoteka
      imshow(f'Pregled slike {len(self.fajlovi)+1}', resize(slika, dim))
      self.master.slike.append(slika)
      self.fajlovi.append(fajl[fajl.rfind('/')+1:])

      # Popunjavanje kutijice sa fajlovima
      self.osvezi()
  
  # Popunjavanje kutijice sa fajlovima
  def osvezi(self):
    self.kutijica.config(state = 'normal')
    self.kutijica.delete(1.0, 'end')
    self.kutijica.insert('end', '\n'.join(self.fajlovi))
    self.kutijica.config(state = 'disabled')

  # Ponistavanje poslednjeg unosa
  def restart(self, dog = None):
    if not self.master.slike:
      return
    
    self.master.slike.pop()
    self.fajlovi.pop()
    
    self.osvezi()

# Srednji frejm, za rucno spajanje
class Rucno(Frame):
  # Konstruktor frejma
  def __init__(self, koren):
    # Log poruka o pokretanju frejma
    print('Odaberite korespondentne tačke.')
    
    # Pozivanje konstruktora roditeljske klase
    super().__init__(koren)

    # Inicijalizacija odabranih tacaka
    self.ltacke = []
    self.dtacke = []

    # Inicijalizacija iscrtavanja
    self.lid_tac = []
    self.lid_tex = []
    self.did_tac = []
    self.did_tex = []

    # Inicijalizacija elemenata GKI
    self.init_gki()
  
  # Inicijalizacija elemenata GKI
  def init_gki(self):
    # Priprema ucitanih slika za prikaz
    self.trenutna = self.master.slike.pop()
    self.lslika = self.master.pripremi(self.trenutna[0])
    self.dslika = self.master.pripremi(self.master.rez)

    # Dimenzije pripremljenih slika
    poz = self.master.poz
    ldim = self.lslika.width(), self.lslika.height()
    ddim = self.dslika.width(), self.dslika.height()
    
    # Postavljanje velicine i pozicije prozora
    self.master.geometry(f'{ldim[0]+ddim[0]+4}x'
                         f'{max(ldim[1],ddim[1])+2}+'
                         f'{poz[0]}+{poz[1]}')
    
    # Postavljanje ucitanih slika na prozor
    self.lplatno = Canvas(self, width = ldim[0]+2, height = ldim[1]+2,
                                borderwidth = 0, highlightthicknes = 0)
    self.lplatno.create_image(ldim[0]/2+1, ldim[1]/2+1, image = self.lslika)
    self.lplatno.grid(row = 0, column = 0)
    self.dplatno = Canvas(self, width = ddim[0]+2, height = ddim[1]+2,
                                borderwidth = 0, highlightthicknes = 0)
    self.dplatno.create_image(ddim[0]/2+1, ddim[1]/2+1, image = self.dslika)
    self.dplatno.grid(row = 0, column = 1)

    # Dodavanje transformacije u meni
    self.master.meni.add_command(label = 'Спој (S)',
                                 command = self.spoj)
    self.master.bind('<S>', self.spoj)
    self.master.bind('<s>', self.spoj)

    # Vezivanje dogadjaja misa
    self.lplatno.bind('<Button-1>', self.ltacka)
    self.lplatno.bind('<Button-3>', self.lponovi)
    self.dplatno.bind('<Button-1>', self.dtacka)
    self.dplatno.bind('<Button-3>', self.dponovi)

    # Ponovno pokretanje aplikacije
    self.master.bind('<R>', self.restart)
    self.master.bind('<r>', self.restart)

  # Racunanje panorame
  def pano(self):
    try:
      self.master.rez = spoj(self.trenutna[0],
                             self.master.rez,
                             sleva = self.trenutna[1],
                             nove = self.ltacke,
                             orig = self.dtacke)
    except:
      self.master.rez = None
      self.master.slike = []

    # Prelazak na naredni frejm
    try:
      self.master.poz = self.master.winfo_x(), self.master.winfo_y()

      # Rezultat ako su obradjene sve slike, inace dalje
      if len(self.master.slike) == 0:
        self.master.postavi_frejm(Rezultat)
      else:
        self.master.postavi_frejm(Rucno)
    except:
      pass

  # Spajanje slika
  def spoj(self, dog = None):
    if len(self.ltacke) != len(self.dtacke):
      if not askyesno('Упозорење',
                      'Није одабран исти број тачака на сликама.\n'
                      'Желите ли аутоматски одабир за ове слике?'):
        return

    elif len(self.ltacke) < 4:
      if not askyesno('Упозорење',
                      'Потребно је одабрати макар четири пара тачака.\n'
                      'Желите ли аутоматски одабир за ове слике?'):
        return

    # Opozivanje dogadjaja
    self.master.unbind('<S>')
    self.master.unbind('<s>')
    self.master.meni.delete('Спој (S)')
    self.master.unbind('<R>')
    self.master.unbind('<r>')
    self.lplatno.unbind('<Button-1>')
    self.lplatno.unbind('<Button-3>')
    self.dplatno.unbind('<Button-1>')
    self.dplatno.unbind('<Button-3>')

    # Skaliranje levih tacaka prema originalu
    sdim = self.trenutna[0].shape
    ndim = self.lslika.width(), self.lslika.height()
    skala = sdim[1]/ndim[0], sdim[0]/ndim[1]
    skaliraj = lambda x: (round(skala[0]*x[0]),
                          round(skala[1]*x[1]))
    self.ltacke = [*map(skaliraj, self.ltacke)]

    # Skaliranje desnih tacaka prema originalu
    sdim = self.master.rez.shape
    ndim = self.dslika.width(), self.dslika.height()
    skala = sdim[1]/ndim[0], sdim[0]/ndim[1]
    skaliraj = lambda x: (round(skala[0]*x[0]),
                          round(skala[1]*x[1]))
    self.dtacke = [*map(skaliraj, self.dtacke)]

    # Transformacija u zasebnoj niti
    nit = Thread(target = self.pano)
    nit.daemon = True
    nit.start()

  # Dodavanje tacke na levo platno
  def ltacka(self, dog = None):
    if dog is not None:
      self.ltacke.append((dog.x-1, dog.y-1))

    # Brisanje prethodno nacrtanih tacaka
    [*map(self.lplatno.delete, self.lid_tac)]
    [*map(self.lplatno.delete, self.lid_tex)]

    # Crtanje novih tacaka
    self.lid_tac = [self.lplatno.create_oval
                (t[0]-1, t[1]-1, t[0]+3, t[1]+3,
               outline = 'orange', fill = 'orange')
                     for t in self.ltacke]

    # Crtanje rednih brojeva tacaka
    self.lid_tex = [self.lplatno.create_text(
                    t[0]+11, t[1]-9,
                    text = str(i+1),
                    fill = 'blue',
                    font = 'Times 15')
                    for i, t in \
                    enumerate(self.ltacke)]

  # Dodavanje tacke na desno platno
  def dtacka(self, dog = None):
    if dog is not None:
      self.dtacke.append((dog.x-1, dog.y-1))

    # Brisanje prethodno nacrtanih tacaka
    [*map(self.dplatno.delete, self.did_tac)]
    [*map(self.dplatno.delete, self.did_tex)]

    # Crtanje novih tacaka
    self.did_tac = [self.dplatno.create_oval
                (t[0]-1, t[1]-1, t[0]+3, t[1]+3,
                outline = 'blue', fill = 'blue')
                     for t in self.dtacke]

    # Crtanje rednih brojeva tacaka
    self.did_tex = [self.dplatno.create_text(
                    t[0]+11, t[1]-9,
                    text = str(i+1),
                    fill = 'orange',
                    font = 'Times 15')
                    for i, t in \
                    enumerate(self.dtacke)]
  
  # Ponistavanje tacke na levom platnu
  def lponovi(self, dog):
    if self.ltacke:
      self.ltacke.pop()
      self.ltacka()
  
  # Ponistavanje tacke na desnom platnu
  def dponovi(self, dog):
    if self.dtacke:
      self.dtacke.pop()
      self.dtacka()

  # Ponovno pokretanje aplikacije
  def restart(self, dog = None):
    # Poruka korisniku o restartovanju
    if askyesno('Поновно покретање',
                'Да ли стварно желите да рестартујете програм?'):
      # Pamcenje polozaja prozora
      self.master.poz = self.master.winfo_x(), self.master.winfo_y()

      # Brisanje spajanja iz menija
      self.master.meni.delete('Спој (S)')

      # Vracanje na pocetni frejm
      self.master.postavi_frejm(Ucitavanje)

# Poslednji frejm, za prikaz rezultata
class Rezultat(Frame):
  # Konstruktor frejma
  def __init__(self, koren):
    # Log poruka o pokretanju frejma
    print('Sačuvajte panoramsku sliku.')
    
    # Pozivanje konstruktora roditeljske klase
    super().__init__(koren)

    # Inicijalizacija elemenata GKI
    if self.master.rez is not None:
      self.init_gki()
    else:
      self.greska()
  
  # Inicijalizacija elemenata GKI
  def init_gki(self):
    # Priprema rezultujuce slike za prikaz
    self.slika = self.master.pripremi(self.master.rez)
    
    # Postavljanje velicine i pozicije prozora
    poz = self.master.poz
    dim = self.slika.width(), self.slika.height()
    self.master.geometry(f'{dim[0]+1}x{dim[1]+1}+{poz[0]}+{poz[1]}')

    # Postavljanje rezultujuce slike na prozor
    self.platno = Canvas(self, width = dim[0], height = dim[1],
                               borderwidth = 0, highlightthicknes = 0)
    self.platno.create_image(dim[0]/2, dim[1]/2, image = self.slika)
    self.platno.pack()

    # Restartovanje aplikacije
    self.platno.bind('<Button-3>', self.restart)
    self.master.bind('<R>', self.restart)
    self.master.bind('<r>', self.restart)
    
    # Dodavanje cuvanja slike u meni
    self.master.meni.add_command(label = 'Сачувај (S)',
                                 command = self.sacuvaj)
    self.master.bind('<S>', self.sacuvaj)
    self.master.bind('<s>', self.sacuvaj)

  # Inicijalizacija GKI za gresku
  def greska(self):
    # Postavljanje velicine i pozicije prozora
    poz = self.master.poz
    dim = self.master.dim
    self.master.geometry(f'{dim[0]}x{dim[1]}+{poz[0]}+{poz[1]}')
    
    # Okvir za gresku
    okvir = LabelFrame(self, text = 'Рестартујте апликацију:',
                             padx = 35, pady = 35)
    okvir.grid(column = 0, row = 0,
               padx = 15, pady = 10)
    
    # Dugme za ponovno pokretanje
    restartuj = Button(okvir, text = 'Рестартуј (R)',
		              command = self.restart)
    restartuj.grid(column = 0, row = 0,
		   padx = 5, pady = 5)
    self.master.bind('<R>', self.restart)
    self.master.bind('<r>', self.restart)

    # Vezivanje dogadjaja misa
    self.master.bind('<Button-3>', self.restart)

    # Obavestenje o gresci
    showerror('Грешка',
              'Није могуће спојити одабране слике. Слике нису део'
              ' панораме, нису поређане слева надесно, област преклапања'
              ' је исувише нејасна за препознавање или је дошло до неког'
              ' другог непремостивог проблема. Уколико то желите,'
              ' покушајте са неким другим сликама.')

  # Cuvanje panoramske slike
  def sacuvaj(self, dog = None):
    fajl = asksaveasfilename(
           filetypes = [('Bilo koji tip', '*.*')]
           )
    
    if fajl:
      try:
        imwrite(fajl, self.master.rez)
      except:
        imwrite(fajl + '.bmp', self.master.rez)

  # Ponovno pokretanje aplikacije
  def restart(self, dog = None):
    # Poruka korisniku o restartovanju
    if self.master.rez is None or \
       askyesno('Поновно покретање',
                'Да ли стварно желите да рестартујете програм?'):
      # Pamcenje polozaja prozora
      self.master.poz = self.master.winfo_x(), self.master.winfo_y()

      # Resetovanje globalnih podataka
      if self.master.rez is not None:
        self.master.meni.delete('Сачувај (S)')
        self.master.rez = None

      # Vracanje na pocetni frejm
      self.master.postavi_frejm(Ucitavanje)

# Obavestenje o gresci ukoliko je modul
# pokrenut kao samostalan program
if __name__ == '__main__':
  greska('GKI nije samostalan program! Pokrenite main!')
