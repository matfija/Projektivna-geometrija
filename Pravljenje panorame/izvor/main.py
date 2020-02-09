#!/usr/bin/env python3

# Ukljucivanje modula za GKI
from gki import PPGR

# Glavna (main) fja
def main():
  # Instanciranje objekta stozerne klase
  aplikacija = PPGR()
  
  # Pokretanje glavne petlje programa
  aplikacija.mainloop()

# Ispitivanje globalne promenljive koja sadrzi
# ime programa kako bi se znalo da li je pravilno
# pokrenut, a ne npr. samo importovan ili uzet
# kao ulaz programu koji interpretira kod
if __name__ == '__main__':
  main()
