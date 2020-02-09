#### PPGR4
<img width="500" src="https://raw.githubusercontent.com/matfija/Projektivna-geometrija/master/3D-rekonstrukcija/slike/3DrekNew.gif">
<img width="500" src="https://raw.githubusercontent.com/matfija/Projektivna-geometrija/master/3D-rekonstrukcija/slike/levaNew_oznake.jpg">

## 3D rekonstrukcija :globe_with_meridians:
Treći domaći zadatak na izbornom kursu Primena projektivne geometrije u računarstvu. Na osnovu dve fotografije snimljene iz različitih uglova, rekonstruišu se prostorne koordinate fotografisanog objekta odnosno naslaganih 'kutija' u konkretnom slučaju. Kamera je projektovana na sferu koja okružuje scenu, te ju je moguće pomerati (<kbd>Q</kbd><kbd>W</kbd><kbd>E</kbd><kbd>A</kbd><kbd>S</kbd><kbd>D</kbd> ili mišem).

## Tehnički detalji :robot:
Od nestandardnih biblioteka, korišćene su [numpy](https://numpy.org/) za matematička izračunavanja i [PyOpenGL](http://pyopengl.sourceforge.net/) za grafiku, a najlakše ih je podesiti pomoću [pip](https://pip.pypa.io/en/stable/)-a i postavljene datoteke sa zavisnostima komandom poput `pip install -r reqs.txt`.

Što se tiče matematičke pozadine, prvo je izračunata fundamentalna matrica na osnovu korespondencija. Iz nje su dobijeni epipolovi, a iz njih nadalje kanonske matrice kamera, na osnovu kojih je naposletku izvršena triangulacija.
