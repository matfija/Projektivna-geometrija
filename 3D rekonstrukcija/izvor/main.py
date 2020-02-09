#!/usr/bin/env python3

# Ukljucivanje sistemskog modula
from sys import exit as greska

# Ukljucivanje funkcionalnog modula
from functools import partial

# Ukljucivanje grafickog modula
from tkinter import Tk, LabelFrame, Button

# Ukljucivanje pomocnog modula za
# kutijice sa iskacucim porukama
from tkinter.messagebox import askyesno

# Ukljucivanje modula za
# sakupljanje otpadaka
from gc import collect as otpaci

# Ukljucivanje modula za procese
from multiprocessing import Process

# Odabir rekonstrukcije
def odabir():
  # Prozor za odabir
  app = Tk()
  app.title('3D rekonstrukcija')
  app.geometry('280x170+400+300')
  app.resizable(False, False)

  # Okvir za odabir
  okvir = LabelFrame(app, text = 'Odaberite željenu 3D rekonstrukciju',
                               padx = 15, pady = 15)
  okvir.pack(padx = 5, pady = 5)

  i = 0

  def set_i(j):
    nonlocal i
    i = j
    app.destroy()

  # Dugme za prvi primer
  Button(okvir, text = 'Prvi primer sa dve kutije',
                command = partial(set_i, 1))\
        .grid(column = 0, row = 0, padx = 5, pady = 5)

  # Dugme za drugi primer
  Button(okvir, text = 'Drugi primer sa tri kutije',
                command = partial(set_i, 2))\
        .grid(column = 0, row = 1, padx = 5, pady = 5)

  # Zatvaranje prozora
  def kraj(dog = None):
    # Poruka korisniku o kraju programa
    if askyesno('Kraj programa',
                'Da li stvarno želite da napustite program?'):
      app.destroy()

  # Dugme za odustajanje
  Button(okvir, text = 'Dosta je za danas \ud83d\ude34',
                command = kraj).grid(column = 0, row = 4,
                                     padx = 5, pady = 5)

  # Vezivanje protokola zatvaranja prozora
  app.protocol('WM_DELETE_WINDOW', kraj)
  app.bind('<Escape>', kraj)

  # Glavna petlja prozora
  app.mainloop()

  # Vracanje odabira
  return i

# Glavna (main) fja
def main():
  while True:
    # Sakupljanje otpadaka
    otpaci()

    # Ukljucivanje modula za GKI
    i = odabir()
    if i == 0:
      return
    elif i == 1:
      from animacija1 import main
    elif i == 2:
      from animacija2 import main

    # Pokretanje prozora
    proc = Process(target = main)
    proc.start()
    proc.join()

# Ispitivanje globalne promenljive koja sadrzi
# ime programa kako bi se znalo da li je pravilno
# pokrenut, a ne npr. samo importovan ili uzet
# kao ulaz programu koji interpretira kod
if __name__ == '__main__':
  main()
