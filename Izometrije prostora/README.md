#### PPGR3
<img width="500" src="https://raw.githubusercontent.com/matfija/Projektivna-geometrija/master/Izometrije-prostora/SLerp.gif">

## Izometrije prostora :globe_with_meridians:
Drugi domaći zadatak na izbornom kursu Primena projektivne geometrije u računarstvu. Pred korisnikom je trodimenziono okruženje u kome je prikazan jedan objekat u početnom i završnom položaju, oba interno zadata središtima/centrima, kao i Ojlerovim uglovima odnosno kvaternionima. Tasterom <kbd>Space</kbd> pokreće se animacija koja objekat sfernom linearnom interpolacijom (**S**pherical **L**inear Int**erp**olation – SLerp) prevodi iz jednog položaja u drugi. Kamera je projektovana na sferu koja okružuje scenu, tako da je pomeranjem (<kbd>Q</kbd><kbd>W</kbd><kbd>E</kbd><kbd>A</kbd><kbd>S</kbd><kbd>D</kbd>) moguće posmatrati animaciju iz raznih položaja.

## Tehnički detalji :robot:
Od nestandardnih biblioteka, korišćene su [numpy](https://numpy.org/) za matematička izračunavanja i [PyOpenGL](http://pyopengl.sourceforge.net/) za grafiku, a najlakše ih je podesiti pomoću [pip](https://pip.pypa.io/en/stable/)-a i postavljene datoteke sa zavisnostima komandom poput `pip install -r reqs.txt`.

Što se tiče matematičke pozadine, implementirane su funkcije za prevođenje različitih načina predstavljanja 'orijentacija' tela u prostoru – Ojlerovi uglovi, matrice, osa i ugao, kvaternioni – iz jednog u drugi, kao i funkcije koje interpoliraju kvaternione i središta tela u vremenu. Sveukupno, ovo je mogućilo laku animaciju glatkog kretanja u odnosu na vremenske parametre.
