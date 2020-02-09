#### PPGR2
<img width="700" src="https://raw.githubusercontent.com/matfija/Projektivna-geometrija/master/Pravljenje-panorame/slike/rucno/rucno1.png">
<img width="700" src="https://raw.githubusercontent.com/matfija/Projektivna-geometrija/master/Pravljenje-panorame/slike/rucno/rucno2.png">
<img width="700" src="https://raw.githubusercontent.com/matfija/Projektivna-geometrija/master/Pravljenje-panorame/slike/rucno/rucno3.png">
<img width="700" src="https://raw.githubusercontent.com/matfija/Projektivna-geometrija/master/Pravljenje-panorame/slike/rucno/rucno4.png">

## Pravljenje panorame :camera:
Opcioni domaći rad na izbornom kursu Primena projektivne geometrije u računarstvu. Korisnik učitava slike/fotografije sa datotečnog sistema, nakon čega bira način pravljenja panorame: ručnim unosom korespondentnih tačaka mišem, automatskom projekcijom na zajedničku ravan, automatskom projekcijom na zajedničku ravan sa prethodnom reprojekcijom na valjak radi smanjenja izobličenja. Razultujuću sliku može da sačuva na računaru.

Skelet programa je GKI pomoću koga se učitavaju i prikazuju originalne i transformisana slika, kao i grafički elementi kojima se upravlja tokom izvršavanja aplikacije. Sastavni deo rada je i pomoćni modul koji određuje odgovarajuću projektivnu transformaciju koristeći, između ostalog, RANSAC algoritam, nakon čega spaja slike na mestima preklapanja.

## Tehnički detalji :robot:
Od nestandardnih biblioteka, korišćene su [PIL](https://pillow.readthedocs.io/en/stable/) i [OpenCV](https://opencv.org/) za rad sa slikama, a najlakše ih je podesiti pomoću [pip](https://pip.pypa.io/en/stable/)-a i postavljene datoteke sa zavisnostima komandom poput `pip install -r reqs.txt`.

Što se tiče matematičke pozadine, uprošćeno na slučaj dve slike, panorama se dobija iz suštinski dva koraka. U prvom, biraju se najmanje četiri para korespondentnih tačaka na obe slike. Tako je moguće izračunati odgovarajuću projektivnu transformaciju kojom se jedna slika preslikava u koordinatni sistem druge. Eventualni autlajeri filtriraju se RANSAC algoritmom. U drugom, dolazi do samog spajanja slika, što se čini pažljivom iteracijom kroz piksele preklapajuće oblasti. Pritom se pazi i na dimenzije rezultujuće slike, kao i na to da ne dođe do prevelikog isecanja ili iskrivljenja.
