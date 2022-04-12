from ucenik import Ucenik
from ucenikplus import UcenikPlus
from razred import Razred
import pickle

if __name__ == '__main__':
    u1 = Ucenik("Pero Peric")
    u1.unesi_ocjenu(5, "fizika", "25.03.2022")
    u1.unesi_ocjenu(1, "fizika", "26.03.2022")
    u1.unesi_ocjenu(2, "fizika", "27.03.2022")
    u1.unesi_ocjenu(4, "matematika", "22.03.2022")
    u1.unesi_ocjenu(5, "matematika", "23.03.2022")
    u1.unesi_ocjenu(5, "matematika", "24.03.2022")
    u1.unesi_ocjenu(3, "tjelesni", "24.03.2022")
    print(u1.prosjek_predmet("matematika"))
    print(u1.prosjek_predmet("fizika"))
    print(u1.prosjek_predmet("tjelesni"))
    print(u1.predmeti_rang())
    print(u1.globalni_prosjek())
    
    print("========================")
    
    u2 = UcenikPlus("Marko Marulic")
    u2.unesi_ocjenu(4, "fizika", "25.03.2022")
    u2.unesi_ocjenu(3, "fizika", "26.03.2022")
    u2.unesi_ocjenu(2, "fizika", "27.03.2022")
    u2.unesi_ocjenu(4, "matematika", "22.03.2022")
    u2.unesi_ocjenu(4, "matematika", "23.03.2022")
    u2.unesi_ocjenu(5, "matematika", "24.03.2022")
    print(u2.prosjek_predmet("matematika"))
    print(u2.prosjek_predmet("fizika"))
    print(u2.prosjek_predmet("nestolijevo"))
    print(u2.predmeti_rang())
    print(u2.globalni_prosjek())
    
    print("========================")

    u3 = Ucenik("Grga Cvarak")
    u3.unesi_ocjenu(2, "matematika", "22.03.2022")
    u3.unesi_ocjenu(3, "matematika", "23.03.2022")
    u3.unesi_ocjenu(5, "matematika", "24.03.2022")
    u3.unesi_ocjenu(7, "matematika", "24.03.2022")
    u3.unesi_ocjenu(5, "tjelesni", "24.03.2022")
    
    r1 = Razred("4G", [u1, u2, u3])
    print(r1.ucenici_rang("tjelesni"))
    
    r1.spremi('spremljeno.dat')
    
    with open('spremljeno.dat', 'rb') as f:
        r = pickle.load(f)
    print(r)