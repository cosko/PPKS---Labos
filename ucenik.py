class Ucenik:
    
    def __init__(self, ime_i_prezime):
        self.ime_i_prezime = ime_i_prezime
        self.ocjene = dict()
        
    def unesi_ocjenu(self, ocjena, predmet, datum):
        if ocjena < 1 or ocjena > 5:
            print("Unesena ocjena (%d) nije valjana, mora biti u rasponu [1, 5]." % ocjena)
            return
        if predmet not in self.ocjene:
            self.ocjene[predmet] = list()
        self.ocjene[predmet].append(tuple((ocjena, datum)))
            
    def prosjek_predmet(self, predmet):
        if predmet not in self.ocjene:
            print("Učenik još nema unesenu ocjenu za predmet: {}".format(predmet))
            return 0
        popis_ocjena = self.ocjene.get(predmet)
        sum = 0
        for ocjena in popis_ocjena:
            sum += ocjena[0]
        return sum/len(popis_ocjena)
    
    def predmeti_rang(self):
        prosjecne_ocjene = self.__dohvati_sve_prosjecne_ocjene()
        sortirane_prosjecne_ocjene = sorted(prosjecne_ocjene, key=lambda p: p[1], reverse=True)
        sortirani_predmeti = map(lambda x:x[0], sortirane_prosjecne_ocjene)
        return list(sortirani_predmeti)
    
    def __dohvati_sve_prosjecne_ocjene(self):
        prosjecne_ocjene = list()
        for predmet in self.ocjene.keys():
            prosjecne_ocjene.append(tuple((predmet, self.prosjek_predmet(predmet))))
        return prosjecne_ocjene
    
    def globalni_prosjek(self):
        #prosjek prosjecnih ocjena
        ppo = self._dohvati_prosjek_prosjecnih_ocjena()
        
        #prosjek svih ocjena
        pso = self._dohvati_prosjek_svih_ocjena();
        return ppo, pso
    
    def _dohvati_prosjek_prosjecnih_ocjena(self):
        sum = 0
        prosjecne_ocjene = self.__dohvati_sve_prosjecne_ocjene()
        for prosjecna_ocjena in prosjecne_ocjene:
            sum += prosjecna_ocjena[1]
        return (sum / len(prosjecne_ocjene))
    
    def _dohvati_prosjek_svih_ocjena(self):
        sum = 0
        br = 0
        for predmet in self.ocjene.keys():
            for ocjena in self.ocjene[predmet]:
                sum += ocjena[0]
                br += 1
        return (sum / br)
            
    def __str__(self):
        return f"{self.ime_i_prezime}, {self.ocjene}"