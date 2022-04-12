from ucenik import Ucenik
import pickle

class Razred:
    
    def __init__(self, ime, ucenici):
        self.ime = ime
        self.ucenici = ucenici
        
    def ucenici_rang(self, predmet):
        ucenici_s_prosjekom = list()
        for ucenik in self.ucenici:
            if isinstance(ucenik, Ucenik):
                ocjena = ucenik.prosjek_predmet(predmet)
                ucenici_s_prosjekom.append(tuple((ucenik.ime_i_prezime, ocjena)))
        sortirani_ucenici = sorted(ucenici_s_prosjekom, key=lambda x:x[1], reverse=True)
        return list(map(lambda x:x[0], sortirani_ucenici))
    
    def spremi(self, path):
        with open(path, 'wb') as file:
            pickle.dump(self, file)
            
    def __str__(self):
        return f"{self.ime}, {self.ucenici}"