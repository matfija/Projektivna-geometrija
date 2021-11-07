#### PPGR

## Primena projektivne geometrije u računarstvu :globe_with_meridians::computer:
Repozitorijum sa domaćim zadacima na izbornom predmetu Primena projektivne geometrije u računarstvu:
* otklanjanje projektivne (perspektivne) distorzije na slici,
  * rektifikacija proizvoljne četvorke tačaka u opštem položaju,
* pravljenje panorame od dve ili više preklapajućih slika,
* implementacija i animacija kretanja (izometrija) prostora,
* rekonstrukcija prostornih koordinata objekta iz dve slike.

Rad je u proširenoj verziji predstavljen na [X simpozijumu „Matematika i primene“](https://alas.matf.bg.ac.rs/~konferencija/2019/), u okviru sekcije posvećene naučnoistraživačkom i stručnom radu studenata. Moguće je pronaći ga u [programu](https://alas.matf.bg.ac.rs/~konferencija/Program2019.pdf), kao i u [knjizi apstrakata](https://alas.matf.bg.ac.rs/~konferencija/KNJIGA_APSTRAKATA_2019.pdf).

## Detalji i podešavanje :memo:
Svi programi su napisani u jeziku Python (tada najsvežija verzija 3.7.5), na operativnom sistemu Windows, uz upotrebu zvaničnog [IDLE](https://docs.python.org/3/library/idle.html)-a kao integrisanog razvojnog okruženja, ali, usled fleksibilnosti samog Pythona, rade i na drugim operativnim sistemima, kao što su Ubuntu i druge distribucije Linuxa.

GKI je odrađen pomoću standardnog Tk/Tcl paketa – [tkinter](https://docs.python.org/3/library/tkinter.html) – koji se može podesiti komandom poput `sudo apt-get install python3-tk` za Ubuntu za starije verzije, dok je za novije automatski podešen. Nema dodatne potrebe za podešavanjem ni u slučaju rada sa IDLE-om.

Nakon kloniranja (`git clone https://github.com/matfija/Projektivna-geometrija`) tj. bilo kog načina preuzimanja repozitorijuma, željeni program se pokreće pozivanjem Pajtonovog interpretatora nad glavnim fajlom, što je moguće učiniti komandom poput `python3 main.py` za sisteme poput Ubuntua ili `python main.py` za sisteme poput Windowsa.

Osim toga, omogućeno je i direktno pokretanje komandom poput `./main.py`, pošto se na početku svake datoteke sa glavnom (main ili test) fjom nalazi shebang koji sugeriše operativnom sistemu gde se nalazi neophodni interpretator. Naravno, za ovaj pristup je neophodno prethodno učiniti fajl izvršivim komandom poput `chmod u+x main.py`.

Za oba navedena podržana sistema dostupne su release verzije rada na odgovarajućoj [stranici](https://github.com/matfija/Projektivna-geometrija/releases) na GitHub adresi projekta, što uključuje .exe za Windows 10, ali i niže verzije u slučaju posedovanja odgovarajućih rantajm biblioteka.
