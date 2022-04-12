from ucenik import Ucenik
import math

class UcenikPlus(Ucenik):
    
    def prosjek_predmet(self, predmet):
        return math.ceil(super().prosjek_predmet(predmet))
    
    def _dohvati_prosjek_prosjecnih_ocjena(self):
        return math.ceil(super()._dohvati_prosjek_prosjecnih_ocjena())
    
    def _dohvati_prosjek_svih_ocjena(self):
        return math.ceil(super()._dohvati_prosjek_svih_ocjena())