#### PPGR1
<img src="https://raw.githubusercontent.com/matfija/Projektivna-geometrija/master/Otklanjanje-distorzije/slike/lenax.png">

## Otklanjanje distorzije :camera:
Prvi domaći rad na izbornom kursu Primena projektivne geometrije u računarstvu. Korisnik učitava sliku/fotografiju sa datotečnog sistema, nakon čega bira četiri tačke za koje u rezultatu želi da čine pravougaonik. Po potrebi, označava još četiri tačke, čime sugeriše aplikaciji gde želi da se taj pravougaonik nađe. Razultujuću sliku može da sačuva na računaru.

Skelet programa je GKI sa platnom na kojem se prikazuju učitana i transformisana slika, kao i grafički elementi kojima se upravlja tokom izvršavanja aplikacije. Sastavni deo rada su i dodatni moduli, od kojih jedan računa konveksni omotač proizvoljnog skupa tačaka u ravni, a drugi određuje projektivne transformacije naivnim, DLT i modifikovanim DLT algoritmom sa normalizacijom tačaka, a zatim testira i upoređuje implementirane funkcionalnosti na jednom test primeru.

## Tehnički detalji :robot:
Od nestandardnih biblioteka, korišćene su [numpy](https://numpy.org/) za matematička izračunavanja i [PIL](https://pillow.readthedocs.io/en/stable/) za rad sa slikama, a najlakše ih je podesiti pomoću [pip](https://pip.pypa.io/en/stable/)-a i postavljene datoteke sa zavisnostima komandom poput `pip install -r reqs.txt`.

Što se tiče matematičke pozadine, rektifikacija izabranih tačaka (piksela) vrši se pomoću odgovarajuće projektivne transformacije. Naime, odabirom četiri tačke odnosno četiri para tačaka (parovi original-slika) u potpunosti je određena projekcija kojom se originali transformišu u slike. Kada se ta projekcija primeni na sve tačke originalne slike (preciznije, kada se inverzna transformacija primeni na sve tačke rezultujuće slike, kako bi se izbegli prazni pikseli u rezultatu), dobije se transformisana slika na kojoj je uneti četvorougao pretvoren u pravougaonik, čime je distorzija otklonjena.
